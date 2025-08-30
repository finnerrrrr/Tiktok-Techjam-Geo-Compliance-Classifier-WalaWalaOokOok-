# utils/rag.py
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.retrievers import BM25Retriever
from langchain_core.retrievers import BaseRetriever
from langchain.schema import Document
from sentence_transformers import CrossEncoder
from typing import List
import numpy as np
import os
from . import semanticchunker as sc

def create_vector_db_from_dir(directory_path, persist_directory, embedding_model):
    """Create a Chroma vector DB and BM25 index from raw text files."""
    documents = []
    for filename in os.listdir(directory_path):
        if not filename.endswith(".txt"):
            continue
        filepath = os.path.join(directory_path, filename)
        try:
            law_name, chunked_doc = sc.get_chunks(filepath)  # List[str]
        except Exception as e:
            print(f"[RAG] Skipping {filename}: {e}")
            continue

        if not chunked_doc:
            print(f"[RAG] Skipping {filename}: produced 0 chunks")
            continue

        for i, chunk in enumerate(chunked_doc):
            documents.append(
                Document(page_content=chunk, metadata={"law": law_name, "source": filename, "chunk_number": i})
            )

    if not documents:
        raise ValueError(f"No usable .txt files found in {directory_path}")

    vectordb = Chroma.from_documents(
        documents=documents,
        embedding=embedding_model,
        persist_directory=persist_directory
    )
    vectordb.persist()

    bm25_retriever = BM25Retriever.from_documents(documents)

    return vectordb, bm25_retriever


def get_vector_db(persist_directory, embedding_model):
    """Load an existing Chroma vector database and build a BM25 index."""
    vectordb = Chroma(persist_directory=persist_directory, embedding_function=embedding_model)
    items = vectordb.get()
    documents = [Document(page_content=doc, metadata=meta) for doc, meta in zip(items["documents"], items["metadatas"])]
    bm25_retriever = BM25Retriever.from_documents(documents)
    return vectordb, bm25_retriever


class HybridRetriever(BaseRetriever):
    """Combine dense and sparse retrievers with re-ranking and diversification."""

    def __init__(
        self,
        vectorstore: Chroma,
        bm25_retriever: BM25Retriever,
        embedding_model: HuggingFaceEmbeddings,
        cross_encoder_model: str = "cross-encoder/ms-marco-MiniLM-L-6-v2",
        k: int = 5,
        lambda_mult: float = 0.5,
        facet_key: str = "law",
    ) -> None:
        self.vectorstore = vectorstore
        self.bm25_retriever = bm25_retriever
        self.embedding_model = embedding_model
        self.cross_encoder = CrossEncoder(cross_encoder_model)
        self.k = k
        self.lambda_mult = lambda_mult
        self.facet_key = facet_key

    # BaseRetriever interface
    def get_relevant_documents(self, query: str) -> List[Document]:
        dense_docs = self.vectorstore.similarity_search(query, k=self.k)
        self.bm25_retriever.k = self.k
        sparse_docs = self.bm25_retriever.get_relevant_documents(query)
        candidates = self._dedupe(dense_docs + sparse_docs)
        if not candidates:
            return []

        scores = self.cross_encoder.predict([(query, d.page_content) for d in candidates])
        ranked_docs = [d for d, _ in sorted(zip(candidates, scores), key=lambda x: x[1], reverse=True)]

        mmr_docs = self._apply_mmr(query, ranked_docs)
        balanced_docs = self._facet_balance(mmr_docs)
        return balanced_docs

    # Utility methods
    def _dedupe(self, docs: List[Document]) -> List[Document]:
        seen = set()
        unique_docs = []
        for doc in docs:
            key = (doc.page_content, frozenset(doc.metadata.items()))
            if key not in seen:
                seen.add(key)
                unique_docs.append(doc)
        return unique_docs

    def _apply_mmr(self, query: str, docs: List[Document]) -> List[Document]:
        if not docs:
            return []
        query_emb = self.embedding_model.embed_query(query)
        doc_embs = self.embedding_model.embed_documents([d.page_content for d in docs])
        selected = []
        candidates = list(range(len(docs)))
        while candidates and len(selected) < min(self.k, len(docs)):
            if not selected:
                idx = int(np.argmax(np.dot(doc_embs, query_emb)))
                selected.append(idx)
                candidates.remove(idx)
                continue
            mmr_scores = []
            for idx in candidates:
                sim_query = np.dot(doc_embs[idx], query_emb)
                sim_selected = max(np.dot(doc_embs[idx], doc_embs[j]) for j in selected)
                mmr_scores.append(self.lambda_mult * sim_query - (1 - self.lambda_mult) * sim_selected)
            best_idx = candidates[int(np.argmax(mmr_scores))]
            selected.append(best_idx)
            candidates.remove(best_idx)
        return [docs[i] for i in selected]

    def _facet_balance(self, docs: List[Document]) -> List[Document]:
        if not docs:
            return []
        selected: List[Document] = []
        used = set()
        for doc in docs:
            facet = doc.metadata.get(self.facet_key)
            if facet not in used:
                selected.append(doc)
                used.add(facet)
            if len(selected) >= self.k:
                return selected
        for doc in docs:
            if doc not in selected:
                selected.append(doc)
            if len(selected) >= self.k:
                break
        return selected

# Use a good open-source embedding model
embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

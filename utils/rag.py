from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.retrievers import BM25Retriever
from langchain_core.retrievers import BaseRetriever
from langchain.schema import Document
from typing import List, Optional, Dict, Tuple, Any
import os

from . import semanticchunker as sc

def create_vector_db_from_dir(directory_path: str, persist_directory: str, embedding_model):
    """Create a Chroma vector DB and BM25 index from raw text files.

    Each `.txt` file is assumed to follow the convention
    ``<jurisdiction>_<law_code>_<clause>.txt`` and live under a domain
    sub-folder (e.g. ``kb/data_privacy/SG_PDPA2012.txt``).  Metadata for
    ``domain``, ``jurisdiction`` and ``clause`` are attached to every
    chunk so downstream agents can filter and cite sources precisely.
    """

    documents: List[Document] = []
    for dirpath, _, filenames in os.walk(directory_path):
        for filename in filenames:
            if not filename.endswith(".txt"):
                continue
            filepath = os.path.join(dirpath, filename)

            try:
                law_name, chunked_doc = sc.get_chunks(filepath)
            except Exception as e:
                print(f"[RAG] Skipping {filename}: {e}")
                continue

            if not chunked_doc:
                print(f"[RAG] Skipping {filename}: produced 0 chunks")
                continue

            # Determine metadata
            rel_dir = os.path.relpath(dirpath, directory_path)
            domain = rel_dir.split(os.sep)[0] if rel_dir != "." else "general"
            base = os.path.splitext(filename)[0]
            parts = base.split("_")
            jurisdiction = parts[0] if len(parts) > 0 else ""
            law_code = parts[1] if len(parts) > 1 else ""
            clause = parts[2] if len(parts) > 2 else ""

            source_path = os.path.join(rel_dir, filename) if rel_dir != "." else filename

            for i, chunk in enumerate(chunked_doc):
                documents.append(
                    Document(
                        page_content=chunk,
                        metadata={
                            "law": law_name,
                            "domain": domain,
                            "jurisdiction": jurisdiction,
                            "law_code": law_code,
                            "clause": clause,
                            "source": source_path,
                            "chunk_number": i,
                        },
                    )
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


def get_vector_db(persist_directory: str, embedding_model):
    """Load an existing Chroma vector database and rebuild the BM25 index."""
    vectordb = Chroma(persist_directory=persist_directory, embedding_function=embedding_model)
    items = vectordb.get()
    documents = [Document(page_content=doc, metadata=meta) for doc, meta in zip(items["documents"], items["metadatas"])]
    bm25_retriever = BM25Retriever.from_documents(documents)
    return vectordb, bm25_retriever


class HybridRetriever(BaseRetriever):
    """Hybrid retriever using reciprocal rank fusion over dense and sparse results."""

    vectorstore: Chroma
    bm25_retriever: BM25Retriever
    k: int = 5
    rrf_k: int = 60

    class Config:
        arbitrary_types_allowed = True

    def __init__(
        self,
        vectorstore: Chroma,
        bm25_retriever: BM25Retriever,
        k: int = 5,
        rrf_k: int = 60,
        **data
    ) -> None:
        super().__init__(
            vectorstore=vectorstore,
            bm25_retriever=bm25_retriever,
            k=k,
            rrf_k=rrf_k,
            **data
        )

    def get_relevant_documents(
        self, query: str, *, filters: Optional[Dict[str, str]] = None
    ) -> List[Document]:
        """Retrieve top ``k`` documents using semantic + BM25 fusion."""

        dense_docs = self.vectorstore.similarity_search(query, k=self.k, filter=filters)

        self.bm25_retriever.k = self.k
        sparse_docs = self.bm25_retriever.get_relevant_documents(query)
        if filters:
            sparse_docs = [d for d in sparse_docs if all(d.metadata.get(key) == val for key, val in filters.items())]

        scored: Dict[Tuple[str, Tuple[Tuple[str, Any], ...]], Tuple[Document, float]] = {}

        def _update_scores(docs: List[Document]) -> None:
            for rank, doc in enumerate(docs):
                key = (doc.page_content, tuple(sorted(doc.metadata.items())))
                score = 1 / (self.rrf_k + rank + 1)
                if key in scored:
                    scored[key] = (doc, scored[key][1] + score)
                else:
                    scored[key] = (doc, score)

        _update_scores(dense_docs)
        _update_scores(sparse_docs)

        ranked_docs = sorted(scored.values(), key=lambda x: x[1], reverse=True)
        return [doc for doc, _ in ranked_docs[: self.k]]

    # Add the async version if needed by LangChain
    async def aget_relevant_documents(
        self, query: str, *, filters: Optional[Dict[str, str]] = None
    ) -> List[Document]:
        """Async version of get_relevant_documents."""
        return self.get_relevant_documents(query, filters=filters)
      
# Use a good open-source embedding model
embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

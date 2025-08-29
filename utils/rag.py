# utils/rag.py
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.schema import Document
import os
from . import semanticchunker as sc

def create_vector_db_from_dir(directory_path, persist_directory, embedding_model):
    documents = []
    for filename in os.listdir(directory_path):
        if not filename.endswith(".txt"):
            continue
        filepath = os.path.join(directory_path, filename)
        try:
            chunked_doc = sc.get_chunks(filepath)  # List[str]
        except Exception as e:
            print(f"[RAG] Skipping {filename}: {e}")
            continue

        if not chunked_doc:
            print(f"[RAG] Skipping {filename}: produced 0 chunks")
            continue

        for i, chunk in enumerate(chunked_doc):
            documents.append(
                Document(page_content=chunk, metadata={"source": filename, "chunk_number": i})
            )

    if not documents:
        raise ValueError(f"No usable .txt files found in {directory_path}")

    vectordb = Chroma.from_documents(
        documents=documents,
        embedding=embedding_model,
        persist_directory=persist_directory
    )
    vectordb.persist()
    return vectordb


def get_vector_db(persist_directory, embedding_model):
    """Loads an existing Chroma vector database."""
    vectordb = Chroma(persist_directory=persist_directory, embedding_function=embedding_model)
    return vectordb

# Use a good open-source embedding model
embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)
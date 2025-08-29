# agents/base_agent.py
from abc import ABC, abstractmethod
from langchain.schema import BaseRetriever

class BaseAgent(ABC):
    def __init__(self, name, retriever: BaseRetriever):
        self.name = name
        self.retriever = retriever

    @abstractmethod
    def analyze_feature(self, feature_description: str) -> dict:
        """
        Analyze a feature description. Must return a dict with:
        {
            "requires_geo_compliance": bool,
            "reasoning": str,
            "related_regulations": list
        }
        """
        pass

    def _retrieve_context(self, query: str, k: int = 5) -> str:
        """Retrieves relevant context from the agent's knowledge base."""
        docs = self.retriever.get_relevant_documents(query)
        context = "\n\n".join([doc.page_content for doc in docs])
        sources = [{"chunk text": doc.page_content, "source": doc.metadata.get("source", "unknown"), 
                   "chunk_number": doc.metadata.get("chunk_number", "unknown")} 
                  for doc in docs]
        return context, sources

    def _create_optimized_query(self, feature_description: str) -> str:
        """Simple query optimization. Override this in child classes for more sophistication."""
        # For a robust version, you'd use an LLM here as discussed.
        # This is a simple placeholder.
        return f"{feature_description} legal compliance regulation law"
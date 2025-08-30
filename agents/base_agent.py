# agents/base_agent.py
from abc import ABC, abstractmethod
from langchain.schema import BaseRetriever
from pydantic import BaseModel, Field
from typing import List, Tuple

# Define Pydantic models for structured return data
class RetrievedSource(BaseModel):
    chunk_text: str = Field(description="The actual text content of the chunk")
    source: str = Field(description="Filename or document source")
    chunk_number: str = Field(description="Numerical identifier for this chunk")
    law: str = Field(description="Name of the law this chunk belongs to")

class RetrievalResult(BaseModel):
    laws: List[str] = Field(description="Unique list of laws referenced in the retrieved chunks")
    context: str = Field(description="Concatenated text of all retrieved chunks")
    sources: List[RetrievedSource] = Field(description="List of source metadata for each chunk")

class BaseAgent(ABC):
    def __init__(self, name, retriever: BaseRetriever):
        self.name = name
        self.retriever = retriever

    @abstractmethod
    def analyze_feature(self, feature_description: str) -> dict:
        """
        Analyze a feature summary. Must return a dict with:
        {
            "Content-Moderation Concern": [Yes/No/Unclear]
            "Analysis": [reasoning with law name(s) and chunk number(s)]
            "Related Regulations": [list of cited laws or 'None']
        }
        """
        pass        

    def _retrieve_context(self, query: str, k: int = 5) -> RetrievalResult:
        """Retrieves relevant context from the agent's knowledge base."""
        docs = self.retriever.get_relevant_documents(query)
        
        # Build context string
        context = "\n\n".join([doc.page_content for doc in docs])
        
        # Build sources list with validation
        sources = []
        laws_set = set()
        
        for doc in docs:
            source = RetrievedSource(
                chunk_text=doc.page_content,
                source=doc.metadata.get("source", "unknown"),
                chunk_number=str(doc.metadata.get("chunk_number", "unknown")),
                law=doc.metadata.get("law", "unknown")
            )
            sources.append(source)
            laws_set.add(source.law)
        
        # Convert set to sorted list for consistent output
        laws = sorted(list(laws_set))
        
        return RetrievalResult(laws=laws, context=context, sources=sources)

    # def _create_optimized_query(self, feature_description: str) -> str:
    #     """Simple query optimization. Override this in child classes for more sophistication."""
    #     return f"{feature_description} legal compliance regulation law"
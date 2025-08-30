# agents/base_agent.py
from __future__ import annotations

from typing import Any, Dict, List
from pydantic import BaseModel, Field
import os, sys

# Make ../utils importable
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from utils.rag import RAGSearcher  # hybrid searcher (semantic + BM25)


class RetrievedChunk(BaseModel):
    """Single retrieval unit (matches rag.py output shape)."""
    content: str = Field(description="Chunk text")
    relevance_score: float = Field(description="0..10 hybrid score")
    metadata: Dict[str, Any] = Field(
        default_factory=dict,
        description="Chunk metadata from the VDB (e.g., law, source, chunk_number, jurisdiction)"
    )


class BaseAgent:
    """
    Minimal domain agent:
      • holds a domain-specific VDB
      • runs hybrid RAG via RAGSearcher
      • returns top-k chunks (no judgments)
    """

    def __init__(self, name: str, vdb: Any, semantic_weight: float = 0.60, bm25_weight: float = 0.40):
        """
        Args:
          name: Display name, e.g. "Youth Safety Agent"
          vdb:  Duck-typed vector DB with:
                - chunks (list[dict|obj{content, metadata}])
                - embeddings (np.ndarray, L2-normalized)
                - bm25 (rank_bm25.BM25Okapi)
                - embedder or embedder_name (SentenceTransformer or str)
        """
        self.name = name
        self.vdb = vdb
        self.searcher = RAGSearcher(semantic_weight=semantic_weight, bm25_weight=bm25_weight)

    def analyze_feature(
        self,
        prepped_query: str | Dict[str, Any],
        top_k: int = 5,
        candidate_k_each: int = 50,
    ) -> List[Dict[str, Any]]:
        """
        Perform hybrid retrieval and return k most relevant chunks.

        Returns a list of dicts (directly from RAGSearcher):
          [
            {"content": str, "relevance_score": float, "metadata": dict},
            ...
          ]
        """
        results = self.searcher.search(
            vdb=self.vdb,
            prepped_query=prepped_query,
            top_k=top_k,
            candidate_k_each=candidate_k_each,
        )
        return results
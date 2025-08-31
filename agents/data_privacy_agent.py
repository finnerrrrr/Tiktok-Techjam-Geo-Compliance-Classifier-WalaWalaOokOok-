# agents/youth_safety_agent.py
# -*- coding: utf-8 -*-
"""
Simple YouthSafetyAgent

- Points RAG to the Youth Safety corpus directory (default: "kb/youth_safety").
- Accepts a *prepped query* (string or dict) from the Query Prep agent.
- Calls RAG to run a fixed-weight hybrid search and returns the top-k chunks.

Each returned item has:
{
  "law_name": str,
  "chunk": str,
  "relevance_score": float,  # 0..10
  "domain": str              # e.g., "youth_safety"
}
"""

from typing import Any, Dict, List, Union
from utils.rag import RAGEngine


class DataPrivacyAgent:
    def __init__(
        self,
        domain_dir: str = "kb/data_privacy",
        model_name: str = "sentence-transformers/all-MiniLM-L6-v2",
        top_k: int = 5,
    ) -> None:
        self.name = "Data Privacy Agent"
        self.top_k = top_k
        # Build the domain-specific RAG engine once (chunks, embeddings, BM25)
        self._engine = RAGEngine.from_domain_dir(domain_dir, model_name=model_name)

    def analyze_feature(self, prepped_query: Union[str, Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        Pass the prepped query straight to RAG and return the top-k results.
        """
        return self._engine.search(prepped_query, top_k=self.top_k)

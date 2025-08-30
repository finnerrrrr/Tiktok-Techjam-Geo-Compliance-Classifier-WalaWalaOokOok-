# utils/rag.py
# -*- coding: utf-8 -*-
"""
RAG utility for domain agents.

What this module does
---------------------
1) Build an in-memory VDB for a given *domain directory* (e.g. "utils/consumer_protection"):
   - Iterates all `.txt` files (recursive).
   - Uses `semanticchunker.get_chunks(path)` to produce (law_name, [chunks...]).
   - Stores chunks with metadata {law_name, domain, source, chunk_number}.
   - Creates BOTH:
       • Sentence-Transformer embeddings (L2-normalized) for semantic similarity
       • BM25 index over tokenized chunk text for lexical similarity

2) Execute a **hybrid search** against the VDB using a *prepped query* (string or dict):
       hybrid_score = 0.60 * semantic_cosine + 0.40 * bm25_norm
   Returns ONLY the top-5 chunks as:
       { "law_name": str, "chunk": str, "relevance_score": float, "domain": str }

Notes
-----
- This module is pure Python with `sentence-transformers` and `rank_bm25`.
- The "prepped query" can be a dict from your Query Prep agent:
    {
      "feature_title": "...",
      "feature_description": "...",
      "feature_requirements": "...",
      "potential_impacts": "...",
      "regions": "EU"
    }
  We combine these into one search string (light weighting).
"""

from __future__ import annotations

import os
import re
import math
from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Tuple, Union

import numpy as np
from rank_bm25 import BM25Okapi
from sentence_transformers import SentenceTransformer

# Import your semantic chunker (must live next to this file as utils/semanticchunker.py)
from . import semanticchunker as sc


# ---------------------------
# Small tokenizer for BM25
# ---------------------------
_TOKEN_RE = re.compile(r"[A-Za-z0-9]+", re.UNICODE)
def _tok(text: str) -> List[str]:
    return _TOKEN_RE.findall(text.lower())


# ---------------------------
# Chunk container
# ---------------------------
@dataclass
class _Chunk:
    text: str
    law_name: str
    domain: str
    source: str
    chunk_number: int


# ---------------------------
# RAG Engine
# ---------------------------
class RAGEngine:
    """
    Build & query a domain-specific VDB.

    Usage:
        engine = RAGEngine.from_domain_dir("utils/consumer_protection")
        results = engine.search(prepped_query, top_k=5)
        # results: List[{"law_name","chunk","relevance_score","domain"}]
    """

    def __init__(self, model_name: str = "sentence-transformers/all-MiniLM-L6-v2"):
        self.model_name = model_name
        self.embedder = SentenceTransformer(model_name)

        self.domain: str = ""                # e.g. "consumer_protection"
        self.chunks: List[_Chunk] = []       # ordered list of chunks
        self._embeddings: Optional[np.ndarray] = None   # (N, d), L2-normalized
        self._bm25: Optional[BM25Okapi] = None
        self._doc_tokens: List[List[str]] = []

    # ---------- Build ----------
    @classmethod
    def from_domain_dir(cls, domain_dir: str, model_name: str = "sentence-transformers/all-MiniLM-L6-v2") -> "RAGEngine":
        """
        Build an engine by scanning a directory containing `.txt` files for a specific domain.
        Recursively walks the directory tree.
        """
        engine = cls(model_name=model_name)
        if not os.path.isdir(domain_dir):
            raise FileNotFoundError(f"Domain directory not found: {domain_dir}")

        engine.domain = os.path.basename(os.path.normpath(domain_dir)) or "general"

        txt_files: List[str] = []
        for root, _dirs, files in os.walk(domain_dir):
            for fname in files:
                if fname.lower().endswith(".txt"):
                    txt_files.append(os.path.join(root, fname))

        if not txt_files:
            raise ValueError(f"No .txt files found in {domain_dir}")

        # Chunk each file with semanticchunker
        for path in txt_files:
            try:
                law_name, chunk_list = sc.get_chunks(path)  # returns (law_name, [chunk_str, ...])
            except Exception as e:
                print(f"[RAG] Skipping {os.path.basename(path)}: {e}")
                continue
            if not chunk_list:
                continue

            rel_source = os.path.relpath(path, start=domain_dir)
            for i, chunk_text in enumerate(chunk_list):
                engine.chunks.append(
                    _Chunk(
                        text=chunk_text,
                        law_name=law_name or os.path.splitext(os.path.basename(path))[0],
                        domain=engine.domain,
                        source=rel_source,
                        chunk_number=i,
                    )
                )

        if not engine.chunks:
            raise ValueError(f"semanticchunker produced 0 chunks in {domain_dir}")

        # Build BM25 + embeddings
        engine._doc_tokens = [_tok(c.text) for c in engine.chunks]
        engine._bm25 = BM25Okapi(engine._doc_tokens)

        texts = [c.text for c in engine.chunks]
        emb = engine.embedder.encode(texts, normalize_embeddings=True, convert_to_numpy=True)
        engine._embeddings = emb

        return engine

    # ---------- Query ----------
    def search(
        self,
        prepped_query: Union[str, Dict[str, Any]],
        top_k: int = 5,
        semantic_weight: float = 0.60,
        bm25_weight: float = 0.40,
    ) -> List[Dict[str, Any]]:
        """
        Hybrid search over the engine's VDB and return the top_k chunks.

        Returns (each item):
            {
              "law_name": str,
              "chunk": str,
              "relevance_score": float,   # 0..10 (hybrid)
              "domain": str
            }
        """
        if not self.chunks or self._embeddings is None or self._bm25 is None:
            raise RuntimeError("Engine not initialized. Use RAGEngine.from_domain_dir(...) first.")

        # 1) Prepare query text from dict or string
        q_text = _combine_prepped_query(prepped_query)

        # 2) Semantic & BM25 scores for all docs
        q_vec = self.embedder.encode([q_text], normalize_embeddings=True, convert_to_numpy=True)[0]
        sem_scores = (self._embeddings @ q_vec)  # cosine similarity in [-1,1], mostly >= 0 for MiniLM
        bm25_scores = self._bm25.get_scores(_tok(q_text))  # arbitrary positive scale

        # 3) Normalize each score vector to 0..1
        sem_n = _minmax_norm(sem_scores.tolist())
        bm25_n = _minmax_norm(bm25_scores.tolist())

        # 4) Hybrid score (fixed weights)
        s = semantic_weight + bm25_weight
        sw = semantic_weight / s
        bw = bm25_weight / s
        hybrid = [sw * s_ + bw * b_ for s_, b_ in zip(sem_n, bm25_n)]

        # 5) Rank and select top_k
        order = np.argsort(-np.asarray(hybrid))[: top_k]

        results: List[Dict[str, Any]] = []
        for idx in order:
            score_0_10 = 10.0 * float(hybrid[idx])  # human-readable scale
            c = self.chunks[idx]
            results.append({
                "law_name": c.law_name,
                "chunk": c.text,
                "relevance_score": round(score_0_10, 3),
                "domain": c.domain,
            })

        return results


# ---------------------------
# Helpers
# ---------------------------
def _minmax_norm(values: List[float]) -> List[float]:
    if not values:
        return []
    vmin, vmax = float(min(values)), float(max(values))
    if math.isclose(vmin, vmax):
        return [0.5 for _ in values]
    return [(v - vmin) / (vmax - vmin) for v in values]


def _combine_prepped_query(q: Union[str, Dict[str, Any]]) -> str:
    """
    Convert a structured 'prepped query' into a single search string.
    Lightly prioritizes title/description and keeps a 'region:<X>' hint if present.
    """
    if isinstance(q, str):
        return q.strip()

    def _safe(s: Any) -> str:
        return str(s).strip() if isinstance(s, (str, int, float)) else ""

    parts: List[str] = []
    title   = _safe(q.get("feature_title"))
    desc    = _safe(q.get("feature_description"))
    reqs    = _safe(q.get("feature_requirements"))
    impacts = _safe(q.get("potential_impacts"))
    regions = _safe(q.get("regions"))

    if title:   parts.append(title)
    if desc:    parts.append(desc)
    if reqs:    parts.append(reqs)
    if impacts: parts.append(impacts)
    if regions: parts.append(f"region:{regions}")

    return " ".join(parts).strip()

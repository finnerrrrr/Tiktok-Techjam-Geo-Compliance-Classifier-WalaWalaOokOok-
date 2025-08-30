# utils/rag.py
# -*- coding: utf-8 -*-
"""
RAG (Retrieve–Augment) — hybrid search over an ALREADY-BUILT domain VDB.

This module assumes the *domain agent* has already:
  • chunked its corpus (e.g., via your semanticchunker)
  • computed document embeddings (L2-normalized) with a SentenceTransformer
  • built a BM25Okapi index over chunk tokens
  • stored these in a VDB object

What this module does:
  • Accepts that VDB + a PREPPED query (string or dict from your QueryPrep agent)
  • Runs hybrid search with FIXED weights:
        hybrid = 0.60 * semantic_cosine + 0.40 * bm25_norm
  • Returns ONLY the top_k chunks (default 5) as:
        { "content": str, "relevance_score": float(0..10), "metadata": dict }

Expected VDB interface (duck-typed; no base class required):
  vdb.chunks           -> List[chunk_items]; each chunk_item has either:
                           - dict form: {"content": str, "metadata": dict}
                           - attr form: .content: str, .metadata: dict
  vdb.embeddings       -> np.ndarray of shape (N, d), L2-normalized
  vdb.bm25             -> rank_bm25.BM25Okapi instance over the same chunks
  vdb.embedder         -> (optional) a SentenceTransformer instance for query encoding
  vdb.embedder_name    -> (optional) model name string for lazy loading if embedder not provided
"""

from __future__ import annotations

import math
import re
from typing import Any, Dict, List, Optional, Tuple, Union

import numpy as np
from rank_bm25 import BM25Okapi
from sentence_transformers import SentenceTransformer


# ---------------------------
# Lightweight tokenizer for BM25
# ---------------------------
_TOKEN_RE = re.compile(r"[A-Za-z0-9]+", re.UNICODE)
def _tok(text: str) -> List[str]:
    return _TOKEN_RE.findall(text.lower())


# ---------------------------
# Core Searcher
# ---------------------------
class RAGSearcher:
    """
    Executes HYBRID search over a provided VDB:
        hybrid = 0.60 * semantic_cosine + 0.40 * bm25_norm

    Returns ONLY the top_k chunks with human-friendly scores (0..10).
    """

    def __init__(self, semantic_weight: float = 0.60, bm25_weight: float = 0.40):
        if not (0.0 <= semantic_weight <= 1.0 and 0.0 <= bm25_weight <= 1.0):
            raise ValueError("Weights must be in [0,1].")
        s = semantic_weight + bm25_weight
        self.semantic_weight = semantic_weight / s
        self.bm25_weight = bm25_weight / s
        self._embedder_cache: Dict[str, SentenceTransformer] = {}

    def search(
        self,
        vdb: Any,  # duck-typed VDB (see file docstring)
        prepped_query: Union[str, Dict[str, Any]],
        top_k: int = 5,
        candidate_k_each: int = 50,
    ) -> List[Dict[str, Any]]:
        """
        Args
        ----
        vdb: object with {chunks, embeddings, bm25, (embedder|embedder_name)}
        prepped_query: string OR dict with fields like:
            {
              "feature_title": "...",
              "feature_description": "...",
              "feature_requirements": "...",
              "potential_impacts": "...",
              "regions": "EU"
            }
        top_k: number of results to return (default 5)
        candidate_k_each: shortlist size per modality before fusion (default 50)

        Returns
        -------
        List[dict] where each item is:
            {
              "content": str,
              "relevance_score": float (0..10),
              "metadata": dict
            }
        """
        # --- validate VDB surface ---
        _ensure_has(vdb, "chunks")
        _ensure_has(vdb, "embeddings")
        _ensure_has(vdb, "bm25")

        if len(vdb.chunks) == 0:
            return []

        # 1) Build a single query string
        q_text = _combine_prepped_query(prepped_query)

        # 2) Encode query using the SAME embedder
        embedder = _resolve_embedder(vdb, self._embedder_cache)
        q_vec = embedder.encode([q_text], normalize_embeddings=True, convert_to_numpy=True)[0]

        # 3) Modality scores over ALL docs
        emb: np.ndarray = vdb.embeddings
        if not isinstance(emb, np.ndarray):
            raise TypeError("vdb.embeddings must be a NumPy ndarray")
        if emb.ndim != 2 or emb.shape[0] != len(vdb.chunks):
            raise ValueError("vdb.embeddings shape must be (N, d) aligned with vdb.chunks")

        sem_scores_all = (emb @ q_vec)  # cosine similarity
        if not isinstance(vdb.bm25, BM25Okapi):
            raise TypeError("vdb.bm25 must be a rank_bm25.BM25Okapi instance")
        bm25_scores_all = vdb.bm25.get_scores(_tok(q_text))  # arbitrary positive scale

        # 4) Per-modality candidates
        sem_rank = np.argsort(-sem_scores_all)
        bm_rank = np.argsort(-bm25_scores_all)
        sem_cands = sem_rank[: min(candidate_k_each, len(sem_rank))]
        bm_cands = bm_rank[: min(candidate_k_each, len(bm_rank))]
        cand_ids = list(dict.fromkeys(list(sem_cands) + list(bm_cands)))  # dedup, preserve order

        # Edge case: fewer candidates than requested
        if not cand_ids:
            return []

        # 5) Normalize scores within the candidate union
        sem = [float(sem_scores_all[i]) for i in cand_ids]
        bm = [float(bm25_scores_all[i]) for i in cand_ids]
        sem_n = _minmax_norm(sem)  # 0..1
        bm_n = _minmax_norm(bm)    # 0..1

        # 6) Hybrid score
        hybrid = [self.semantic_weight * s + self.bm25_weight * b for s, b in zip(sem_n, bm_n)]
        order = np.argsort(-np.asarray(hybrid))[: top_k]

        # 7) Build results
        results: List[Dict[str, Any]] = []
        for pos in order:
            idx = cand_ids[pos]
            content, meta = _get_content_and_meta(vdb.chunks[idx])
            score_0_10 = 10.0 * float(hybrid[pos])
            results.append({
                "content": content,
                "relevance_score": round(score_0_10, 3),
                "metadata": meta,
            })

        return results


# ---------------------------
# Helpers
# ---------------------------
def _ensure_has(obj: Any, attr: str) -> None:
    if not hasattr(obj, attr):
        raise AttributeError(f"VDB is missing required attribute: {attr}")

def _get_content_and_meta(item: Any) -> Tuple[str, Dict[str, Any]]:
    # Supports dict items or objects with .content/.metadata
    if isinstance(item, dict):
        content = item.get("content", "")
        meta = item.get("metadata", {}) or {}
        return content, meta
    if hasattr(item, "content"):
        content = getattr(item, "content")
        meta = getattr(item, "metadata", {}) or {}
        return content, meta
    raise TypeError("Chunk item must be a dict with keys {'content','metadata'} or have attributes .content/.metadata")

def _resolve_embedder(vdb: Any, cache: Dict[str, SentenceTransformer]) -> SentenceTransformer:
    # Prefer an already-initialized embedder on the VDB
    embedder = getattr(vdb, "embedder", None)
    if isinstance(embedder, SentenceTransformer):
        return embedder
    # Else, load by name (and cache)
    name = getattr(vdb, "embedder_name", None)
    if not isinstance(name, str) or not name.strip():
        raise AttributeError("VDB must provide either .embedder (SentenceTransformer) or .embedder_name (str)")
    if name not in cache:
        cache[name] = SentenceTransformer(name)
    return cache[name]

def _minmax_norm(values: List[float]) -> List[float]:
    if not values:
        return []
    vmin, vmax = float(min(values)), float(max(values))
    if math.isclose(vmin, vmax):
        return [0.5 for _ in values]
    return [(v - vmin) / (vmax - vmin) for v in values]

def _combine_prepped_query(q: Union[str, Dict[str, Any]]) -> str:
    """
    Converts a structured prepped query dict into a single search string.
    If q is already a string, returns as-is.
    Dict fields used (all optional): feature_title, feature_description,
    feature_requirements, potential_impacts, regions.
    """
    if isinstance(q, str):
        return q.strip()

    parts: List[str] = []
    title   = _safe_str(q.get("feature_title"))
    desc    = _safe_str(q.get("feature_description"))
    reqs    = _safe_str(q.get("feature_requirements"))
    impacts = _safe_str(q.get("potential_impacts"))
    regions = _safe_str(q.get("regions"))

    if title:   parts.append(title)
    if desc:    parts.append(desc)
    if reqs:    parts.append(reqs)
    if impacts: parts.append(impacts)
    if regions: parts.append(f"region:{regions}")

    return " ".join(parts).strip()

def _safe_str(x: Any) -> str:
    return str(x).strip() if isinstance(x, (str, int, float)) else ""

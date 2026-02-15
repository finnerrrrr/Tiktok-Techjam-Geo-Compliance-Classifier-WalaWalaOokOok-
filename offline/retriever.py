from __future__ import annotations

from dataclasses import dataclass
from typing import List, Sequence

from fastembed import SparseTextEmbedding, TextEmbedding
from qdrant_client import QdrantClient, models

from offline.domain_inference import all_domains
from offline.qdrant_config import QdrantSettings

DENSE_MODEL_NAME = "BAAI/bge-small-en-v1.5"
SPARSE_MODEL_NAME = "Qdrant/bm25"


@dataclass
class RetrievedEvidence:
    chunk_id: str
    domain: str
    law_name: str
    source_path: str
    text: str
    score: float
    parent_id: str = ""
    parent_snippet: str = ""


class ComplianceRetriever:
    def __init__(self, settings: QdrantSettings | None = None):
        self.settings = settings or QdrantSettings.from_env()
        self.client = QdrantClient(
            url=self.settings.url,
            api_key=self.settings.api_key,
            timeout=self.settings.timeout,
            prefer_grpc=self.settings.prefer_grpc,
        )
        self.collection_name = self.settings.collection_name
        self._domains = all_domains()

        self._dense_model = TextEmbedding(model_name=DENSE_MODEL_NAME)
        self._sparse_model = SparseTextEmbedding(model_name=SPARSE_MODEL_NAME)

    @property
    def available_domains(self) -> List[str]:
        return list(self._domains)

    def _domain_filter(self, allowed_domains: Sequence[str] | None) -> models.Filter | None:
        domains = [domain.lower() for domain in (allowed_domains or []) if domain]
        if not domains:
            return None
        return models.Filter(
            must=[
                models.FieldCondition(
                    key="domain",
                    match=models.MatchAny(any=domains),
                )
            ]
        )

    def _query_hybrid(self, query: str, query_filter: models.Filter | None, limit: int):
        dense_query = list(self._dense_model.embed([query]))[0].tolist()
        sparse_query_raw = list(self._sparse_model.embed([query]))[0]
        sparse_query = models.SparseVector(
            indices=sparse_query_raw.indices.tolist(),
            values=sparse_query_raw.values.tolist(),
        )

        return self.client.query_points(
            collection_name=self.collection_name,
            prefetch=[
                models.Prefetch(
                    using="dense",
                    query=dense_query,
                    filter=query_filter,
                    limit=max(limit * 3, 20),
                ),
                models.Prefetch(
                    using="sparse",
                    query=sparse_query,
                    filter=query_filter,
                    limit=max(limit * 3, 20),
                ),
            ],
            query=models.FusionQuery(fusion=models.Fusion.RRF),
            limit=limit,
            with_payload=True,
        )

    def _convert_hits(self, response) -> List[RetrievedEvidence]:
        points = getattr(response, "points", response)
        evidence: List[RetrievedEvidence] = []
        for point in points:
            payload = point.payload or {}
            evidence.append(
                RetrievedEvidence(
                    chunk_id=str(payload.get("chunk_id", "")),
                    domain=str(payload.get("domain", "unknown")),
                    law_name=str(payload.get("law_name", "unknown")),
                    source_path=str(payload.get("source_path", "")),
                    text=str(payload.get("child_text", "")),
                    score=float(getattr(point, "score", 0.0)),
                    parent_id=str(payload.get("parent_id", "")),
                    parent_snippet=str(payload.get("parent_text", "")),
                )
            )
        return evidence

    def search(self, query: str, allowed_domains: Sequence[str] | None = None, top_k: int = 5) -> List[RetrievedEvidence]:
        if not query.strip():
            return []

        domain_filter = self._domain_filter(allowed_domains)
        response = self._query_hybrid(query=query, query_filter=domain_filter, limit=top_k)
        hits = self._convert_hits(response)

        if hits:
            return hits

        # Fallback to unfiltered search if filtered results are empty.
        if domain_filter is not None:
            fallback_response = self._query_hybrid(query=query, query_filter=None, limit=top_k)
            return self._convert_hits(fallback_response)

        return []

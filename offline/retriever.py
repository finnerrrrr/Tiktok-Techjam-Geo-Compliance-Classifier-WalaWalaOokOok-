from __future__ import annotations

from dataclasses import dataclass
from typing import List, Sequence

from fastembed import LateInteractionTextEmbedding, SparseTextEmbedding, TextEmbedding
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
        self._late_model = LateInteractionTextEmbedding(model_name=self.settings.late_interaction_model_name)

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

    @staticmethod
    def _to_dense(vector) -> list[float]:
        return vector.tolist() if hasattr(vector, "tolist") else list(vector)

    @staticmethod
    def _to_multivector(vectors) -> list[list[float]]:
        if hasattr(vectors, "tolist"):
            matrix = vectors.tolist()
        else:
            matrix = vectors
        return [row.tolist() if hasattr(row, "tolist") else list(row) for row in matrix]

    def _query_late(self, query: str):
        if hasattr(self._late_model, "query_embed"):
            return list(self._late_model.query_embed([query]))[0]
        return list(self._late_model.embed([query]))[0]

    def _query_hybrid_with_late_rerank(
        self,
        query: str,
        query_filter: models.Filter | None,
        top_k: int,
        recall_limit: int,
    ):
        dense_query = self._to_dense(list(self._dense_model.embed([query]))[0])

        sparse_query_raw = list(self._sparse_model.embed([query]))[0]
        if hasattr(sparse_query_raw, "as_object"):
            sparse_query = models.SparseVector(**sparse_query_raw.as_object())
        else:
            sparse_query = models.SparseVector(
                indices=sparse_query_raw.indices.tolist(),
                values=sparse_query_raw.values.tolist(),
            )

        late_query = self._to_multivector(self._query_late(query))

        prefetch = [
            models.Prefetch(
                query=dense_query,
                using=self.settings.dense_vector_name,
                filter=query_filter,
                limit=recall_limit,
            ),
            models.Prefetch(
                query=sparse_query,
                using=self.settings.sparse_vector_name,
                filter=query_filter,
                limit=recall_limit,
            ),
        ]

        return self.client.query_points(
            collection_name=self.collection_name,
            prefetch=prefetch,
            query=late_query,
            using=self.settings.late_vector_name,
            with_payload=True,
            limit=top_k,
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

        recall_limit = max(top_k * self.settings.hybrid_recall_multiplier, self.settings.hybrid_recall_min)
        domain_filter = self._domain_filter(allowed_domains)

        response = self._query_hybrid_with_late_rerank(
            query=query,
            query_filter=domain_filter,
            top_k=top_k,
            recall_limit=recall_limit,
        )
        hits = self._convert_hits(response)

        # Fallback to unfiltered search if filtered results are empty.
        if not hits and domain_filter is not None:
            fallback_response = self._query_hybrid_with_late_rerank(
                query=query,
                query_filter=None,
                top_k=top_k,
                recall_limit=recall_limit,
            )
            hits = self._convert_hits(fallback_response)

        return hits

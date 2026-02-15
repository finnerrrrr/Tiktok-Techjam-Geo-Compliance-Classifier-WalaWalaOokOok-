from __future__ import annotations

import os
from typing import Optional

from pydantic import BaseModel, Field
from qdrant_client import models


class QdrantSettings(BaseModel):
    url: str = Field(default="http://localhost:6333")
    api_key: Optional[str] = Field(default=None)
    collection_name: str = Field(default="geo_compliance_hybrid_v1")
    timeout: float = Field(default=30.0)
    prefer_grpc: bool = Field(default=False)
    vector_size: int = Field(default=384)
    distance: str = Field(default="Cosine")
    recreate_collection: bool = Field(default=False)

    @classmethod
    def from_env(cls) -> "QdrantSettings":
        return cls(
            url=os.getenv("QDRANT_URL", "http://localhost:6333"),
            api_key=os.getenv("QDRANT_API_KEY"),
            collection_name=os.getenv("QDRANT_COLLECTION", "geo_compliance_hybrid_v1"),
            timeout=float(os.getenv("QDRANT_TIMEOUT", "30")),
            prefer_grpc=os.getenv("QDRANT_PREFER_GRPC", "false").lower() == "true",
            vector_size=int(os.getenv("QDRANT_VECTOR_SIZE", "384")),
            distance=os.getenv("QDRANT_DISTANCE", "Cosine"),
            recreate_collection=os.getenv("QDRANT_RECREATE_COLLECTION", "false").lower() == "true",
        )

    def with_overrides(
        self,
        *,
        url: Optional[str] = None,
        api_key: Optional[str] = None,
        collection_name: Optional[str] = None,
        recreate_collection: Optional[bool] = None,
    ) -> "QdrantSettings":
        data = self.model_dump()
        if url is not None:
            data["url"] = url
        if api_key is not None:
            data["api_key"] = api_key
        if collection_name is not None:
            data["collection_name"] = collection_name
        if recreate_collection is not None:
            data["recreate_collection"] = recreate_collection
        return QdrantSettings(**data)

    def distance_enum(self) -> models.Distance:
        value = self.distance.strip().lower()
        if value in {"dot", "dotproduct", "dot_product"}:
            return models.Distance.DOT
        if value in {"euclid", "euclidean"}:
            return models.Distance.EUCLID
        if value in {"manhattan", "l1"}:
            return models.Distance.MANHATTAN
        return models.Distance.COSINE

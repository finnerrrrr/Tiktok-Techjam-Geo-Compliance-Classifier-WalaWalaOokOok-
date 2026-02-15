from __future__ import annotations

import uuid
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, List

from fastembed import SparseTextEmbedding, TextEmbedding
from qdrant_client import QdrantClient, models

from offline.chunking import ChildChunk, build_parent_child_chunks, iter_source_files, parse_source
from offline.domain_inference import infer_domain
from offline.qdrant_config import QdrantSettings

DENSE_MODEL_NAME = "BAAI/bge-small-en-v1.5"
SPARSE_MODEL_NAME = "Qdrant/bm25"


@dataclass
class IndexBuildStats:
    files_processed: int
    parent_chunks: int
    child_chunks: int
    domains: list[str]


def _deterministic_point_id(source_path: str, parent_id: str, child_index: int) -> str:
    seed = f"{source_path}:{parent_id}:{child_index}"
    return str(uuid.uuid5(uuid.NAMESPACE_URL, seed))


def _infer_region_hint(text: str) -> str:
    text_lc = text.lower()
    region_map = {
        "eu": ["eu", "europe", "dsa", "gdpr"],
        "us": ["us", "usa", "california", "florida"],
        "sg": ["singapore"],
        "my": ["malaysia"],
        "hk": ["hong kong"],
        "uae": ["uae"],
        "au": ["australia"],
        "in": ["india"],
    }
    for region, hints in region_map.items():
        if any(hint in text_lc for hint in hints):
            return region
    return ""


def _create_qdrant_client(settings: QdrantSettings) -> QdrantClient:
    return QdrantClient(
        url=settings.url,
        api_key=settings.api_key,
        timeout=settings.timeout,
        prefer_grpc=settings.prefer_grpc,
    )


def _ensure_collection(client: QdrantClient, settings: QdrantSettings, vector_size: int) -> None:
    exists = client.collection_exists(settings.collection_name)
    if exists and settings.recreate_collection:
        client.delete_collection(settings.collection_name)
        exists = False

    if not exists:
        client.create_collection(
            collection_name=settings.collection_name,
            vectors_config={
                "dense": models.VectorParams(
                    size=vector_size,
                    distance=settings.distance_enum(),
                )
            },
            sparse_vectors_config={
                "sparse": models.SparseVectorParams()
            },
        )

    for field in ["domain", "law_name", "source_path", "region_hint"]:
        try:
            client.create_payload_index(
                collection_name=settings.collection_name,
                field_name=field,
                field_schema=models.PayloadSchemaType.KEYWORD,
            )
        except Exception:
            # Idempotent safety: ignore if index already exists.
            pass


def _iter_child_chunks(data_root: Path) -> Iterable[ChildChunk]:
    for source_path in iter_source_files(data_root):
        title, body = parse_source(source_path)
        domain = infer_domain(source_path=source_path, title=title, body=body)
        child_chunks = build_parent_child_chunks(
            source_path=source_path,
            law_name=title,
            domain=domain,
            body=body,
        )
        for child in child_chunks:
            yield child


def build_qdrant_index(data_root: Path, settings: QdrantSettings) -> IndexBuildStats:
    if not data_root.exists():
        raise FileNotFoundError(f"Data root not found: {data_root}")

    client = _create_qdrant_client(settings)
    child_chunks = list(_iter_child_chunks(data_root))
    if not child_chunks:
        return IndexBuildStats(files_processed=0, parent_chunks=0, child_chunks=0, domains=[])

    dense_model = TextEmbedding(model_name=DENSE_MODEL_NAME)
    sparse_model = SparseTextEmbedding(model_name=SPARSE_MODEL_NAME)

    child_texts = [chunk.child_text for chunk in child_chunks]
    dense_vectors = list(dense_model.embed(child_texts))
    sparse_vectors = list(sparse_model.embed(child_texts))
    vector_size = len(dense_vectors[0])

    _ensure_collection(client, settings, vector_size)

    points: List[models.PointStruct] = []
    parent_ids: set[str] = set()
    source_files: set[str] = set()
    domains: set[str] = set()

    for chunk, dense_vec, sparse_vec in zip(child_chunks, dense_vectors, sparse_vectors):
        point_id = _deterministic_point_id(chunk.source_path, chunk.parent_id, chunk.child_index)
        source_files.add(chunk.source_path)
        parent_ids.add(f"{chunk.source_path}:{chunk.parent_id}")
        domains.add(chunk.domain)

        payload = {
            "doc_id": Path(chunk.source_path).stem,
            "chunk_id": f"{chunk.parent_id}:c{chunk.child_index}",
            "parent_id": chunk.parent_id,
            "child_index": chunk.child_index,
            "domain": chunk.domain,
            "law_name": chunk.law_name,
            "source_path": chunk.source_path,
            "region_hint": _infer_region_hint(f"{chunk.law_name} {chunk.parent_text} {chunk.child_text}"),
            "parent_text": chunk.parent_text,
            "child_text": chunk.child_text,
        }

        points.append(
            models.PointStruct(
                id=point_id,
                vector={
                    "dense": dense_vec.tolist(),
                    "sparse": models.SparseVector(
                        indices=sparse_vec.indices.tolist(),
                        values=sparse_vec.values.tolist(),
                    ),
                },
                payload=payload,
            )
        )

    batch_size = 128
    for start in range(0, len(points), batch_size):
        client.upsert(
            collection_name=settings.collection_name,
            points=points[start:start + batch_size],
            wait=True,
        )

    return IndexBuildStats(
        files_processed=len(source_files),
        parent_chunks=len(parent_ids),
        child_chunks=len(points),
        domains=sorted(domains),
    )


def ensure_qdrant_index(data_root: Path, settings: QdrantSettings, rebuild: bool = False) -> IndexBuildStats | None:
    client = _create_qdrant_client(settings)
    exists = client.collection_exists(settings.collection_name)

    needs_build = rebuild or settings.recreate_collection or not exists
    if not needs_build:
        count = client.count(collection_name=settings.collection_name, exact=False)
        points_count = int(getattr(count, "count", 0))
        needs_build = points_count == 0

    if not needs_build:
        return None

    return build_qdrant_index(data_root=data_root, settings=settings)

from __future__ import annotations

import argparse
from pathlib import Path

from offline.index_builder import ensure_qdrant_index
from offline.qdrant_config import QdrantSettings
from online.pipeline import run_batch


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Geo compliance classifier (Qdrant hybrid backend)"
    )
    parser.add_argument(
        "--input",
        type=Path,
        default=Path("input_data/sample_features.csv"),
        help="Input CSV path with 2 columns: feature_name, feature_description",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("outputs/classification_output.csv"),
        help="Output CSV path",
    )
    parser.add_argument(
        "--data-root",
        type=Path,
        default=Path("data_sources"),
        help="Root directory containing source .txt compliance docs",
    )
    parser.add_argument(
        "--collection-name",
        type=str,
        default=None,
        help="Optional Qdrant collection name override",
    )
    parser.add_argument(
        "--qdrant-url",
        type=str,
        default=None,
        help="Qdrant endpoint URL override (default from env or http://localhost:6333)",
    )
    parser.add_argument(
        "--qdrant-api-key",
        type=str,
        default=None,
        help="Qdrant API key override",
    )
    parser.add_argument(
        "--rebuild-index",
        action="store_true",
        help="Rebuild and re-upsert offline index into Qdrant",
    )
    return parser.parse_args()


def build_settings(args: argparse.Namespace) -> QdrantSettings:
    base = QdrantSettings.from_env()
    return base.with_overrides(
        url=args.qdrant_url,
        api_key=args.qdrant_api_key,
        collection_name=args.collection_name,
        recreate_collection=args.rebuild_index,
    )


def main() -> None:
    args = parse_args()
    settings = build_settings(args)

    stats = ensure_qdrant_index(
        data_root=args.data_root,
        settings=settings,
        rebuild=args.rebuild_index,
    )
    if stats is not None:
        print(
            "Indexed Qdrant collection",
            f"{settings.collection_name}: files={stats.files_processed} parents={stats.parent_chunks} children={stats.child_chunks} domains={stats.domains}",
        )
    else:
        print(f"Using existing Qdrant collection: {settings.collection_name}")

    results = run_batch(
        input_csv=args.input,
        output_csv=args.output,
        settings=settings,
    )
    print(f"Processed {len(results)} rows")
    print(f"Output written to {args.output}")


if __name__ == "__main__":
    main()

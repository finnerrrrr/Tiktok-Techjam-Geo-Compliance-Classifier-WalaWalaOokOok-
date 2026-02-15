from __future__ import annotations

import csv
import json
from pathlib import Path
from typing import Dict, Iterable, List

from offline.qdrant_config import QdrantSettings
from online.graph.workflow import build_app
from online.schemas import FeatureRecord, WorkflowOutput


def _read_rows(input_csv: Path) -> Iterable[FeatureRecord]:
    with input_csv.open("r", encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        if not reader.fieldnames or len(reader.fieldnames) < 2:
            raise ValueError("Input CSV must contain at least 2 columns: feature name and feature description.")

        for row in reader:
            feature_name = (
                row.get("feature_name")
                or row.get("feature")
                or row.get(reader.fieldnames[0], "")
            )
            feature_description = (
                row.get("feature_description")
                or row.get("description")
                or row.get(reader.fieldnames[1], "")
            )

            record = FeatureRecord(
                feature_name=str(feature_name).strip(),
                feature_description=str(feature_description).strip(),
            )
            yield record


def run_batch(
    input_csv: Path,
    output_csv: Path,
    settings: QdrantSettings | None = None,
) -> List[WorkflowOutput]:
    app = build_app(settings=settings)
    results: List[WorkflowOutput] = []

    for idx, record in enumerate(_read_rows(input_csv), start=1):
        run_state: Dict[str, object] = {
            "feature_name": record.feature_name,
            "feature_description": record.feature_description,
            "audit_trail": [f"start: processing row={idx}"],
        }
        final_state = app.invoke(
            run_state,
            config={"configurable": {"thread_id": f"row-{idx}"}},
        )
        output = WorkflowOutput.model_validate(final_state["output"])
        results.append(output)

    output_csv.parent.mkdir(parents=True, exist_ok=True)
    with output_csv.open("w", encoding="utf-8", newline="") as handle:
        fieldnames = [
            "feature_name",
            "feature_description",
            "needs_geo_compliance",
            "reasoning",
            "citations",
            "confidence",
            "needs_hitl",
            "hitl_reason",
            "audit_trail",
        ]
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for item in results:
            writer.writerow(
                {
                    "feature_name": item.feature_name,
                    "feature_description": item.feature_description,
                    "needs_geo_compliance": item.needs_geo_compliance,
                    "reasoning": item.reasoning,
                    "citations": json.dumps(item.citations, ensure_ascii=True),
                    "confidence": item.confidence,
                    "needs_hitl": item.needs_hitl,
                    "hitl_reason": item.hitl_reason,
                    "audit_trail": json.dumps(item.audit_trail, ensure_ascii=True),
                }
            )

    return results

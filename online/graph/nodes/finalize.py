from __future__ import annotations

from online.graph.state import WorkflowState


def run(state: WorkflowState) -> WorkflowState:
    output = {
        "feature_name": state.get("feature_name", ""),
        "feature_description": state.get("feature_description", ""),
        "needs_geo_compliance": bool(state.get("needs_geo_compliance", False)),
        "reasoning": state.get("reasoning", ""),
        "citations": list(state.get("citations", [])),
        "confidence": float(state.get("classification_confidence", 0.0)),
        "needs_hitl": bool(state.get("needs_hitl", False)),
        "hitl_reason": state.get("hitl_reason", ""),
        "audit_trail": list(state.get("audit_trail", [])),
    }
    return {"output": output}

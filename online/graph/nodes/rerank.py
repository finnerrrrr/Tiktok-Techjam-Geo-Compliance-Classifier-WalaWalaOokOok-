from __future__ import annotations

import re
from typing import Dict, List

from online.graph.state import WorkflowState


_TOKEN_RE = re.compile(r"[A-Za-z0-9_]+")


def _tok(text: str) -> set[str]:
    return {token.lower() for token in _TOKEN_RE.findall(text or "")}


def _clamp(val: float, lo: float = 0.0, hi: float = 1.0) -> float:
    return max(lo, min(hi, val))


def _jaccard(left: str, right: str) -> float:
    a = _tok(left)
    b = _tok(right)
    if not a and not b:
        return 1.0
    return len(a & b) / max(len(a | b), 1)


def _contains_any(text: str, hints: List[str]) -> bool:
    text_lc = (text or "").lower()
    return any(hint.lower() in text_lc for hint in hints if hint)


def run(state: WorkflowState) -> WorkflowState:
    retrieved = list(state.get("retrieved_evidence", []))
    if not retrieved:
        audit = list(state.get("audit_trail", []))
        audit.append("rerank: no evidence to rerank")
        return {"reranked_evidence": [], "audit_trail": audit}

    candidate_domains = {d.lower() for d in state.get("candidate_domains", [])}
    candidate_laws = [law.lower() for law in state.get("candidate_laws", [])]
    region_hints = [region.lower() for region in state.get("region_hints", [])]

    scored: List[Dict[str, object]] = []
    for item in retrieved:
        text = str(item.get("text", ""))
        law_name = str(item.get("law_name", "")).lower()
        domain = str(item.get("domain", "")).lower()

        retrieval_component = _clamp(float(item.get("base_score", 0.0)))
        law_match_component = 1.0 if any(law and (law in law_name or law in text.lower()) for law in candidate_laws) else 0.0
        region_component = 1.0 if _contains_any(text, region_hints) else 0.0
        domain_component = 1.0 if domain in candidate_domains else 0.0

        rerank_score = round(
            0.55 * retrieval_component
            + 0.25 * law_match_component
            + 0.10 * region_component
            + 0.10 * domain_component,
            4,
        )

        enriched = dict(item)
        enriched["rerank_score"] = rerank_score
        scored.append(enriched)

    scored.sort(key=lambda entry: float(entry.get("rerank_score", 0.0)), reverse=True)

    domain_best: Dict[str, Dict[str, object]] = {}
    for item in scored:
        domain = str(item.get("domain", "")).lower()
        if domain and domain not in domain_best:
            domain_best[domain] = item

    selected: List[Dict[str, object]] = list(domain_best.values())
    selected_ids = {str(item.get("chunk_id", "")) for item in selected}

    for item in scored:
        if len(selected) >= 8:
            break
        chunk_id = str(item.get("chunk_id", ""))
        if chunk_id in selected_ids:
            continue
        if any(_jaccard(str(item.get("text", "")), str(existing.get("text", ""))) > 0.85 for existing in selected):
            continue
        selected.append(item)
        selected_ids.add(chunk_id)

    selected.sort(key=lambda entry: float(entry.get("rerank_score", 0.0)), reverse=True)
    selected = selected[:8]

    audit = list(state.get("audit_trail", []))
    top_ids = [str(item.get("chunk_id", "")) for item in selected[:3]]
    audit.append(f"rerank: kept={len(selected)} top={top_ids}")

    return {
        "reranked_evidence": selected,
        "audit_trail": audit,
    }

from __future__ import annotations

import os
import re
from typing import Any, Dict, List

from pydantic import BaseModel, Field

from online.graph.state import WorkflowState

try:
    from langchain_openai import ChatOpenAI
except Exception:  # pragma: no cover
    ChatOpenAI = None


DOMAIN_RULES = {
    "data_privacy": ["data", "privacy", "consent", "tracking", "personal", "retention", "gdpr", "pdpa", "delete"],
    "youth_safety": ["minor", "child", "children", "teen", "age", "guardian", "parental", "under-18"],
    "consumer_protection": ["deceptive", "dark pattern", "subscription", "refund", "consumer", "ads", "transparency"],
}

LAW_HINTS = {
    "gdpr": "EU General Data Protection Regulation (GDPR)",
    "dsa": "EU Digital Services Act (DSA)",
    "pdpa": "Personal Data Protection Act (PDPA)",
    "juvenile": "Juvenile protection statutes",
    "wadeema": "UAE Wadeema Law",
    "sb976": "California SB 976",
    "hb3": "Florida HB 3",
}

REGION_HINTS = [
    "eu",
    "europe",
    "uk",
    "singapore",
    "malaysia",
    "india",
    "uae",
    "florida",
    "california",
    "australia",
    "hong kong",
    "us",
    "usa",
]


class QueryEnhancementOutput(BaseModel):
    expanded_query: str = Field(default="")
    candidate_domains: List[str] = Field(default_factory=list)
    candidate_laws: List[str] = Field(default_factory=list)
    region_hints: List[str] = Field(default_factory=list)
    routing_confidence: float = Field(default=0.0)


_TOKEN_RE = re.compile(r"[A-Za-z0-9_\-]+")


def _normalize_domain(domain: str) -> str:
    return domain.strip().lower().replace(" ", "_")


def _clamp(val: float, lo: float = 0.0, hi: float = 1.0) -> float:
    return max(lo, min(hi, val))


def _unique(items: List[str]) -> List[str]:
    seen: set[str] = set()
    out: List[str] = []
    for item in items:
        key = item.strip().lower()
        if key and key not in seen:
            seen.add(key)
            out.append(item.strip())
    return out


def _rule_enhance(feature_name: str, feature_description: str, known_domains: List[str]) -> Dict[str, Any]:
    query = f"{feature_name}. {feature_description}".strip()
    query_lc = query.lower()
    tokens = {token.lower() for token in _TOKEN_RE.findall(query_lc)}

    candidate_domains: List[str] = []
    matched_keywords = 0
    total_signals = 0

    for domain, keywords in DOMAIN_RULES.items():
        domain_hits = sum(1 for keyword in keywords if keyword in query_lc or keyword in tokens)
        total_signals += len(keywords)
        matched_keywords += domain_hits
        if domain_hits > 0:
            candidate_domains.append(domain)

    candidate_laws = [law_name for key, law_name in LAW_HINTS.items() if key in query_lc or key in tokens]
    regions = [region for region in REGION_HINTS if region in query_lc]

    if not candidate_domains:
        candidate_domains = list(known_domains)

    routing_conf = _clamp(matched_keywords / max(total_signals, 1) * 3.0)
    if candidate_laws:
        routing_conf = _clamp(routing_conf + 0.15)
    if regions:
        routing_conf = _clamp(routing_conf + 0.10)

    expanded_query = query
    if candidate_laws or regions:
        parts = [query]
        if regions:
            parts.append("Regions: " + ", ".join(_unique(regions)))
        if candidate_laws:
            parts.append("Potential laws: " + ", ".join(_unique(candidate_laws)))
        expanded_query = " | ".join(parts)

    return {
        "expanded_query": expanded_query,
        "candidate_domains": _unique([_normalize_domain(item) for item in candidate_domains if _normalize_domain(item) in known_domains]),
        "candidate_laws": _unique(candidate_laws),
        "region_hints": _unique(regions),
        "routing_confidence": routing_conf,
    }


def _llm_enhance(feature_name: str, feature_description: str, known_domains: List[str]) -> QueryEnhancementOutput | None:
    if ChatOpenAI is None or not os.environ.get("OPENAI_API_KEY"):
        return None

    try:
        llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
        structured = llm.with_structured_output(QueryEnhancementOutput)
        prompt = (
            "You are a compliance query enhancer and domain router. "
            "Given a feature name and description, return ONLY structured output with: "
            "expanded_query, candidate_domains, candidate_laws, region_hints, routing_confidence. "
            f"Allowed domains: {known_domains}. Use only these domain values. "
            "routing_confidence must be between 0 and 1."
            f"\n\nFeature name: {feature_name}"
            f"\nFeature description: {feature_description}"
        )
        response = structured.invoke(prompt)

        domains = [
            _normalize_domain(d)
            for d in response.candidate_domains
            if _normalize_domain(d) in known_domains
        ]
        return QueryEnhancementOutput(
            expanded_query=response.expanded_query.strip(),
            candidate_domains=_unique(domains),
            candidate_laws=_unique(response.candidate_laws),
            region_hints=_unique(response.region_hints),
            routing_confidence=_clamp(float(response.routing_confidence)),
        )
    except Exception:
        return None


def make_node(known_domains: List[str]):
    known = sorted({_normalize_domain(domain) for domain in known_domains})

    def run(state: WorkflowState) -> WorkflowState:
        feature_name = state.get("feature_name", "").strip()
        feature_description = state.get("feature_description", "").strip()

        rule_data = _rule_enhance(feature_name, feature_description, known)
        used_llm = False

        final_data = dict(rule_data)
        if rule_data["routing_confidence"] < 0.30:
            llm_data = _llm_enhance(feature_name, feature_description, known)
            if llm_data:
                used_llm = True
                final_data["expanded_query"] = llm_data.expanded_query or final_data["expanded_query"]
                final_data["candidate_domains"] = llm_data.candidate_domains or final_data["candidate_domains"]
                final_data["candidate_laws"] = _unique(final_data["candidate_laws"] + llm_data.candidate_laws)
                final_data["region_hints"] = _unique(final_data["region_hints"] + llm_data.region_hints)
                final_data["routing_confidence"] = max(final_data["routing_confidence"], llm_data.routing_confidence)

        if not final_data["candidate_domains"]:
            final_data["candidate_domains"] = known

        audit = list(state.get("audit_trail", []))
        audit.append(
            "query_enhance_route: "
            f"domains={final_data['candidate_domains']} laws={len(final_data['candidate_laws'])} "
            f"regions={final_data['region_hints']} confidence={round(final_data['routing_confidence'], 3)} "
            f"llm_used={used_llm}"
        )

        return {
            "expanded_query": final_data["expanded_query"],
            "candidate_domains": final_data["candidate_domains"],
            "candidate_laws": final_data["candidate_laws"],
            "region_hints": final_data["region_hints"],
            "routing_confidence": float(final_data["routing_confidence"]),
            "audit_trail": audit,
        }

    return run

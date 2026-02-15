from __future__ import annotations

from typing import Callable, Dict, List

from online.graph.state import WorkflowState


def make_node(search_fn: Callable[..., list], known_domains: List[str], top_k_per_domain: int = 5, max_candidates: int = 24):
    known_lower = [domain.lower() for domain in known_domains]

    def run(state: WorkflowState) -> WorkflowState:
        query = state.get("expanded_query", "")
        domains = [d.lower() for d in state.get("candidate_domains", []) if d]
        search_domains = domains or known_lower

        collected: Dict[str, dict] = {}

        for domain in search_domains:
            hits = search_fn(query=query, allowed_domains=[domain], top_k=top_k_per_domain)
            for hit in hits:
                if hit.chunk_id not in collected:
                    collected[hit.chunk_id] = {
                        "chunk_id": hit.chunk_id,
                        "domain": hit.domain,
                        "law_name": hit.law_name,
                        "source_path": hit.source_path,
                        "text": hit.text,
                        "base_score": hit.score,
                        "parent_id": getattr(hit, "parent_id", ""),
                        "parent_snippet": getattr(hit, "parent_snippet", ""),
                    }

        used_fallback = False
        if not collected:
            used_fallback = True
            for hit in search_fn(query=query, allowed_domains=known_lower, top_k=max_candidates):
                if hit.chunk_id not in collected:
                    collected[hit.chunk_id] = {
                        "chunk_id": hit.chunk_id,
                        "domain": hit.domain,
                        "law_name": hit.law_name,
                        "source_path": hit.source_path,
                        "text": hit.text,
                        "base_score": hit.score,
                        "parent_id": getattr(hit, "parent_id", ""),
                        "parent_snippet": getattr(hit, "parent_snippet", ""),
                    }

        evidence = sorted(collected.values(), key=lambda item: float(item.get("base_score", 0.0)), reverse=True)[:max_candidates]

        audit = list(state.get("audit_trail", []))
        audit.append(
            f"retrieve: domains={search_domains} retrieved={len(evidence)} fallback={used_fallback}"
        )

        return {
            "retrieved_evidence": evidence,
            "audit_trail": audit,
        }

    return run


# GeoLogicClassifer123

![Alt text](assets/agent_workflow.png)


# From Guesswork to Governance — High-Level Agent Overview

## Pipeline (at a glance)
Query Prep → Domain Agents → Reranker → Verifier → (HITL if needed) → Aggregator → Classifier → Output & Audit

---

## 1) Query Prep Agent
**What:** Normalize feature artifacts and extract key signals.  
**Task:** Clean text, resolve codenames/jargon, detect intent & geo, add synonyms/triggers, emit an enriched query.

## 2) Domain Agents (xN)
**What:** Per-domain retrieval (e.g., youth safety, reporting/CSAM, EU DSA).  
**Task:** Pull top candidate law chunks with citations and jurisdiction tags using hybrid lexical+semantic search.

## 3) Reranker Agent
**What:** Precision pass over the candidates.  
**Task:** Re-rank with a cross-encoder and apply diversity (MMR) to select a small, high-signal, non-redundant set.

## 4) Verifier Agent
**What:** Turn “relevant text” into grounded evidence.  
**Task:** Check geo/citation alignment, score evidence quality, decide **verified** vs **low confidence**, and surface supporting/conflicting snippets.

## 5) HITL (Human-in-the-Loop)
**What:** Fast human review for edge cases.  
**Task:** Present top evidence and suggested label; capture overrides/rationales when confidence is low or geo/citation is unclear.

## 6) Aggregator Agent
**What:** Build the final context bundle.  
**Task:** Deduplicate citations, balance facets (regs/jurisdictions), and assemble a compact context + audit metadata for classification.

## 7) Classifier Agent
**What:** Produce the final triage label with traceability.  
**Task:** Output **YES/NO/UNCERTAIN** with a short reason, referenced regulations, and citation IDs; include a self-confidence score.

## 8) Outputs & Audit Trail
**What:** Submission artifacts and compliance evidence.  
**Task:** Write CSV/JSONL containing the decision, reasoning, citations, sentence indices, scores, thresholds, and any HITL overrides.

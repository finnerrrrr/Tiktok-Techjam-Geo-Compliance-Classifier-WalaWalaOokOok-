# agents/classifier_agent.py
# -*- coding: utf-8 -*-
"""
ClassifierAgent — LLM-backed classifier for geo-compliance flags.

What it does
------------
Takes the aggregated retrieval bundle (from your AggregatorAgent) plus the original
prepped query, asks an LLM to decide whether the feature needs geo-specific
compliance logic, and returns a normalized decision with reasoning.

Inputs
------
classify(aggregated, query)

- aggregated: dict (from AggregatorAgent), e.g.
    {
      "chunks": [
        # RAG-style chunks (from your new rag.py):
        {"law_name": "EU DSA", "chunk": "...", "relevance_score": 8.7, "domain": "content_moderation"},
        # or older pipeline chunks:
        {"content": "...", "citation": "GDPR Art. 6", "relevance_score": 8.7, "domain_tag": "Data Protection"}
      ],
      "summary": "...",              # optional
      "audit_trail": ["..."],        # optional list of steps
      "hitl_override": {             # optional human override
          "flag": "yes|no|uncertain",
          "rationale": "..."
      }
    }

- query: string OR dict (your prepped query). If dict, it will be stringified for the LLM.

Outputs
-------
dict:
{
  "flag": "yes" | "no" | "uncertain",     # normalized (lower-case)
  "reasoning": str,                        # short explanation
  "regulations": List[str],                # unique citations/law names from chunks
  "audit_trail": List[str]                 # includes classifier step (and HITL note if applied)
}

Notes
-----
- Uses OpenAI Chat Completions API via `requests`. Set env var: OPENAI_API_KEY
- Few-shot examples are included for stability.
- Robust to both new RAG chunk schema and older schema.
"""

from __future__ import annotations

import json
import os
import platform
from typing import Any, Dict, List, Union

try:
    import requests  # type: ignore
except Exception:
    requests = None  # gracefully handled below


def _normalize_flag(raw: Any) -> str:
    """Normalize various flag spellings/emojis to 'yes' | 'no' | 'uncertain'."""
    if not isinstance(raw, str):
        return ""
    v = raw.strip().lower()
    if v in {"yes", "y", "✅"}:
        return "yes"
    if v in {"no", "n", "❌"}:
        return "no"
    if v in {"uncertain", "unsure", "?", "❓"}:
        return "uncertain"
    # uppercase variants support
    if v in {"yes/yes", "yes/no"}:  # harmless guard if model returns odd tokens
        return "yes"
    if v in {"no/no"}:
        return "no"
    if v in {"yes/no/uncertain"}:
        return "uncertain"
    return ""


class ClassifierAgent:
    def __init__(
        self,
        model: str = "gpt-4o",
        temperature: float = 0.3,
        max_tokens: int = 500,
    ) -> None:
        self.model = model
        self.temperature = temperature
        self.max_tokens = max_tokens

        # Few-shot examples (normalized to lower-case flags)
        self.labelled_samples: List[Dict[str, Any]] = [
            {
                "feature": "To comply with the Utah Social Media Regulation Act, we are implementing a curfew-based login restriction for users under 18. The system uses ASL to detect minor accounts and routes enforcement through GH to apply only within Utah boundaries.",
                "flag": "yes",
                "reasoning": "Explicit statutory reference + geo targeting.",
                "regulations": ["Utah Social Media Regulation Act"],
            },
            {
                "feature": "A/B test dark theme accessibility for users in South Korea. Rollout limited via GH and monitored with FR flags.",
                "flag": "no",
                "reasoning": "Business-driven geofence without legal mandate.",
                "regulations": [],
            },
            {
                "feature": "DSA visibility lock for flagged UGC (NSP), EU-only enforcement via GH, traceability via EchoTrace.",
                "flag": "yes",
                "reasoning": "Explicit DSA reference and geo enforcement.",
                "regulations": ["EU Digital Services Act (DSA)"],
            },
            {
                "feature": "General safety filters for minors using ASL and CDS; no region mentioned.",
                "flag": "uncertain",
                "reasoning": "No explicit geo/legal citation; requires review.",
                "regulations": [],
            },
        ]

    # ---------------------------
    # Public API
    # ---------------------------
    async def classify(self, aggregated: Dict[str, Any], query: Union[str, Dict[str, Any]]) -> Dict[str, Any]:
        """
        Run LLM classification. Returns a dict with normalized 'flag', 'reasoning',
        'regulations', and an updated 'audit_trail'.
        """
        chunks: List[Dict[str, Any]] = list(aggregated.get("chunks", []))
        audit_trail: List[str] = list(aggregated.get("audit_trail", []))
        hitl = aggregated.get("hitl_override")

        # Extract regulations from either 'citation' (old pipeline) or 'law_name' (new rag.py)
        regs: List[str] = []
        for c in chunks:
            cite = c.get("citation")
            if cite and cite != "No Citation":
                regs.append(str(cite))
            else:
                law = c.get("law_name")
                if law:
                    regs.append(str(law))
        regulations = sorted({r for r in regs if r})

        # Combine chunk text from 'content' (old) or 'chunk' (new)
        content_combined = " ".join(c.get("content") or c.get("chunk") or "" for c in chunks).strip()

        # Convert query dict to stable text if needed
        query_text = json.dumps(query, ensure_ascii=False) if isinstance(query, dict) else str(query)

        # Few-shot examples string
        few_shot = "\n\n".join(
            f"Feature: {s['feature']}\nFlag: {s['flag']}\nReasoning: {s['reasoning']}\nRegulations: {', '.join(s['regulations'])}"
            for s in self.labelled_samples
        )

        prompt = f"""
You are a compliance classifier. Decide if the feature requires geo-specific compliance logic.

Respond with JSON only. The "flag" MUST be one of: "yes", "no", or "uncertain".
Explain briefly in "reasoning" (1–4 sentences). Consider regulations provided.

Few-shot examples:
{few_shot}

Query:
{query_text}

Aggregated feature description from retrieved chunks:
{content_combined}

Regulations (from citations/law names):
{', '.join(regulations) if regulations else 'None'}

Return JSON exactly:
{{
  "flag": "yes|no|uncertain",
  "reasoning": "..."
}}
""".strip()

        llm_content = await self._llm_call(prompt)
        flag, reasoning = self._parse_llm_json(llm_content)

        # Apply HITL override if present
        if isinstance(hitl, dict):
            override_flag = _normalize_flag(hitl.get("flag"))
            override_rationale = hitl.get("rationale")
            if override_flag:
                flag = override_flag
            if override_rationale:
                reasoning = f"{override_rationale} (HITL override)"
            audit_trail.append("HITL override applied in classifier.")

        result = {
            "flag": flag,                 # "yes" | "no" | "uncertain"
            "reasoning": reasoning,
            "regulations": regulations,   # unique list derived from chunks
            "audit_trail": audit_trail + ["LLM classification complete"],
        }
        return result

    # ---------------------------
    # Internals
    # ---------------------------
    async def _llm_call(self, prompt: str) -> str:
        """Call OpenAI Chat Completions; fallback to 'uncertain' on failure."""
        api_key = os.environ.get("OPENAI_API_KEY")
        if not api_key:
            return json.dumps({"flag": "uncertain", "reasoning": "Missing OPENAI_API_KEY; cannot call LLM."})

        headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
        payload = {
            "model": self.model,
            "messages": [{"role": "user", "content": prompt}],
            "temperature": self.temperature,
            "max_tokens": self.max_tokens,
        }

        # Pyodide path
        if platform.system() == "Emscripten":
            try:
                from pyodide.http import pyfetch  # type: ignore
                resp = await pyfetch(
                    "https://api.openai.com/v1/chat/completions", method="POST", headers=headers, body=json.dumps(payload)
                )
                data = await resp.json()
                return data["choices"][0]["message"]["content"]
            except Exception as e:  # pragma: no cover
                return json.dumps({"flag": "uncertain", "reasoning": f"OpenAI API call failed in Pyodide: {e}"})

        # Standard Python
        if requests is None:
            return json.dumps({"flag": "uncertain", "reasoning": "Requests not available; cannot call OpenAI API."})

        try:
            resp = requests.post("https://api.openai.com/v1/chat/completions", json=payload, headers=headers, timeout=60)
            resp.raise_for_status()
            data = resp.json()
            return data["choices"][0]["message"]["content"]
        except Exception as e:  # pragma: no cover
            return json.dumps({"flag": "uncertain", "reasoning": f"OpenAI API call failed: {e}"})

    def _parse_llm_json(self, content: str) -> (str, str):
        """
        Parse the LLM response JSON and normalize the flag.
        If parsing fails, return ('uncertain', <error_message>).
        """
        try:
            data = json.loads(content)
            flag = _normalize_flag(data.get("flag"))
            reasoning = (data.get("reasoning") or "").strip() or "No reasoning provided."
            if not flag:
                flag = "uncertain"
            return flag, reasoning
        except Exception:
            return "uncertain", f"Failed to parse LLM response as JSON: {content}"

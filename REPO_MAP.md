├── .DS_Store
├── .gitignore
├── README.md
├── REPO_MAP.md
├── __pycache__
    ├── config.cpython-310.pyc
    └── config.cpython-311.pyc
├── agents
    ├── __pycache__
    │   ├── aggregator_agent.cpython-311.pyc
    │   ├── classifier_agent.cpython-311.pyc
    │   ├── hitl_agent.cpython-311.pyc
    │   ├── reranker_agent.cpython-311.pyc
    │   ├── verifier_agent.cpython-311.pyc
    │   ├── youth_safety_agent.cpython-311.pyc
    │   └── youth_safety_agent.cpython-313.pyc
    ├── aggregator_agent.py
    ├── classifier_agent.py
    ├── consumer_protection_agent.py
    ├── data_privacy_agent.py
    ├── hitl_agent.py
    ├── reranker_agent.py
    ├── verifier_agent.py
    └── youth_safety_agent.py
├── assets
    ├── agent_workflow.png
    └── techjam_archi-1.png
├── config.py
├── kb
    ├── consumer_protection
    │   └── EU_DSA_A25.txt
    ├── data_privacy
    │   ├── EU_GDPR_A5.txt
    │   ├── HK_PDPC_Part5.txt
    │   ├── HK_PDPC_Part6.txt
    │   ├── MY_PDPA_DIV1.txt
    │   ├── MY_PDPA_DIV3.txt
    │   ├── SG_PDPA.txt
    │   └── uae_pdpl_2021.txt
    └── youth_safety
    │   ├── AU_CWSA_2024
    │   ├── CA_SB976.txt
    │   ├── EU_DSA_A28.txt
    │   ├── FL_HB3.txt
    │   ├── INDIA_Juvenile_2015.txt
    │   └── uae_wadeema_2024.txt
├── main.py
├── requirements.txt
└── utils
    ├── __pycache__
        ├── inputqueryenhancer.cpython-311.pyc
        ├── rag.cpython-311.pyc
        ├── rag.cpython-313.pyc
        └── semanticchunker.cpython-311.pyc
    ├── inputqueryenhancer.py
    ├── rag.py
    └── semanticchunker.py


/.DS_Store:
--------------------------------------------------------------------------------
https://raw.githubusercontent.com/finnerrrrr/Tiktok-Techjam-Geo-Compliance-Classifier-WalaWalaOokOok-/124c2ba0a405c212bed7646e88ff39925ca85feb/.DS_Store


--------------------------------------------------------------------------------
/.gitignore:
--------------------------------------------------------------------------------
 1 | # venvs
 2 | .venv/
 3 | .venv*/
 4 | venv/
 5 | env/
 6 | 
 7 | # python cache
 8 | __pycache__/
 9 | *.py[cod]
10 | *.egg-info/
11 | 
12 | # OS junk
13 | .DS_Store
14 | 
15 | # big artifacts (safeties)
16 | *.dylib
17 | *.so


--------------------------------------------------------------------------------
/README.md:
--------------------------------------------------------------------------------
 1 | # Geo Compliance Classifier
 2 | 
 3 | ## Problem Statement
 4 | Automated pipeline that classifies new product features for compliance with global regulations. Given a feature title and description, the system retrieves relevant legal texts, verifies jurisdictional alignment, and outputs a triage label (Yes/No/Uncertain) along with an audit trail.
 5 | 
 6 | ## Features and Functionality
 7 | - **Agent pipeline:** query preparation, domain retrieval, reranking, verification, optional human-in-the-loop review, aggregation and classification.
 8 | - **Jurisdiction-aware retrieval:** domain agents search a curated knowledge base of regional regulations.
 9 | - **Transparent outputs:** final decisions include reasoning, cited regulations and an audit trail.
10 | - **Demo:** run `python main.py` for a local example.
11 | 
12 | ## Development Tools
13 | - Python 3.x
14 | - Git & VS Code
15 | 
16 | ## APIs
17 | - OpenAI API for language models and embeddings
18 | - Hugging Face models for reranking
19 | 
20 | ## Libraries
21 | - LangChain & LangChain Community
22 | - ChromaDB
23 | - NLTK
24 | - NumPy
25 | - Pydantic
26 | - Rank-BM25
27 | - Requests
28 | - Python Dotenv
29 | 
30 | ## Assets
31 | - `assets/atechjam_archi-1.png` – high level agent workflow diagram
32 | 
33 | ## Datasets
34 | - Regulatory text snippets under `kb/` (e.g., GDPR, EU DSA, PDPA, youth safety laws)
35 | 
36 | ## Repository
37 | This project is open sourced at: [Geo Compliance Classifier Repository](https://github.com/your-team/Tiktok-Techjam-Geo-Compliance-Classifier-WalaWalaOokOok-)
38 | 
39 | ### Local Demo Setup
40 | 1. Clone the repository
41 |    ```bash
42 |    git clone https://github.com/your-team/Tiktok-Techjam-Geo-Compliance-Classifier-WalaWalaOokOok-.git
43 |    cd Tiktok-Techjam-Geo-Compliance-Classifier-WalaWalaOokOok-
44 |    ```
45 | 2. Install dependencies
46 |    ```bash
47 |    pip install -r requirements.txt
48 |    ```
49 | 3. Provide an `OPENAI_API_KEY` in your environment
50 | 4. Run the demo
51 |    ```bash
52 |    python main.py
53 |    ```
54 | 


--------------------------------------------------------------------------------
/__pycache__/config.cpython-310.pyc:
--------------------------------------------------------------------------------
https://raw.githubusercontent.com/finnerrrrr/Tiktok-Techjam-Geo-Compliance-Classifier-WalaWalaOokOok-/124c2ba0a405c212bed7646e88ff39925ca85feb/__pycache__/config.cpython-310.pyc


--------------------------------------------------------------------------------
/__pycache__/config.cpython-311.pyc:
--------------------------------------------------------------------------------
https://raw.githubusercontent.com/finnerrrrr/Tiktok-Techjam-Geo-Compliance-Classifier-WalaWalaOokOok-/124c2ba0a405c212bed7646e88ff39925ca85feb/__pycache__/config.cpython-311.pyc


--------------------------------------------------------------------------------
/agents/__pycache__/aggregator_agent.cpython-311.pyc:
--------------------------------------------------------------------------------
https://raw.githubusercontent.com/finnerrrrr/Tiktok-Techjam-Geo-Compliance-Classifier-WalaWalaOokOok-/124c2ba0a405c212bed7646e88ff39925ca85feb/agents/__pycache__/aggregator_agent.cpython-311.pyc


--------------------------------------------------------------------------------
/agents/__pycache__/classifier_agent.cpython-311.pyc:
--------------------------------------------------------------------------------
https://raw.githubusercontent.com/finnerrrrr/Tiktok-Techjam-Geo-Compliance-Classifier-WalaWalaOokOok-/124c2ba0a405c212bed7646e88ff39925ca85feb/agents/__pycache__/classifier_agent.cpython-311.pyc


--------------------------------------------------------------------------------
/agents/__pycache__/hitl_agent.cpython-311.pyc:
--------------------------------------------------------------------------------
https://raw.githubusercontent.com/finnerrrrr/Tiktok-Techjam-Geo-Compliance-Classifier-WalaWalaOokOok-/124c2ba0a405c212bed7646e88ff39925ca85feb/agents/__pycache__/hitl_agent.cpython-311.pyc


--------------------------------------------------------------------------------
/agents/__pycache__/reranker_agent.cpython-311.pyc:
--------------------------------------------------------------------------------
https://raw.githubusercontent.com/finnerrrrr/Tiktok-Techjam-Geo-Compliance-Classifier-WalaWalaOokOok-/124c2ba0a405c212bed7646e88ff39925ca85feb/agents/__pycache__/reranker_agent.cpython-311.pyc


--------------------------------------------------------------------------------
/agents/__pycache__/verifier_agent.cpython-311.pyc:
--------------------------------------------------------------------------------
https://raw.githubusercontent.com/finnerrrrr/Tiktok-Techjam-Geo-Compliance-Classifier-WalaWalaOokOok-/124c2ba0a405c212bed7646e88ff39925ca85feb/agents/__pycache__/verifier_agent.cpython-311.pyc


--------------------------------------------------------------------------------
/agents/__pycache__/youth_safety_agent.cpython-311.pyc:
--------------------------------------------------------------------------------
https://raw.githubusercontent.com/finnerrrrr/Tiktok-Techjam-Geo-Compliance-Classifier-WalaWalaOokOok-/124c2ba0a405c212bed7646e88ff39925ca85feb/agents/__pycache__/youth_safety_agent.cpython-311.pyc


--------------------------------------------------------------------------------
/agents/__pycache__/youth_safety_agent.cpython-313.pyc:
--------------------------------------------------------------------------------
https://raw.githubusercontent.com/finnerrrrr/Tiktok-Techjam-Geo-Compliance-Classifier-WalaWalaOokOok-/124c2ba0a405c212bed7646e88ff39925ca85feb/agents/__pycache__/youth_safety_agent.cpython-313.pyc


--------------------------------------------------------------------------------
/agents/aggregator_agent.py:
--------------------------------------------------------------------------------
 1 | class AggregatorAgent:
 2 |     def __init__(self):
 3 |         pass
 4 | 
 5 |     def process(self, chunks, hitl_feedback=None):
 6 |         """Aggregate chunks into a cohesive context bundle, incorporate HITL feedback"""
 7 |         aggregated = {
 8 |             'chunks': chunks,
 9 |             'summary': ' '.join([chunk['content'][:50] for chunk in chunks]),
10 |             'audit_trail': []
11 |         }
12 |         if hitl_feedback:
13 |             aggregated['hitl_override'] = {
14 |                 'flag': hitl_feedback.get('override_flag'),
15 |                 'rationale': hitl_feedback.get('override_rationale')
16 |             }
17 |             aggregated['chunks'] = hitl_feedback.get('updated_chunks', chunks)
18 |             aggregated['audit_trail'].append("HITL Override Applied")
19 | 
20 |         return aggregated
21 | 


--------------------------------------------------------------------------------
/agents/classifier_agent.py:
--------------------------------------------------------------------------------
  1 | # agents/classifier_agent.py
  2 | # -*- coding: utf-8 -*-
  3 | """
  4 | ClassifierAgent — LLM-backed classifier for geo-compliance flags.
  5 | 
  6 | What it does
  7 | ------------
  8 | Takes the aggregated retrieval bundle (from your AggregatorAgent) plus the original
  9 | prepped query, asks an LLM to decide whether the feature needs geo-specific
 10 | compliance logic, and returns a normalized decision with reasoning.
 11 | 
 12 | Inputs
 13 | ------
 14 | classify(aggregated, query)
 15 | 
 16 | - aggregated: dict (from AggregatorAgent), e.g.
 17 |     {
 18 |       "chunks": [
 19 |         # RAG-style chunks (from your new rag.py):
 20 |         {"law_name": "EU DSA", "chunk": "...", "relevance_score": 8.7, "domain": "content_moderation"},
 21 |         # or older pipeline chunks:
 22 |         {"content": "...", "citation": "GDPR Art. 6", "relevance_score": 8.7, "domain_tag": "Data Protection"}
 23 |       ],
 24 |       "summary": "...",              # optional
 25 |       "audit_trail": ["..."],        # optional list of steps
 26 |       "hitl_override": {             # optional human override
 27 |           "flag": "yes|no|uncertain",
 28 |           "rationale": "..."
 29 |       }
 30 |     }
 31 | 
 32 | - query: string OR dict (your prepped query). If dict, it will be stringified for the LLM.
 33 | 
 34 | Outputs
 35 | -------
 36 | dict:
 37 | {
 38 |   "flag": "yes" | "no" | "uncertain",     # normalized (lower-case)
 39 |   "reasoning": str,                        # short explanation
 40 |   "regulations": List[str],                # unique citations/law names from chunks
 41 |   "audit_trail": List[str]                 # includes classifier step (and HITL note if applied)
 42 | }
 43 | 
 44 | Notes
 45 | -----
 46 | - Uses OpenAI Chat Completions API via `requests`. Set env var: OPENAI_API_KEY
 47 | - Few-shot examples are included for stability.
 48 | - Robust to both new RAG chunk schema and older schema.
 49 | """
 50 | 
 51 | from __future__ import annotations
 52 | 
 53 | import json
 54 | import os
 55 | import platform
 56 | from typing import Any, Dict, List, Union
 57 | 
 58 | try:
 59 |     import requests  # type: ignore
 60 | except Exception:
 61 |     requests = None  # gracefully handled below
 62 | 
 63 | 
 64 | def _normalize_flag(raw: Any) -> str:
 65 |     """Normalize various flag spellings/emojis to 'yes' | 'no' | 'uncertain'."""
 66 |     if not isinstance(raw, str):
 67 |         return ""
 68 |     v = raw.strip().lower()
 69 |     if v in {"yes", "y", "✅"}:
 70 |         return "yes"
 71 |     if v in {"no", "n", "❌"}:
 72 |         return "no"
 73 |     if v in {"uncertain", "unsure", "?", "❓"}:
 74 |         return "uncertain"
 75 |     # uppercase variants support
 76 |     if v in {"yes/yes", "yes/no"}:  # harmless guard if model returns odd tokens
 77 |         return "yes"
 78 |     if v in {"no/no"}:
 79 |         return "no"
 80 |     if v in {"yes/no/uncertain"}:
 81 |         return "uncertain"
 82 |     return ""
 83 | 
 84 | 
 85 | class ClassifierAgent:
 86 |     def __init__(
 87 |         self,
 88 |         model: str = "gpt-4o",
 89 |         temperature: float = 0.3,
 90 |         max_tokens: int = 500,
 91 |     ) -> None:
 92 |         self.model = model
 93 |         self.temperature = temperature
 94 |         self.max_tokens = max_tokens
 95 | 
 96 |         # Few-shot examples (normalized to lower-case flags)
 97 |         self.labelled_samples: List[Dict[str, Any]] = [
 98 |             {
 99 |                 "feature": "To comply with the Utah Social Media Regulation Act, we are implementing a curfew-based login restriction for users under 18. The system uses ASL to detect minor accounts and routes enforcement through GH to apply only within Utah boundaries.",
100 |                 "flag": "yes",
101 |                 "reasoning": "Explicit statutory reference + geo targeting.",
102 |                 "regulations": ["Utah Social Media Regulation Act"],
103 |             },
104 |             {
105 |                 "feature": "A/B test dark theme accessibility for users in South Korea. Rollout limited via GH and monitored with FR flags.",
106 |                 "flag": "no",
107 |                 "reasoning": "Business-driven geofence without legal mandate.",
108 |                 "regulations": [],
109 |             },
110 |             {
111 |                 "feature": "DSA visibility lock for flagged UGC (NSP), EU-only enforcement via GH, traceability via EchoTrace.",
112 |                 "flag": "yes",
113 |                 "reasoning": "Explicit DSA reference and geo enforcement.",
114 |                 "regulations": ["EU Digital Services Act (DSA)"],
115 |             },
116 |             {
117 |                 "feature": "General safety filters for minors using ASL and CDS; no region mentioned.",
118 |                 "flag": "uncertain",
119 |                 "reasoning": "No explicit geo/legal citation; requires review.",
120 |                 "regulations": [],
121 |             },
122 |         ]
123 | 
124 |     # ---------------------------
125 |     # Public API
126 |     # ---------------------------
127 |     async def classify(self, aggregated: Dict[str, Any], query: Union[str, Dict[str, Any]]) -> Dict[str, Any]:
128 |         """
129 |         Run LLM classification. Returns a dict with normalized 'flag', 'reasoning',
130 |         'regulations', and an updated 'audit_trail'.
131 |         """
132 |         chunks: List[Dict[str, Any]] = list(aggregated.get("chunks", []))
133 |         audit_trail: List[str] = list(aggregated.get("audit_trail", []))
134 |         hitl = aggregated.get("hitl_override")
135 | 
136 |         # Extract regulations from either 'citation' (old pipeline) or 'law_name' (new rag.py)
137 |         regs: List[str] = []
138 |         for c in chunks:
139 |             cite = c.get("citation")
140 |             if cite and cite != "No Citation":
141 |                 regs.append(str(cite))
142 |             else:
143 |                 law = c.get("law_name")
144 |                 if law:
145 |                     regs.append(str(law))
146 |         regulations = sorted({r for r in regs if r})
147 | 
148 |         # Combine chunk text from 'content' (old) or 'chunk' (new)
149 |         content_combined = " ".join(c.get("content") or c.get("chunk") or "" for c in chunks).strip()
150 | 
151 |         # Convert query dict to stable text if needed
152 |         query_text = json.dumps(query, ensure_ascii=False) if isinstance(query, dict) else str(query)
153 | 
154 |         # Few-shot examples string
155 |         few_shot = "\n\n".join(
156 |             f"Feature: {s['feature']}\nFlag: {s['flag']}\nReasoning: {s['reasoning']}\nRegulations: {', '.join(s['regulations'])}"
157 |             for s in self.labelled_samples
158 |         )
159 | 
160 |         prompt = f"""
161 | You are a compliance classifier. Decide if the feature requires geo-specific compliance logic.
162 | 
163 | Respond with JSON only. The "flag" MUST be one of: "yes", "no", or "uncertain".
164 | Explain briefly in "reasoning" (1–4 sentences). Consider regulations provided.
165 | 
166 | Few-shot examples:
167 | {few_shot}
168 | 
169 | Query:
170 | {query_text}
171 | 
172 | Aggregated feature description from retrieved chunks:
173 | {content_combined}
174 | 
175 | Regulations (from citations/law names):
176 | {', '.join(regulations) if regulations else 'None'}
177 | 
178 | Return JSON exactly:
179 | {{
180 |   "flag": "yes|no|uncertain",
181 |   "reasoning": "..."
182 | }}
183 | """.strip()
184 | 
185 |         llm_content = await self._llm_call(prompt)
186 |         flag, reasoning = self._parse_llm_json(llm_content)
187 | 
188 |         # Apply HITL override if present
189 |         if isinstance(hitl, dict):
190 |             override_flag = _normalize_flag(hitl.get("flag"))
191 |             override_rationale = hitl.get("rationale")
192 |             if override_flag:
193 |                 flag = override_flag
194 |             if override_rationale:
195 |                 reasoning = f"{override_rationale} (HITL override)"
196 |             audit_trail.append("HITL override applied in classifier.")
197 | 
198 |         result = {
199 |             "flag": flag,                 # "yes" | "no" | "uncertain"
200 |             "reasoning": reasoning,
201 |             "regulations": regulations,   # unique list derived from chunks
202 |             "audit_trail": audit_trail + ["LLM classification complete"],
203 |         }
204 |         return result
205 | 
206 |     # ---------------------------
207 |     # Internals
208 |     # ---------------------------
209 |     async def _llm_call(self, prompt: str) -> str:
210 |         """Call OpenAI Chat Completions; fallback to 'uncertain' on failure."""
211 |         api_key = os.environ.get("OPENAI_API_KEY")
212 |         if not api_key:
213 |             return json.dumps({"flag": "uncertain", "reasoning": "Missing OPENAI_API_KEY; cannot call LLM."})
214 | 
215 |         headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
216 |         payload = {
217 |             "model": self.model,
218 |             "messages": [{"role": "user", "content": prompt}],
219 |             "temperature": self.temperature,
220 |             "max_tokens": self.max_tokens,
221 |         }
222 | 
223 |         # Pyodide path
224 |         if platform.system() == "Emscripten":
225 |             try:
226 |                 from pyodide.http import pyfetch  # type: ignore
227 |                 resp = await pyfetch(
228 |                     "https://api.openai.com/v1/chat/completions", method="POST", headers=headers, body=json.dumps(payload)
229 |                 )
230 |                 data = await resp.json()
231 |                 return data["choices"][0]["message"]["content"]
232 |             except Exception as e:  # pragma: no cover
233 |                 return json.dumps({"flag": "uncertain", "reasoning": f"OpenAI API call failed in Pyodide: {e}"})
234 | 
235 |         # Standard Python
236 |         if requests is None:
237 |             return json.dumps({"flag": "uncertain", "reasoning": "Requests not available; cannot call OpenAI API."})
238 | 
239 |         try:
240 |             resp = requests.post("https://api.openai.com/v1/chat/completions", json=payload, headers=headers, timeout=60)
241 |             resp.raise_for_status()
242 |             data = resp.json()
243 |             return data["choices"][0]["message"]["content"]
244 |         except Exception as e:  # pragma: no cover
245 |             return json.dumps({"flag": "uncertain", "reasoning": f"OpenAI API call failed: {e}"})
246 | 
247 |     def _parse_llm_json(self, content: str) -> (str, str):
248 |         """
249 |         Parse the LLM response JSON and normalize the flag.
250 |         If parsing fails, return ('uncertain', <error_message>).
251 |         """
252 |         try:
253 |             data = json.loads(content)
254 |             flag = _normalize_flag(data.get("flag"))
255 |             reasoning = (data.get("reasoning") or "").strip() or "No reasoning provided."
256 |             if not flag:
257 |                 flag = "uncertain"
258 |             return flag, reasoning
259 |         except Exception:
260 |             return "uncertain", f"Failed to parse LLM response as JSON: {content}"
261 | 


--------------------------------------------------------------------------------
/agents/consumer_protection_agent.py:
--------------------------------------------------------------------------------
 1 | # agents/youth_safety_agent.py
 2 | # -*- coding: utf-8 -*-
 3 | """
 4 | Simple YouthSafetyAgent
 5 | 
 6 | - Points RAG to the Youth Safety corpus directory (default: "kb/youth_safety").
 7 | - Accepts a *prepped query* (string or dict) from the Query Prep agent.
 8 | - Calls RAG to run a fixed-weight hybrid search and returns the top-k chunks.
 9 | 
10 | Each returned item has:
11 | {
12 |   "law_name": str,
13 |   "chunk": str,
14 |   "relevance_score": float,  # 0..10
15 |   "domain": str              # e.g., "youth_safety"
16 | }
17 | """
18 | 
19 | from typing import Any, Dict, List, Union
20 | from utils.rag import RAGEngine
21 | 
22 | 
23 | class ConsumerProtectionAgent:
24 |     def __init__(
25 |         self,
26 |         domain_dir: str = "kb/consumer_protection",
27 |         model_name: str = "sentence-transformers/all-MiniLM-L6-v2",
28 |         top_k: int = 5,
29 |     ) -> None:
30 |         self.name = "Consumer Protection Agent"
31 |         self.top_k = top_k
32 |         # Build the domain-specific RAG engine once (chunks, embeddings, BM25)
33 |         self._engine = RAGEngine.from_domain_dir(domain_dir, model_name=model_name)
34 | 
35 |     def analyze_feature(self, prepped_query: Union[str, Dict[str, Any]]) -> List[Dict[str, Any]]:
36 |         """
37 |         Pass the prepped query straight to RAG and return the top-k results.
38 |         """
39 |         return self._engine.search(prepped_query, top_k=self.top_k)
40 | 


--------------------------------------------------------------------------------
/agents/data_privacy_agent.py:
--------------------------------------------------------------------------------
 1 | # agents/youth_safety_agent.py
 2 | # -*- coding: utf-8 -*-
 3 | """
 4 | Simple YouthSafetyAgent
 5 | 
 6 | - Points RAG to the Youth Safety corpus directory (default: "kb/youth_safety").
 7 | - Accepts a *prepped query* (string or dict) from the Query Prep agent.
 8 | - Calls RAG to run a fixed-weight hybrid search and returns the top-k chunks.
 9 | 
10 | Each returned item has:
11 | {
12 |   "law_name": str,
13 |   "chunk": str,
14 |   "relevance_score": float,  # 0..10
15 |   "domain": str              # e.g., "youth_safety"
16 | }
17 | """
18 | 
19 | from typing import Any, Dict, List, Union
20 | from utils.rag import RAGEngine
21 | 
22 | 
23 | class DataPrivacyAgent:
24 |     def __init__(
25 |         self,
26 |         domain_dir: str = "kb/data_privacy",
27 |         model_name: str = "sentence-transformers/all-MiniLM-L6-v2",
28 |         top_k: int = 5,
29 |     ) -> None:
30 |         self.name = "Data Privacy Agent"
31 |         self.top_k = top_k
32 |         # Build the domain-specific RAG engine once (chunks, embeddings, BM25)
33 |         self._engine = RAGEngine.from_domain_dir(domain_dir, model_name=model_name)
34 | 
35 |     def analyze_feature(self, prepped_query: Union[str, Dict[str, Any]]) -> List[Dict[str, Any]]:
36 |         """
37 |         Pass the prepped query straight to RAG and return the top-k results.
38 |         """
39 |         return self._engine.search(prepped_query, top_k=self.top_k)
40 | 


--------------------------------------------------------------------------------
/agents/hitl_agent.py:
--------------------------------------------------------------------------------
 1 | class HITLAgent:
 2 |     def __init__(self):
 3 |         pass
 4 | 
 5 |     def process(self, verification_result, query):
 6 |         """Handle human-in-the-loop interaction with basic validation."""
 7 |         # --- basic structure checks (minimal) ---
 8 |         if not isinstance(verification_result, dict):
 9 |             raise ValueError("verification_result must be a dict.")
10 |         for key in ("chunks", "confidence", "detailed_scores"):
11 |             if key not in verification_result:
12 |                 raise ValueError(f"verification_result missing required key: '{key}'")
13 | 
14 |         chunks = verification_result["chunks"]
15 |         print("\n--- HITL Review Required ---")
16 |         print(f"Query: {query}")
17 |         print("Current Chunks:")
18 |         for i, chunk in enumerate(chunks, 1):
19 |             # tolerate missing keys in chunk dicts
20 |             content = (chunk.get("content") or "")[:100]
21 |             citation = chunk.get("citation", "N/A")
22 |             domain = chunk.get("domain_tag", "N/A")
23 |             print(f"Chunk {i}: {content}... (Citation: {citation}, Domain: {domain})")
24 |         print(f"Confidence: {verification_result['confidence']:.2f}")
25 |         print("Detailed Scores:", verification_result["detailed_scores"])
26 | 
27 |         # --- override yes/no ---
28 |         override = input("\nDo you want to override? (yes/no): ").strip().lower()
29 |         if override not in {"yes", "no"}:
30 |             raise ValueError("Override must be 'yes' or 'no'.")
31 | 
32 |         if override == "yes":
33 |             print("Enter corrections:")
34 | 
35 |             # --- label normalization & validation ---
36 |             new_flag_raw = input("New label (yes/no/uncertain): ").strip().lower()  # normalize just in case
37 |             if new_flag_raw in {"y", "yes"}:
38 |                 new_flag = "yes"
39 |             elif new_flag_raw in {"n", "no"}:
40 |                 new_flag = "no"
41 |             elif new_flag_raw in {"u", "unsure", "uncertain", "?"}:
42 |                 new_flag = "uncertain"
43 |             else:
44 |                 raise ValueError("New label must be 'yes', 'no', or 'uncertain'.")
45 | 
46 |             # --- rationale required ---
47 |             new_rationale = input("New rationale: ").strip()
48 |             if not new_rationale:
49 |                 raise ValueError("Rationale cannot be blank.")
50 | 
51 |             # --- modify chunks? ---
52 |             modify_chunks = input("Modify chunks? (yes/no): ").strip().lower()
53 |             if modify_chunks not in {"yes", "no"}:
54 |                 raise ValueError("Modify chunks must be 'yes' or 'no'.")
55 | 
56 |             if modify_chunks == "yes":
57 |                 # minimal field presence checks
58 |                 new_content = input("New chunk content: ").strip()
59 |                 if not new_content:
60 |                     raise ValueError("New chunk content cannot be blank.")
61 | 
62 |                 new_citation = input("New citation: ").strip()
63 |                 if not new_citation:
64 |                     raise ValueError("New citation cannot be blank.")
65 | 
66 |                 new_domain = input("New domain tag: ").strip()
67 |                 if not new_domain:
68 |                     raise ValueError("New domain tag cannot be blank.")
69 | 
70 |                 new_chunk = {
71 |                     "content": new_content,
72 |                     "citation": new_citation,
73 |                     "domain_tag": new_domain,
74 |                     "relevance_score": 10.0,  # keep your existing default
75 |                 }
76 |                 chunks.append(new_chunk)
77 | 
78 |             feedback = {
79 |                 "override_flag": new_flag,            # 'yes' | 'no' | 'uncertain'
80 |                 "override_rationale": new_rationale,
81 |                 "updated_chunks": chunks,
82 |             }
83 |         else:
84 |             feedback = None
85 | 
86 |         return feedback
87 | 


--------------------------------------------------------------------------------
/agents/reranker_agent.py:
--------------------------------------------------------------------------------
  1 | import asyncio
  2 | import requests
  3 | import numpy as np
  4 | 
  5 | class RerankerAgent:
  6 |     def __init__(self, top_n=5, mmr_lambda=0.7):
  7 |         self.top_n = top_n
  8 |         self.mmr_lambda = mmr_lambda
  9 | 
 10 |     async def load_cross_encoder(self, model_url):
 11 |         """Load cross-encoder model with proper error handling"""
 12 |         try:
 13 |             response = requests.get(model_url)
 14 |             model_data = response.json()
 15 | 
 16 |             class CrossEncoder:
 17 |                 def __init__(self):
 18 |                     self.initialized = True
 19 | 
 20 |                 def predict(self, sentence_pairs, **kwargs):
 21 |                     scores = []
 22 |                     for query, chunk_content in sentence_pairs:
 23 |                         query_terms = set(query.lower().split())
 24 |                         content_terms = set(chunk_content.lower().split())
 25 |                         overlap = len(query_terms & content_terms)
 26 |                         jaccard_sim = overlap / len(query_terms | content_terms) if query_terms or content_terms else 0
 27 |                         citation_boost = 0.2 if "citation" in chunk_content.lower() else 0
 28 |                         score = jaccard_sim * 10 + citation_boost
 29 |                         scores.append(score)
 30 |                     return np.array(scores)
 31 | 
 32 |             return CrossEncoder()
 33 | 
 34 |         except Exception as e:
 35 |             print(f"Error loading cross-encoder: {e}")
 36 |             return None
 37 | 
 38 |     async def rerank_chunks(self, cross_encoder, chunks, query):
 39 |         """Rerank chunks using cross-encoder scores combined with original relevance"""
 40 |         if not chunks:
 41 |             return []
 42 | 
 43 |         sentence_pairs = [[query, chunk["content"]] for chunk in chunks]
 44 |         if cross_encoder:
 45 |             cross_scores = cross_encoder.predict(sentence_pairs)
 46 |         else:
 47 |             cross_scores = [chunk.get("relevance_score", 5) for chunk in chunks]
 48 | 
 49 |         combined_scores = []
 50 |         for i, chunk in enumerate(chunks):
 51 |             orig_score = chunk.get("relevance_score", 5)
 52 |             cross_score = cross_scores[i] if i < len(cross_scores) else 0
 53 |             combined = 0.6 * cross_score + 0.4 * orig_score
 54 |             combined_scores.append((chunk, combined))
 55 | 
 56 |         combined_scores.sort(key=lambda x: x[1], reverse=True)
 57 |         return [chunk for chunk, _ in combined_scores]
 58 | 
 59 |     def apply_mmr(self, chunks, query):
 60 |         """Apply Maximal Marginal Relevance for diversity"""
 61 |         if not chunks:
 62 |             return []
 63 | 
 64 |         selected = []
 65 |         remaining = chunks.copy()
 66 | 
 67 |         while len(selected) < self.top_n and remaining:
 68 |             scores = []
 69 |             for doc in remaining:
 70 |                 query_terms = set(query.lower().split())
 71 |                 doc_terms = set(doc["content"].lower().split())
 72 |                 sim_to_query = len(query_terms & doc_terms) / max(len(query_terms), 1)
 73 |                 if selected:
 74 |                     sim_to_selected = max([
 75 |                         len(set(doc["content"].lower().split()) &
 76 |                             set(s["content"].lower().split())) /
 77 |                         max(len(doc["content"].split()), 1)
 78 |                         for s in selected
 79 |                     ])
 80 |                 else:
 81 |                     sim_to_selected = 0
 82 |                 mmr_score = self.mmr_lambda * sim_to_query - (1 - self.mmr_lambda) * sim_to_selected
 83 |                 scores.append((doc, mmr_score))
 84 | 
 85 |             best_doc = max(scores, key=lambda x: x[1])[0]
 86 |             selected.append(best_doc)
 87 |             remaining.remove(best_doc)
 88 | 
 89 |         return selected
 90 | 
 91 |     def balance_facets(self, chunks):
 92 |         """Balance representation across different domains/facets"""
 93 |         if not chunks:
 94 |             return []
 95 | 
 96 |         facets = defaultdict(list)
 97 |         for chunk in chunks:
 98 |             domain = chunk.get("domain_tag", "Unknown")
 99 |             facets[domain].append(chunk)
100 | 
101 |         balanced = []
102 |         domains = list(facets.keys())
103 |         while len(balanced) < self.top_n and any(facets.values()):
104 |             for domain in domains:
105 |                 if facets[domain] and len(balanced) < self.top_n:
106 |                     balanced.append(facets[domain].pop(0))
107 | 
108 |         return balanced
109 | 
110 |     async def process(self, chunks, query, model_url=None):
111 |         """Main processing pipeline: rerank → MMR → facet balancing"""
112 |         cross_encoder = await self.load_cross_encoder(model_url or
113 |                                                      "https://cdn.jsdelivr.net/npm/cross-encoder/ms-marco-MiniLM-L-6-v2/model.json")
114 |         reranked = await self.rerank_chunks(cross_encoder, chunks, query)
115 |         diverse = self.apply_mmr(reranked, query)
116 |         final_selection = self.balance_facets(diverse)
117 |         return final_selection
118 | 


--------------------------------------------------------------------------------
/agents/verifier_agent.py:
--------------------------------------------------------------------------------
 1 | import numpy as np
 2 | 
 3 | class VerifierAgent:
 4 |     def __init__(self, threshold=7.0, weights=None):
 5 |         self.threshold = threshold
 6 |         self.weights = weights or {
 7 |             'relevance': 0.4,
 8 |             'consistency': 0.3,
 9 |             'citation_quality': 0.2,
10 |             'diversity': 0.1
11 |         }
12 | 
13 |     def compute_relevance(self, chunks, query):
14 |         """Compute relevance score (0-10)"""
15 |         if not chunks:
16 |             return 0.0
17 |         query_terms = set(query.lower().split())
18 |         avg_overlap = np.mean([
19 |             len(query_terms & set(chunk['content'].lower().split())) / max(len(query_terms), 1)
20 |             for chunk in chunks
21 |         ])
22 |         return avg_overlap * 10
23 | 
24 |     def compute_consistency(self, chunks):
25 |         """Compute consistency score (0-10)"""
26 |         if len(chunks) < 2:
27 |             return 10.0
28 |         consistencies = []
29 |         for i in range(len(chunks)):
30 |             for j in range(i+1, len(chunks)):
31 |                 set1 = set(chunks[i]['content'].lower().split())
32 |                 set2 = set(chunks[j]['content'].lower().split())
33 |                 overlap = len(set1 & set2) / len(set1 | set2) if set1 or set2 else 0
34 |                 consistencies.append(overlap)
35 |         return np.mean(consistencies) * 10 if consistencies else 10.0
36 | 
37 |     def compute_citation_quality(self, chunks):
38 |         """Compute citation quality score (0-10)"""
39 |         if not chunks:
40 |             return 0.0
41 |         valid_citations = sum(1 for chunk in chunks if chunk.get('citation') and chunk['citation'] != 'No Citation')
42 |         return (valid_citations / len(chunks)) * 10
43 | 
44 |     def compute_diversity(self, chunks):
45 |         """Compute diversity score (0-10)"""
46 |         if not chunks:
47 |             return 0.0
48 |         unique_domains = len(set(chunk.get('domain_tag', 'Unknown') for chunk in chunks))
49 |         return min(unique_domains / (len(chunks) / 2.0), 1.0) * 10
50 | 
51 |     def compute_confidence(self, chunks, query):
52 |         """Compute overall confidence score"""
53 |         scores = {
54 |             'relevance': self.compute_relevance(chunks, query),
55 |             'consistency': self.compute_consistency(chunks),
56 |             'citation_quality': self.compute_citation_quality(chunks),
57 |             'diversity': self.compute_diversity(chunks)
58 |         }
59 |         confidence = sum(scores[component] * weight for component, weight in self.weights.items())
60 |         return confidence, scores
61 | 
62 |     def process(self, chunks, query):
63 |         """Process chunks and return confidence, detailed scores, and escalation flag"""
64 |         confidence, detailed_scores = self.compute_confidence(chunks, query)
65 |         escalate = confidence < self.threshold
66 |         return {
67 |             'confidence': confidence,
68 |             'detailed_scores': detailed_scores,
69 |             'escalate': escalate,
70 |             'chunks': chunks
71 |         }
72 | 


--------------------------------------------------------------------------------
/agents/youth_safety_agent.py:
--------------------------------------------------------------------------------
 1 | # agents/youth_safety_agent.py
 2 | # -*- coding: utf-8 -*-
 3 | """
 4 | Simple YouthSafetyAgent
 5 | 
 6 | - Points RAG to the Youth Safety corpus directory (default: "kb/youth_safety").
 7 | - Accepts a *prepped query* (string or dict) from the Query Prep agent.
 8 | - Calls RAG to run a fixed-weight hybrid search and returns the top-k chunks.
 9 | 
10 | Each returned item has:
11 | {
12 |   "law_name": str,
13 |   "chunk": str,
14 |   "relevance_score": float,  # 0..10
15 |   "domain": str              # e.g., "youth_safety"
16 | }
17 | """
18 | 
19 | from typing import Any, Dict, List, Union
20 | from utils.rag import RAGEngine
21 | 
22 | 
23 | class YouthSafetyAgent:
24 |     def __init__(
25 |         self,
26 |         domain_dir: str = "kb/youth_safety",
27 |         model_name: str = "sentence-transformers/all-MiniLM-L6-v2",
28 |         top_k: int = 5,
29 |     ) -> None:
30 |         self.name = "Youth Safety Agent"
31 |         self.top_k = top_k
32 |         # Build the domain-specific RAG engine once (chunks, embeddings, BM25)
33 |         self._engine = RAGEngine.from_domain_dir(domain_dir, model_name=model_name)
34 | 
35 |     def analyze_feature(self, prepped_query: Union[str, Dict[str, Any]]) -> List[Dict[str, Any]]:
36 |         """
37 |         Pass the prepped query straight to RAG and return the top-k results.
38 |         """
39 |         return self._engine.search(prepped_query, top_k=self.top_k)
40 | 


--------------------------------------------------------------------------------
/assets/agent_workflow.png:
--------------------------------------------------------------------------------
https://raw.githubusercontent.com/finnerrrrr/Tiktok-Techjam-Geo-Compliance-Classifier-WalaWalaOokOok-/124c2ba0a405c212bed7646e88ff39925ca85feb/assets/agent_workflow.png


--------------------------------------------------------------------------------
/assets/techjam_archi-1.png:
--------------------------------------------------------------------------------
https://raw.githubusercontent.com/finnerrrrr/Tiktok-Techjam-Geo-Compliance-Classifier-WalaWalaOokOok-/124c2ba0a405c212bed7646e88ff39925ca85feb/assets/techjam_archi-1.png


--------------------------------------------------------------------------------
/config.py:
--------------------------------------------------------------------------------
 1 | hf_token = None
 2 | 
 3 | def set_token(token):
 4 |     global hf_token
 5 |     hf_token = token
 6 | 
 7 | def get_token():
 8 |     global hf_token
 9 |     return hf_token
10 | 


--------------------------------------------------------------------------------
/kb/consumer_protection/EU_DSA_A25.txt:
--------------------------------------------------------------------------------
 1 | EU Digital Services Act Article 25 2022/()/()/
 2 | 
 3 | 
 4 | Article 25, Online interface design and organisation - the Digital Services Act (DSA)
 5 | 
 6 | 
 7 | 1. Providers of online platforms shall not design, organise or operate their online interfaces in a way that deceives or manipulates the recipients of their service or in a way that otherwise materially distorts or impairs the ability of the recipients of their service to make free and informed decisions.
 8 | 
 9 | 
10 | 2. The prohibition in paragraph 1 shall not apply to practices covered by Directive 2005/29/EC or Regulation (EU) 2016/679.
11 | 
12 | 
13 | 3. The Commission may issue guidelines on how paragraph 1 applies to specific practices, notably:
14 | 
15 | 
16 | (a) giving more prominence to certain choices when asking the recipient of the service for a decision;
17 | 
18 | 
19 | (b) repeatedly requesting that the recipient of the service make a choice where that choice has already been made, especially by presenting pop-ups that interfere with the user experience;
20 | 
21 | 
22 | (c) making the procedure for terminating a service more difficult than subscribing to it.


--------------------------------------------------------------------------------
/kb/data_privacy/EU_GDPR_A5.txt:
--------------------------------------------------------------------------------
 1 | EU General Data Protection Regulation Article 5 2018/()/()/
 2 | 
 3 | 
 4 | Art. 5 GDPRPrinciples relating to processing of personal data
 5 | Personal data shall be:
 6 | processed lawfully, fairly and in a transparent manner in relation to the data subject (‘lawfulness, fairness and transparency’);
 7 | collected for specified, explicit and legitimate purposes and not further processed in a manner that is incompatible with those purposes; further processing for archiving purposes in the public interest, scientific or historical research purposes or statistical purposes shall, in accordance with Article 89(1), not be considered to be incompatible with the initial purposes (‘purpose limitation’);
 8 | adequate, relevant and limited to what is necessary in relation to the purposes for which they are processed (‘data minimisation’);
 9 | accurate and, where necessary, kept up to date; every reasonable step must be taken to ensure that personal data that are inaccurate, having regard to the purposes for which they are processed, are erased or rectified without delay (‘accuracy’);
10 | kept in a form which permits identification of data subjects for no longer than is necessary for the purposes for which the personal data are processed; personal data may be stored for longer periods insofar as the personal data will be processed solely for archiving purposes in the public interest, scientific or historical research purposes or statistical purposes in accordance with Article 89(1) subject to implementation of the appropriate technical and organisational measures required by this Regulation in order to safeguard the rights and freedoms of the data subject (‘storage limitation’);
11 | processed in a manner that ensures appropriate security of the personal data, including protection against unauthorised or unlawful processing and against accidental loss, destruction or damage, using appropriate technical or organisational measures (‘integrity and confidentiality’).
12 | The controller shall be responsible for, and be able to demonstrate compliance with, paragraph 1 (‘accountability’).


--------------------------------------------------------------------------------
/kb/data_privacy/HK_PDPC_Part5.txt:
--------------------------------------------------------------------------------
 1 | Personal Data (Privacy) Ordinance 2021/()/()/
 2 | Place: Hong Kong
 3 | Effective Date: 2021-12-01
 4 | 
 5 | Part 5
 6 | Access to and Correction of Personal Data
 7 | 
 8 | Division 1 - Access to Personal Data
 9 | (Added 18 of 2012 s. 10)
10 | 
11 | 17A. Interpretation of Part 5
12 | Without limiting the definition of relevant person in section 2(1), in this Part—
13 |   relevant person (有關人士), in relation to an individual, also includes a person authorized in writing by the individual to make, on behalf of the individual—
14 |     (a) a data access request; or
15 |     (b) a data correction request.
16 | (Added 18 of 2012 s. 10. Amended E.R. 1 of 2013)
17 | 
18 | 18. Data Access Request
19 | (1) An individual, or a relevant person on behalf of an individual, may make a request—
20 |     (a) to be informed by a data user whether the data user holds personal data of which the individual is the data subject;
21 |     (b) if the data user holds such data, to be supplied by the data user with a copy of such data.
22 | (2) A data access request under both paragraphs of subsection (1) shall be treated as being a single request, and the provisions of this Ordinance shall be construed accordingly.
23 | (3) A data access request under paragraph (a) of subsection (1) may, in the absence of evidence to the contrary, be treated as being a data access request under both paragraphs of that subsection, and the provisions of this Ordinance (including subsection (2)) shall be construed accordingly.
24 | (4) A data user who, in relation to personal data—(a) does not hold the data; but (b) controls the use of the data in such a way as to prohibit the data user who does hold the data from complying (whether in whole or in part) with a data access request which relates to the data, shall be deemed to hold the data, and the provisions of this Ordinance (including this section) shall be construed accordingly. (Amended 18 of 2012 s. 11)
25 | (5) A person commits an offence if the person, in a data access request, supplies any information which is false or misleading in a material particular for the purposes of having the data user—(a) inform the person whether the data user holds any personal data which is the subject of the request; and (b) if applicable, supply a copy of the data. (Added 18 of 2012 s. 11)
26 | (6) A person who commits an offence under subsection (5) is liable on conviction to a fine at level 3 and to imprisonment for 6 months. (Added 18 of 2012 s. 11)
27 | 
28 | 19. Compliance with Data Access Request
29 | (1) Subject to subsection (2) and sections 20 and 28(5), a data user must comply with a data access request within 40 days after receiving the request by—(a) if the data user holds any personal data which is the subject of the request—(i) informing the requestor in writing that the data user holds the data; and (ii) supplying a copy of the data; or (b) if the data user does not hold any personal data which is the subject of the request, informing the requestor in writing that the data user does not hold the data. (Replaced 18 of 2012 s. 12)
30 | (1A) Despite subsection (1)(b), if—(a) a data access request is made to the Hong Kong Police Force as to whether it holds any record of criminal conviction of an individual; and (b) it does not hold such record, it must comply with the request by informing the requestor orally, within 40 days after receiving the request, that it does not hold such record. (Added 18 of 2012 s. 12)
31 | (2) A data user who is unable to comply with a data access request within the period specified in subsection (1) or (1A) shall—(a) before the expiration of that period—(i) by notice in writing inform the requestor that the data user is so unable and of the reasons why the data user is so unable; and (ii) comply with the request to the extent, if
32 | 


--------------------------------------------------------------------------------
/kb/data_privacy/HK_PDPC_Part6.txt:
--------------------------------------------------------------------------------
  1 | Cap. 486 Personal Data (Privacy) Ordinance 2021/()/()/
  2 | Place: Hong Kong
  3 | Effective Date: 2021-12-01
  4 | 
  5 | Part 6
  6 | 
  7 | Matching Procedures and Transfers of Personal Data, etc.
  8 | 30.Matching procedure not to be carried out except with consent of data subject, etc.
  9 | (1)A data user shall not carry out, whether in whole or in part, a matching procedure—
 10 | (a)unless and until each individual who is a data subject of the personal data the subject of that procedure has given his prescribed consent to the procedure being carried out;
 11 | (b)unless and until the Commissioner has consented under section 32 to the procedure being carried out;
 12 | (c)unless the procedure—
 13 | (i)belongs to a class of matching procedures specified in a notice under subsection (2); and
 14 | (ii)is carried out in accordance with the conditions, if any, specified in the notice; or
 15 | (d)unless it is required or permitted under any provision of any Ordinance specified in Schedule 4.
 16 | (2)For the purposes of this section, the Commissioner may, by notice in the Gazette, specify—
 17 | (a)a class of matching procedures;
 18 | (b)subject to subsection (3), the conditions, if any, subject to which a matching procedure belonging to that class shall be carried out.
 19 | (3)The Commissioner shall, before specifying any conditions in a notice under subsection (2), consult with—
 20 | (a)such bodies representative of data users to which the conditions will apply (whether in whole or in part); and
 21 | (b)such other interested persons,
 22 | as he thinks fit.
 23 | (4)It is hereby declared that a notice under subsection (2) is subsidiary legislation.
 24 | (5)Subject to subsection (6), a data user shall not take adverse action against an individual in consequence (whether in whole or in part) of the carrying out of a matching procedure—
 25 | (a)unless the data user has served a notice in writing on the individual—
 26 | (i)specifying the adverse action it proposes to take and the reasons therefor; and
 27 | (ii)stating that the individual has 7 days after the receipt of the notice within which to show cause why that action should not be taken; and
 28 | (b)until the expiration of those 7 days.
 29 | (6)Subsection (5) shall not operate to prevent a data user from taking adverse action against an individual if compliance with the requirements of that subsection would prejudice any investigation into the commission of an offence or the possible commission of an offence.
 30 | 31.Matching procedure request
 31 | (1)A data user proposing to carry out, whether in whole or in part, a matching procedure may make a request—
 32 | (a)in the specified form;
 33 | (b)to the Commissioner; and
 34 | (c)seeking the Commissioner’s consent under section 32 to the carrying out of that procedure.
 35 | (2)Where 2 or more data users may each make a matching procedure request in respect of the same matching procedure, then any of those data users may make such a request on behalf of all those data users, and the provisions of this Ordinance (including subsection (1)) shall be construed accordingly.
 36 | (3)Without prejudice to the generality of subsection (2), it is hereby declared that a matching procedure request may be made in relation to 2 or more matching procedures, or a series of matching procedures, and the other provisions of this Ordinance (including section 32) shall be construed accordingly.
 37 | (4)A data user who, in a matching procedure request made under subsection (1), supplies any information which is false or misleading in a material particular for the purpose of obtaining the Commissioner’s consent to the carrying out of the matching procedure to which the request relates, commits an offence and is liable on conviction to a fine at level 3 and to imprisonment for 6 months. (Added 18 of 2012 s. 18)
 38 | 32.Determination of matching procedure request
 39 | (1)The Commissioner shall determine a matching procedure request—
 40 | (a)not later than 45 days after receiving the request; and
 41 | (b)by taking into account the prescribed matters applicable to the request and—
 42 | (i)where he is satisfied as to those matters, serving a notice in writing on the requestor stating that he consents to the carrying out of the matching procedure to which the request relates subject to the conditions, if any, specified in the notice;
 43 | (ii)where he is not so satisfied, serving a notice in writing on the requestor stating—
 44 | (A)that he refuses to consent to the carrying out of the matching procedure to which the request relates; and
 45 | (B)such of those matters in respect of which he is not so satisfied and the reasons why he is not so satisfied.
 46 | (2)For the avoidance of doubt, it is hereby declared that a consent in a notice under subsection (1)(b)(i) to the carrying out of a matching procedure to which a matching procedure request relates shall not operate to prevent a data user who is neither the requestor nor, where section 31(2) applies to the request, any data user on whose behalf such request was made, from carrying out, whether in whole or in part, the procedure.
 47 | (3)An appeal may be made to the Administrative Appeals Board—
 48 | (a)against—
 49 | (i)any conditions specified in a notice under subsection (1)(b)(i); or
 50 | (ii)any refusal specified in a notice under subsection (1)(b)(ii); and
 51 | (b)by the requestor on whom the notice was served or any data user on whose behalf the matching procedure request concerned was made.
 52 | (4)In this section, prescribed matter (訂明事宜) means a matter specified in Schedule 5.
 53 | (5)A requestor who contravenes any conditions specified in a notice under subsection (1)(b)(i) commits an offence and is liable on conviction to a fine at level 3. (Added 18 of 2012 s. 19)
 54 | 33.Prohibition against transfer of personal data to place outside Hong Kong except in specified circumstances
 55 | (Not yet in operation)
 56 | (1)This section shall not apply to personal data other than personal data the collection, holding, processing or use of which—
 57 | (a)takes place in Hong Kong; or
 58 | (b)is controlled by a data user whose principal place of business is in Hong Kong.
 59 | (2)A data user shall not transfer personal data to a place outside Hong Kong unless—
 60 | (a)the place is specified for the purposes of this section in a notice under subsection (3);
 61 | (b)the user has reasonable grounds for believing that there is in force in that place any law which is substantially similar to, or serves the same purposes as, this Ordinance;
 62 | (c)the data subject has consented in writing to the transfer;
 63 | (d)the user has reasonable grounds for believing that, in all the circumstances of the case—
 64 | (i)the transfer is for the avoidance or mitigation of adverse action against the data subject;
 65 | (ii)it is not practicable to obtain the consent in writing of the data subject to that transfer; and
 66 | (iii)if it was practicable to obtain such consent, the data subject would give it;
 67 | (e)the data is exempt from data protection principle 3 by virtue of an exemption under Part 8; or (Amended 18 of 2012 s. 2)
 68 | (f)the user has taken all reasonable precautions and exercised all due diligence to ensure that the data will not, in that place, be collected, held, processed or used in any manner which, if that place were Hong Kong, would be a contravention of a requirement under this Ordinance.
 69 | (3)Where the Commissioner has reasonable grounds for believing that there is in force in a place outside Hong Kong any law which is substantially similar to, or serves the same purposes as, this Ordinance, he may, by notice in the Gazette, specify that place for the purposes of this section.
 70 | (4)Where the Commissioner has reasonable grounds for believing that in a place specified in a notice under subsection (3) there is no longer in force any law which is substantially similar to, or serves the same purposes as, this Ordinance, he shall, either by repealing or amending that notice, cause that place to cease to be specified for the purposes of this section.
 71 | (5)For the avoidance of doubt, it is hereby declared that—
 72 | (a)for the purposes of subsection (1)(b), a data user which is a company incorporated in Hong Kong is a data user whose principal place of business is in Hong Kong;
 73 | (b)a notice under subsection (3) is subsidiary legislation; and
 74 | (c)this section shall not operate to prejudice the generality of section 50.
 75 | 34.(Repealed 18 of 2012 s. 20)
 76 | 35.Repeated collections of personal data in same circumstances
 77 | (1)A data user who—
 78 | (a)has complied with the provisions of data protection principle 1(3) in respect of the collection of any personal data from the data subject (first collection); and
 79 | (b)on any subsequent occasion again collects personal data from the data subject (subsequent collection),
 80 | is not required to comply with those provisions in respect of the subsequent collection if, but only if—
 81 | (i)to comply with those provisions in respect of that subsequent collection would be to repeat, without any material difference, what was done to comply with that principle in respect of the first collection; and
 82 | (ii)not more than 12 months have elapsed between the first collection and the subsequent collection.
 83 | (2)For the avoidance of doubt, it is hereby declared that subsection (1) shall not operate to prevent a subsequent collection from becoming a first collection if, but only if, the data user concerned has complied with the provisions of data protection principle 1(3) in respect of the subsequent collection.
 84 | Part 6A
 85 | Use of Personal Data in Direct Marketing and Provision of Personal Data for Use in Direct Marketing
 86 | (Part 6A added 18 of 2012 s. 21)
 87 | Division 1Interpretation
 88 | 35A.Interpretation of Part 6A
 89 | (1)In this Part—
 90 | consent (同意), in relation to a use of personal data in direct marketing or a provision of personal data for use in direct marketing, includes an indication of no objection to the use or provision;
 91 | direct marketing (直接促銷) means—
 92 | (a)the offering, or advertising of the availability, of goods, facilities or services; or
 93 | (b)the solicitation of donations or contributions for charitable, cultural, philanthropic, recreational, political or other purposes,
 94 | through direct marketing means;
 95 | direct marketing means (直接促銷方法) means—
 96 | (a)sending information or goods, addressed to specific persons by name, by mail, fax, electronic mail or other means of communication; or
 97 | (b)making telephone calls to specific persons;
 98 | marketing subject (促銷標的), in relation to direct marketing, means—
 99 | (a)any goods, facility or service offered, or the availability of which is advertised; or
100 | (b)any purpose for which donations or contributions are solicited;
101 | permitted class of marketing subjects (許可類別促銷標的), in relation to a consent by a data subject to an intended use or provision of personal data, means a class of marketing subjects—
102 | (a)that is specified in the information provided to the data subject under section 35C(2)(b)(ii) or 35J(2)(b)(iv); and
103 | (b)in relation to which the consent is given;
104 | permitted class of persons (許可類別人士), in relation to a consent by a data subject to an intended provision of personal data, means a class of persons—
105 | (a)that is specified in the information provided to the data subject under section 35J(2)(b)(iii); and
106 | (b)in relation to which the consent is given;
107 | permitted kind of personal data (許可種類個人資料), in relation to a consent by a data subject to an intended use or provision of personal data, means a kind of personal data—
108 | (a)that is specified in the information provided to the data subject under section 35C(2)(b)(i) or 35J(2)(b)(ii); and
109 | (b)in relation to which the consent is given;
110 | response channel (回應途徑) means a channel provided by a data user to a data subject under section 35C(2)(c) or 35J(2)(c).
111 | (2)For the purposes of this Part, a person provides personal data for gain if the person provides personal data in return for money or other property, irrespective of whether—
112 | (a)the return is contingent on any condition; or
113 | (b)the person retains any control over the use of the data.
114 | (Amended E.R. 1 of 2013)
115 | Division 2Use of Personal Data in Direct Marketing
116 | 35B.Application
117 | This Division does not apply in relation to the offering, or advertising of the availability, of—
118 | (a)social services run, subvented or subsidized by the Social Welfare Department;
119 | (b)health care services provided by the Hospital Authority or Department of Health; or
120 | (c)any other social or health care services which, if not provided, would be likely to cause serious harm to the physical or mental health of—
121 | (i)the individual to whom the services are intended to be provided; or
122 | (ii)any other individual.
123 | 35C.Data user to take specified action before using personal data in direct marketing
124 | (1)Subject to section 35D, a data user who intends to use a data subject’s personal data in direct marketing must take each of the actions specified in subsection (2).
125 | (2)The data user must—
126 | (a)inform the data subject—
127 | (i)that the data user intends to so use the personal data; and
128 | (ii)that the data user may not so use the data unless the data user has received the data subject’s consent to the intended use;
129 | (b)provide the data subject with the following information in relation to the intended use—
130 | (i)the kinds of personal data to be used; and
131 | (ii)the classes of marketing subjects in relation to which the data is to be used; and
132 | (c)provide the data subject with a channel through which the data subject may, without charge by the data user, communicate the data subject’s consent to the intended use.
133 | (3)Subsection (1) applies irrespective of whether the personal data is collected from the data subject by the data user.
134 | (4)The information provided under subsection (2)(a) and (b) must be presented in a manner that is easily understandable and, if in written form, easily readable.
135 | (5)Subject to section 35D, a data user who uses a data subject’s personal data in direct marketing without taking each of the actions specified in subsection (2) commits an offence and is liable on conviction to a fine of $500,000 and to imprisonment for 3 years.
136 | (6)In any proceedings for an offence under subsection (5), it is a defence for the data user charged to prove that the data user took all reasonable precautions and exercised all due diligence to avoid the commission of the offence.
137 | (7)In any proceedings for an offence under subsection (5), the burden of proving that this section does not apply because of section 35D lies on the data user.
138 | 35D.Circumstances under which section 35C does not apply
139 | (1)If, before the commencement date—
140 | (a)a data subject had been explicitly informed by a data user in an easily understandable and, if informed in writing, easily readable manner of the intended use or use of the data subject’s personal data in direct marketing in relation to a class of marketing subjects;
141 | (b)the data user had so used any of the data;
142 | (c)the data subject had not required the data user to cease to so use any of the data; and
143 | (d)the data user had not, in relation to the use, contravened any provision of this Ordinance as in force as at the time of the use,
144 | then section 35C does not apply in relation to the intended use or use, on or after the commencement date*, of the data subject’s relevant personal data, as updated from time to time, in direct marketing in relation to the class of marketing subjects.
145 | (2)If—
146 | (a)a data subject’s personal data is provided to a data user by a person other than the data subject (third person); and
147 | (b)the third person has by notice in writing to the data user—
148 | (i)stated that sections 35J and 35K have been complied with in relation to the provision of data; and
149 | (ii)specified the class of marketing subjects in relation to which the data may be used in direct marketing by the data user, as consented to by the data subject,
150 | then section 35C does not apply in relation to the intended use or use by the data user of the data in direct marketing in relation to that class of marketing subjects.
151 | (3)In this section—
152 | *commencement date (本部生效日期) means the date on which this Part comes into operation;
153 | relevant personal data (有關個人資料), in relation to a data subject, means any personal data of the data subject over the use of which a data user had control immediately before the commencement date.
154 | Editorial Note:
155 | * Commencement date : 1 April 2013
156 | 35E.Data user must not use personal data in direct marketing without data subject’s consent
157 | (1)A data user who has complied with section 35C must not use the data subject’s personal data in direct marketing unless—
158 | (a)the data user has received the data subject’s consent to the intended use of personal data, as described in the information provided by the data user under section 35C(2)(b), either generally or selectively;
159 | (b)if the consent is given orally, the data user has, within 14 days from receiving the consent, sent a written confirmation to the data subject, confirming—
160 | (i)the date of receipt of the consent;
161 | (ii)the permitted kind of personal data; and
162 | (iii)the permitted class of marketing subjects; and
163 | (c)the use is consistent with the data subject’s consent.
164 | (2)For the purposes of subsection (1)(c), the use of personal data is consistent with the data subject’s consent if—
165 | (a)the personal data falls within a permitted kind of personal data; and
166 | (b)the marketing subject in relation to which the data is used falls within a permitted class of marketing subjects.
167 | (3)A data subject may communicate to a data user the consent to a use of personal data either through a response channel or other means.
168 | (4)A data user who contravenes subsection (1) commits an offence and is liable on conviction to a fine of $500,000 and to imprisonment for 3 years.
169 | (5)In any proceedings for an offence under subsection (4), it is a defence for the data user charged to prove that the data user took all reasonable precautions and exercised all due diligence to avoid the commission of the offence.
170 | 35F.Data user must notify data subject when using personal data in direct marketing for first time
171 | (1)A data user must, when using a data subject’s personal data in direct marketing for the first time, inform the data subject that the data user must, without charge to the data subject, cease to use the data in direct marketing if the data subject so requires.
172 | (2)Subsection (1) applies irrespective of whether the personal data is collected from the data subject by the data user.
173 | (3)A data user who contravenes subsection (1) commits an offence and is liable on conviction to a fine of $500,000 and to imprisonment for 3 years.
174 | (4)In any proceedings for an offence under subsection (3), it is a defence for the data user charged to prove that the data user took all reasonable precautions and exercised all due diligence to avoid the commission of the offence.
175 | 35G.Data subject may require data user to cease to use personal data in direct marketing
176 | (1)A data subject may, at any time, require a data user to cease to use the data subject’s personal data in direct marketing.
177 | (2)Subsection (1) applies irrespective of whether the data subject—
178 | (a)has received from the data user the information required to be provided in relation to the use of personal data under section 35C(2); or
179 | (b)has earlier given consent to the data user or a third person to the use.
180 | (3)A data user who receives a requirement from a data subject under subsection (1) must, without charge to the data subject, comply with the requirement.
181 | (4)A data user who contravenes subsection (3) commits an offence and is liable on conviction to a fine of $500,000 and to imprisonment for 3 years.
182 | (5)In any proceedings for an offence under subsection (4), it is a defence for the data user charged to prove that the data user took all reasonable precautions and exercised all due diligence to avoid the commission of the offence.
183 | (6)This section does not affect the operation of section 26.
184 | 35H.Prescribed consent for using personal data in direct marketing under data protection principle 3
185 | Despite section 2(3), where a data user requires, under data protection principle 3, the prescribed consent of a data subject for using any personal data of the data subject in direct marketing, the data user is to be taken to have obtained the consent if the data user has not contravened section 35C, 35E or 35G.
186 | Division 3Provision of Personal Data for Use in Direct Marketing
187 | 35I.Application
188 | (1)This Division does not apply if a data user provides, otherwise than for gain, personal data of a data subject to another person for use by that other person in offering, or advertising the availability, of—
189 | (a)social services run, subvented or subsidized by the Social Welfare Department;
190 | (b)health care services provided by the Hospital Authority or Department of Health; or
191 | (c)any other social or health care services which, if not provided, would be likely to cause serious harm to the physical or mental health of—
192 | (i)the individual to whom the services are intended to be provided; or
193 | (ii)any other individual.
194 | (2)This Division does not apply if a data user provides personal data of a data subject to an agent of the data user for use by the agent in carrying out direct marketing on the data user’s behalf.
195 | 35J.Data user to take specified action before providing personal data
196 | (1)A data user who intends to provide a data subject’s personal data to another person for use by that other person in direct marketing must take each of the actions specified in subsection (2).
197 | (2)The data user must—
198 | (a)inform the data subject in writing—
199 | (i)that the data user intends to so provide the personal data; and
200 | (ii)that the data user may not so provide the data unless the data user has received the data subject’s written consent to the intended provision;
201 | (b)provide the data subject with the following written information in relation to the intended provision—
202 | (i)if the data is to be provided for gain, that the data is to be so provided;
203 | (ii)the kinds of personal data to be provided;
204 | (iii)the classes of persons to which the data is to be provided; and
205 | (iv)the classes of marketing subjects in relation to which the data is to be used; and
206 | (c)provide the data subject with a channel through which the data subject may, without charge by the data user, communicate the data subject’s consent to the intended provision in writing.
207 | (3)Subsection (1) applies irrespective of whether the personal data is collected from the data subject by the data user.
208 | (4)The information provided under subsection (2)(a) and (b) must be presented in a manner that is easily understandable and easily readable.
209 | (5)A data user who provides personal data of a data subject to another person for use by that other person in direct marketing without taking each of the actions specified in subsection (2) commits an offence and is liable on conviction—
210 | (a)if the data is provided for gain, to a fine of $1,000,000 and to imprisonment for 5 years; or
211 | (b)if the data is provided otherwise than for gain, to a fine of $500,000 and to imprisonment for 3 years.
212 | (6)In any proceedings for an offence under subsection (5), it is a defence for the data user charged to prove that the data user took all reasonable precautions and exercised all due diligence to avoid the commission of the offence.
213 | 35K.Data user must not provide personal data for use in direct marketing without data subject’s consent
214 | (1)A data user who has complied with section 35J must not provide the data subject’s personal data to another person for use by that other person in direct marketing unless—
215 | (a)the data user has received the data subject’s written consent to the intended provision of personal data, as described in the information provided by the data user under section 35J(2)(b), either generally or selectively;
216 | (b)if the data is provided for gain, the intention to so provide was specified in the information under section 35J(2)(b)(i); and
217 | (c)the provision is consistent with the data subject’s consent.
218 | (2)For the purposes of subsection (1)(c), the provision of personal data is consistent with the data subject’s consent if—
219 | (a)the personal data falls within a permitted kind of personal data;
220 | (b)the person to whom the data is provided falls within a permitted class of persons; and
221 | (c)the marketing subject in relation to which the data is to be used falls within a permitted class of marketing subjects.
222 | (3)A data subject may communicate to a data user the consent to a provision of personal data either through a response channel or other written means.
223 | (4)A data user who contravenes subsection (1) commits an offence and is liable on conviction—
224 | (a)if the data user provides the personal data for gain, to a fine of $1,000,000 and to imprisonment for 5 years; or
225 | (b)if the data user provides the personal data otherwise than for gain, to a fine of $500,000 and to imprisonment for 3 years.
226 | (5)In any proceedings for an offence under subsection (4), it is a defence for the data user charged to prove that the data user took all reasonable precautions and exercised all due diligence to avoid the commission of the offence.
227 | 35L.Data subject may require data user to cease to provide personal data for use in direct marketing
228 | (1)A data subject who has been provided with information by a data user under section 35J(2)(b) may, at any time, require the data user—
229 | (a)to cease to provide the data subject’s personal data to any other person for use by that other person in direct marketing; and
230 | (b)to notify any person to whom the data has been so provided to cease to use the data in direct marketing.
231 | (2)Subsection (1) applies irrespective of whether the data subject has earlier given consent to the provision of the personal data.
232 | (3)A data user who receives a requirement from a data subject under subsection (1) must, without charge to the data subject, comply with the requirement.
233 | (4)If a data user is required to notify a person to cease to use a data subject’s personal data in direct marketing under a requirement referred to in subsection (1)(b), the data user must so notify the person in writing.
234 | (5)A person who receives a written notification from a data user under subsection (4) must cease to use the personal data in direct marketing in accordance with the notification.
235 | (6)A data user who contravenes subsection (3) commits an offence and is liable on conviction—
236 | (a)if the contravention involves a provision of personal data of a data subject for gain, to a fine of $1,000,000 and to imprisonment for 5 years; or
237 | (b)in any other case, to a fine of $500,000 and to imprisonment for 3 years.
238 | (7)A person who contravenes subsection (5) commits an offence and is liable on conviction to a fine of $500,000 and to imprisonment for 3 years.
239 | (8)In any proceedings for an offence under subsection (6) or (7), it is a defence for the data user or person charged to prove that the data user or person took all reasonable precautions and exercised all due diligence to avoid the commission of the offence.
240 | (9)This section does not affect the operation of section 26.
241 | 35M.Prescribed consent for providing personal data for use in direct marketing under data protection principle 3
242 | Despite section 2(3), where a data user requires, under data protection principle 3, the prescribed consent of a data subject for providing any personal data of the data subject to another person for use in direct marketing, the data user is to be taken to have obtained the consent if the data user has not contravened section 35J, 35K or 35L.
243 | 


--------------------------------------------------------------------------------
/kb/data_privacy/MY_PDPA_DIV1.txt:
--------------------------------------------------------------------------------
  1 | Malaysia Personal Data Protection Act 2010/()/()/
  2 | Place: Malaysia
  3 | Effective Date: 2010-12-01
  4 | 
  5 | Division 1 - Personal Data Protection Principles
  6 | Section 5. Personal Data Protection Principles
  7 | (1) The processing of personal data by a data user shall be in compliance with the following Personal Data Protection Principles, namely—
  8 | (a) the General Principle;
  9 | (b) the Notice and Choice Principle;
 10 | (c) the Disclosure Principle;
 11 | (d) the Security Principle;
 12 | (e) the Retention Principle;
 13 | (f) the Data Integrity Principle; and
 14 | (g) the Access Principle,
 15 | as set out in sections 6, 7, 8, 9, 10, 11 and 12.
 16 | (2) Subject to sections 45 and 46, a data user who contravenes subsection (1) commits an offence and shall, on conviction, be liable to a fine not exceeding three hundred thousand ringgit or to imprisonment for a term not exceeding two years or to both.
 17 | 
 18 | Section 6. General Principle
 19 | (1) A data user shall not—
 20 | (a) in the case of personal data other than sensitive personal data, process personal data
 21 | about a data subject unless the data subject has given his consent to the processing of the
 22 | personal data; or
 23 | (b) in the case of sensitive personal data, process sensitive personal data about a data subject
 24 | except in accordance with the provisions of section 40.
 25 | (2) Notwithstanding paragraph (1)(a), a data user may process personal data about a data subject if the processing is necessary—
 26 | (a) for the performance of a contract to which the data subject is a party;
 27 | (b) for the taking of steps at the request of the data subject with a view to entering into a contract;
 28 | (c) for compliance with any legal obligation to which the data user is the subject, other than an obligation imposed by a contract;
 29 | (d) in order to protect the vital interests of the data subject;
 30 | (e) for the administration of justice; or
 31 | (f) for the exercise of any functions conferred on any person by or under any law.
 32 | (3) Personal data shall not be processed unless—
 33 | (a) the personal data is processed for a lawful purpose directly related to an activity of the data user;
 34 | (b) the processing of the personal data is necessary for or directly related to that purpose; and
 35 | (c) the personal data is adequate but not excessive in relation to that purpose.
 36 | 
 37 | Section 7. Notice and Choice Principle
 38 | (1) A data user shall by written notice inform a data subject—
 39 | (a) that personal data of the data subject is being processed by or on behalf of the data user, and shall provide a description of the personal data to that data subject;
 40 | (b) the purposes for which the personal data is being or is to be collected and further processed;
 41 | (c) of any information available to the data user as to the source of that personal data;
 42 | (d) of the data subject’s right to request access to and to request correction of the personal data and how to contact the data user with any inquiries or complaints in respect of the personal data;
 43 | (e) of the class of third parties to whom the data user discloses or may disclose the personal data;
 44 | (f) of the choices and means the data user offers the data subject for limiting the processing of personal data, including personal data relating to other persons who may be identified from that personal data;
 45 | (g) whether it is obligatory or voluntary for the data subject to supply the personal data; and
 46 | (h) where it is obligatory for the data subject to supply the personal data, the consequences for the data subject if he fails to supply the personal data.
 47 | (2) The notice under subsection (1) shall be given as soon as practicable by the data user—
 48 | (a) when the data subject is first asked by the data user to provide his personal data;
 49 | (b) when the data user first collects the personal data of the data subject; or
 50 | (c) in any other case, before the data user—
 51 | (i) uses the personal data of the data subject for a purpose other than the purpose for which the personal data was collected; or
 52 | (ii) discloses the personal data to a third party.
 53 | (3) A notice under subsection (1) shall be in the national and English languages, and the
 54 | individual shall be provided with a clear and readily accessible means to exercise his choice,
 55 | where necessary, in the national and English languages.
 56 | Section 8. Disclosure Principle
 57 | Subject to section 39, no personal data shall, without the consent of the data subject, be
 58 | disclosed—
 59 | (a) for any purpose other than—
 60 | (i) the purpose for which the personal data was to be disclosed at the time of collection of the personal data; or
 61 | (ii) a purpose directly related to the purpose referred to in subparagraph (i); or
 62 | (b) to any party other than a third party of the class of third parties as specified in paragraph
 63 | 7(1)(e).
 64 | Section 9. Security Principle
 65 | (1) A data user shall, when processing personal data, take practical steps to protect the personal data from any loss, misuse, modification, unauthorized or accidental access or disclosure, alteration or destruction by having regard—
 66 | (a) to the nature of the personal data and the harm that would result from such loss, misuse,
 67 | modification, unauthorized or accidental access or disclosure, alteration or destruction;
 68 | (b) to the place or location where the personal data is stored;
 69 | (c) to any security measures incorporated into any equipment in which the personal data is stored;
 70 | (d) to the measures taken for ensuring the reliability, integrity and competence of personnel having access to the personal data; and
 71 | (e) to the measures taken for ensuring the secure transfer of the personal data.
 72 | (2) Where processing of personal data is carried out by a data processor on behalf of the data user, the data user shall, for the purpose of protecting the personal data from any loss, misuse, modification, unauthorized or accidental access or disclosure, alteration or destruction, ensure that the data processor—
 73 | (a) provides sufficient guarantees in respect of the technical and organizational security measures governing the processing to be carried out; and
 74 | (b) takes reasonable steps to ensure compliance with those measures.
 75 | Section 10. Retention Principle
 76 | (1) The personal data processed for any purpose shall not be kept longer than is necessary for the fulfilment of that purpose.
 77 | (2) It shall be the duty of a data user to take all reasonable steps to ensure that all personal data is destroyed or permanently deleted if it is no longer required for the purpose for which it was to be processed.
 78 | Section 11. Data Integrity Principle
 79 | A data user shall take reasonable steps to ensure that the personal data is accurate, complete,
 80 | not misleading and kept up-to-date by having regard to the purpose, including any directly related
 81 | purpose, for which the personal data was collected and further processed.
 82 | Section 12. Access Principle
 83 | A data subject shall be given access to his personal data held by a data user and be able to correct that personal data where the personal data is inaccurate, incomplete, misleading or not up-to-date, except where compliance with a request to such access or correction is refused under this Act.
 84 | Division 2 – Registration
 85 | Section 13. Application of this Division
 86 | (1) This Division shall apply to a data user who belongs to a class of data users as specified in the
 87 | order made under subsection 14(1).
 88 | (2) A data user who belongs to a class of data users not specified in the order made under subsection 14(1) shall comply with all the provisions of this Act other than the provisions of this Division relating to the registration of data users and matters connected thereto.
 89 | Section 14. Registration of data users
 90 | (1) The Minister may, upon the recommendation of the Commissioner, by order published in
 91 | the Gazette, specify a class of data users who shall be required to be registered as data users
 92 | under this Act.
 93 | (2) The Commissioner shall, before making his recommendation under subsection (1), consult
 94 | with—
 95 | (a) such bodies representative of data users belonging to that class; or
 96 | (b) such other interested persons.
 97 | Section 15. Application for registration
 98 | (1) A person who belongs to the class of data users as specified in the order made under subsection 14(1) shall submit an application for registration to the Commissioner in the manner and form as determined by the Commissioner.
 99 | (2) Every application for registration shall be accompanied with the prescribed registration fee and such documents as may be required by the Commissioner.
100 | (3) The Commissioner may in writing at any time after receiving the application and before it is determined, require the applicant to provide such additional documents or information within the time as specified by the Commissioner.
101 | (4) If the requirement under subsection (3) is not complied with, the application for registration shall be deemed to have been withdrawn by the applicant and shall not be further proceeded with by the Commissioner, but without prejudice to a fresh application being made by the applicant.
102 | Section 16. Certificate of registration
103 | (1) After having given due consideration to an application under subsection 15(1), the
104 | Commissioner may—(a) register the applicant and issue a certificate of registration to the applicant in such form as determined by the Commissioner; or
105 | (b) refuse the application.
106 | (2) The certificate of registration may be issued subject to such conditions or restrictions as the
107 | Commissioner may think fit to impose.
108 | (3) Where the Commissioner refuses the application for registration in pursuance of subsection (1), he shall inform the applicant by a written notice that the application has been refused and the reasons for the refusal.
109 | (4) A person who belongs to the class of data users as specified in the order made under subsection 14(1) and who processes personal data without a certificate of registration issued in pursuance of paragraph 16(1)(a) commits an offence and shall, on conviction, be liable to a fine not exceeding five hundred thousand ringgit or to imprisonment for a term not exceeding three years or to both.
110 | Section 17. Renewal of certificate of registration
111 | (1) A data user may make an application for the renewal of the certificate of registration not later than ninety days before the date of expiry of the certificate of registration in the manner and form as determined by the Commissioner and the application shall be accompanied with the prescribed renewal fee and such documents as may be required by the Commissioner, but no application for renewal shall be allowed where the application is made after the date of expiry of the certificate of registration.
112 | (2) When renewing a certificate of registration, the Commissioner may vary the conditions or restrictions imposed upon the issuance of the certificate of registration or impose additional conditions or restrictions.
113 | (3) The Commissioner may refuse to renew a certificate of registration—
114 | (a) if the data user has failed to comply with any of the provisions of this Act;
115 | (b) if the data user has failed to comply with any conditions or restrictions imposed upon the issuance of the certificate of registration; or
116 | (c) if he is satisfied that the data user is unable to continue the processing of personal data in accordance with this Act.
117 | 


--------------------------------------------------------------------------------
/kb/data_privacy/MY_PDPA_DIV3.txt:
--------------------------------------------------------------------------------
  1 | Malaysia Personal Data Protection Act 2010/()/()/
  2 | Place: Malaysia
  3 | Effective Date: 2010-12-01
  4 | 
  5 | Division 4 - Rights of data subject
  6 | Section 30. Right of access to personal data
  7 | (1) An individual is entitled to be informed by a data user whether personal data of which that individual is the data subject is being processed by or on behalf of the data user.
  8 | (2) A requestor may, upon payment of a prescribed fee, make a data access request in writing to the data user—
  9 | (a) for information of the data subject’s personal data that is being processed by or on behalf of the data user; and
 10 | (b) to have communicated to him a copy of the personal data in an intelligible form.
 11 | (3) A data access request for any information under subsection (2) shall be treated as a single request, and a data access request for information under paragraph (2)(a) shall, in the absence of any indication to the contrary, be treated as extending also to such request under paragraph
 12 | (2)(b).
 13 | (4) In the case of a data user having separate entries in respect of personal data held for different purposes, a separate data access request shall be made for each separate entry.
 14 | (5) Where a data user does not hold the personal data, but controls the processing of the personal data in such a way as to prohibit the data user who holds the personal data from complying, whether in whole or part, with the data access request under subsection (2) which relates to the personal data, the firstmentioned data user shall be deemed to hold the personal data and the provisions of this Act shall be construed accordingly
 15 | 
 16 | Section 31. Compliance with data access request
 17 | (1) Subject to subsection (2) and section 32, a data user shall comply with a data access request under section 30 not later than twenty-one days from the date of receipt of the data access request.
 18 | (2) A data user who is unable to comply with a data access request within the period specified in subsection (1) shall before the expiration of that period—
 19 | (a) by notice in writing inform the requestor that he is unable to comply with the data access request within such period and the reasons why he is unable to do so; and
 20 | (b) comply with the data access request to the extent that he is able to do so.
 21 | (3) Notwithstanding subsection (2), the data user shall comply in whole with the data access request not later than fourteen days after the expiration of the period stipulated in subsection (1).
 22 | 
 23 | Section 32. Circumstances where data user may refuse to comply with data access request
 24 | (1) A data user may refuse to comply with a data access request under section 30 if—
 25 | (a) the data user is not supplied with such information as he may reasonably require—
 26 | (i) in order to satisfy himself as to the identity of the requestor; or
 27 | (ii) where the requestor claims to be a relevant person, in order to satisfy himself—
 28 | (A) as to the identity of the data subject in relation to whom the requestor claims to be the relevant person; and
 29 | (B) that the requestor is the relevant person in relation to the data subject;
 30 | (b) the data user is not supplied with such information as he may reasonably require to locate
 31 | the personal data to which the data access request relates;
 32 | (c) the burden or expense of providing access is disproportionate to the risks to the data
 33 | subject’s privacy in relation to the personal data in the case in question;
 34 | (d) the data user cannot comply with the data access request without disclosing personal data
 35 | relating to another individual who can be identified from that information, unless—
 36 | (i) that other individual has consented to the disclosure of the information to the requestor;
 37 | or
 38 | (ii) it is reasonable in all the circumstances to comply with the data access request without the consent of the other individual;
 39 | (e) subject to subsection (3), any other data user controls the processing of the personal data to which the data access request relates in such a way as to prohibit the first-mentioned data user from complying, whether in whole or in part, with the data access request;
 40 | (f) providing access would constitute a violation of an order of a court;
 41 | (g) providing access would disclose confidential commercial information; or
 42 | (h) such access to personal data is regulated by another law.
 43 | (2) In determining for the purposes of subparagraph (1)(d)(ii) whether it is reasonable in all the circumstances to comply with the data access request without the consent of the other individual, regard shall be had, in particular, to—
 44 | (a) any duty of confidentiality owed to the other individual;
 45 | (b) any steps taken by the data user with a view to seeking the consent of the other individual;
 46 | (c) whether the other individual is capable of giving consent; and
 47 | (d) any express refusal of consent by the other individual.
 48 | (3) Paragraph (1)(e) shall not operate so as to excuse the data user from complying with the data access request under subsection 30(2) to any extent that the data user can comply with the data access request without contravening the prohibition concerned.
 49 | 
 50 | Section 33. Notification of refusal to comply with data access request
 51 | Where a data user who pursuant to section 32 refuses to comply with a data access request under section 30, he shall, not later than twenty-one days from the date of receipt of the data access request, by notice in writing, inform the requestor—
 52 | (a) of the refusal and the reasons for the refusal; and
 53 | (b) where paragraph 32(1)(e) is applicable, of the name and address of the other data user concerned.
 54 | Section 34. Right to correct personal data
 55 | (1) Where—
 56 | (a) a copy of the personal data has been supplied by the data user in compliance with the data access request under section 30 and the requestor considers that the personal data is inaccurate, incomplete, misleading or not up-to-date; or
 57 | (b) the data subject knows that his personal data being held by the data user is inaccurate, incomplete, misleading or not up-to-date, the requestor or data subject, as the case may be, may make a data correction request in writing to the data user that the data user makes the necessary correction to the personal data.
 58 | (2) Where a data user does not hold the personal data, but controls the processing of the personal data in such a way as to prohibit the data user who holds the personal data from complying, whether in whole or in part, with the data correction request under subsection (1) which relates to the personal data, the first-mentioned data user shall be deemed to be the data user to whom such a request may be made and the provisions of this Act shall be construed accordingly.
 59 | Section 35. Compliance with data correction request
 60 | (1) Subject to subsections (2), (3) and (5) and section 36, where a data user is satisfied that the personal data to which a data correction request relates is inaccurate, incomplete, misleading or not up-to-date, he shall, not later than twenty-one days from the date of receipt of the data correction request—
 61 | (a) make the necessary correction to the personal data;
 62 | (b) supply the requestor with a copy of the personal data as corrected; and
 63 | (c) subject to subsection (4), where—
 64 | (i) the personal data has been disclosed to a third party during the twelve months immediately preceding the day on which the correction is made; and
 65 | (ii) the data user has no reason to believe that the third party has ceased using the personal data for the purpose, including any directly related purpose, for which the personal data was disclosed to the third party, take all practicable steps to supply the third party with a copy of the personal data as so corrected accompanied by a notice in writing stating the reasons for the correction.
 66 | (2) A data user who is unable to comply with a data correction request within the period specified in subsection (1) shall before the expiration of that period—
 67 | (a) by notice in writing inform the requestor that he is unable to comply with the data correction request within such period and the reasons why he is unable to do so; and
 68 | (b) comply with the data correction request to the extent that he is able to do so.
 69 | (3) Notwithstanding subsection (2), the data user shall comply in whole with the data correction request not later than fourteen days after the expiration of the period stipulated in subsection (1).
 70 | (4) A data user is not required to comply with paragraph (1)(c) in any case where the disclosure of the personal data to a third party consists of the third party’s own inspection of a register—
 71 | (a) in which the personal data is entered or otherwise recorded; and
 72 | (b) which is available for inspection by the public.
 73 | (5) Where a data user is requested to correct personal data under subsection 34(1) and the personal data is being processed by another data user that is in a better position to respond to the data correction request—
 74 | (a) the first-mentioned data user shall immediately transfer the data correction request to such data user, and notify the requestor of this fact; and
 75 | (b) sections 34, 35, 36 and 37 shall apply as if the references therein to a data user were references to such other data user.
 76 | Section 36. Circumstances where data user may refuse to comply with data
 77 | correction request
 78 | (1) A data user may refuse to comply with a data correction request under section 34 if—
 79 | (a) the data user is not supplied with such information as he may reasonably require—
 80 | (i) in order to satisfy himself as to the identity of the requestor; or
 81 | (ii) where the requestor claims to be a relevant person, in order to satisfy himself—
 82 | (A) as to the identity of the data subject in relation to whom the requestor claims to be the relevant
 83 | person; and
 84 | (B) that the requestor is the relevant person in relation to the data subject;
 85 | (b) the data user is not supplied with such information as he may reasonably require to ascertain in what way the personal data to which the data correction request relates is inaccurate, incomplete, misleading or not up-to-date;
 86 | (c) the data user is not satisfied that the personal data to which the data correction request relates is inaccurate, incomplete, misleading or not up-to-date;
 87 | (d) the data user is not satisfied that the correction which is the subject of the data correction request is accurate, complete, not misleading or up-to-date; or
 88 | (e) subject to subsection (2), any other data user controls the processing of the personal data to which the data correction request relates in such a way as to prohibit the first-mentioned data user from complying, whether in whole or in part, with the data correction request.
 89 | (2) Paragraph (1)(e) shall not operate so as to excuse the data user from complying with subsection 35(1) in relation to the data correction request to any extent that the data user can comply with that subsection without contravening the prohibition concerned.
 90 | Section 37. Notification of refusal to comply with data correction request
 91 | (1) Where a data user who pursuant to section 36 refuses to comply with a data correction request under section 34, he shall, not later than twenty-one days from the date of receipt of the data correction request, by notice in writing, inform the requestor—
 92 | (a) of the refusal and the reasons for the refusal; and
 93 | (b) where paragraph 36(1)(e) is applicable, of the name and address of the other data user
 94 | concerned.
 95 | (2) Without prejudice to the generality of subsection (1), where personal data to which the data correction request relates is an expression of opinion and the data user is not satisfied that the expression of opinion is inaccurate, incomplete, misleading or not up-to-date, the data user
 96 | shall—
 97 | (a) make a note, whether annexed to the personal data or elsewhere—
 98 | (i) of the matters in respect of which the expression of opinion is considered by the requestor to be inaccurate, incomplete, misleading or not up-to-date; and
 99 | (ii) in such a way that the personal data cannot be used by any person without the note being drawn to the attention of and being available for inspection by that person; and
100 | (b) attach a copy of the note to the notice referred to in subsection (1) which relates to the data correction request.
101 | (3) In this section, “expression of opinion” includes an assertion of fact which is unverifiable or in
102 | all circumstances of the case is not practicable to verify.
103 | (4) A data user who contravenes subsection (2) commits an offence and shall, on conviction, be liable to a fine not exceeding one hundred thousand ringgit or to imprisonment for a term not exceeding one year or to both.
104 | Section 38. Withdrawal of consent to process personal data
105 | (1) A data subject may by notice in writing withdraw his consent to the processing of personal
106 | data in respect of which he is the data subject.
107 | (2) The data user shall, upon receiving the notice under subsection (1), cease the processing of
108 | the personal data.
109 | (3) The failure of the data subject to exercise the right conferred by subsection (1) does not affect
110 | any other rights conferred on him by this Part.
111 | (4) A data user who contravenes subsection (2) commits an offence and shall, on conviction, be liable to a fine not exceeding one hundred thousand ringgit or to imprisonment for a term not exceeding one year or to both.
112 | Section 39. Extent of disclosure of personal data
113 | Notwithstanding section 8, personal data of a data subject may be disclosed by a data user for any purpose other than the purpose for which the personal data was to be disclosed at the time of its collection or any other purpose directly related to that purpose, only under the following circumstances:
114 | (a) the data subject has given his consent to the disclosure;
115 | (b) the disclosure —
116 | (i) is necessary for the purpose of preventing or detecting a crime, or for the purpose of investigations; or
117 | (ii) was required or authorized by or under any law or by the order of a court;
118 | (c) the data user acted in the reasonable belief that he had in law the right to disclose the personal data to the other person;
119 | (d) the data user acted in the reasonable belief that he would have had the consent of the data subject if the data subject had known of the disclosing of the personal data and the circumstances of such disclosure; or
120 | (e) the disclosure was justified as being in the public interest in circumstances as determined by the Minister.
121 | Section 40. Processing of sensitive personal data
122 | (1) Subject to subsection (2) and section 5, a data user shall not process any sensitive personal
123 | data of a data subject except in accordance with the following conditions:
124 | (a) the data subject has given his explicit consent to the processing of the personal data;
125 | (b) the processing is necessary—
126 | (i) for the purposes of exercising or performing any right or obligation which is conferred or
127 | imposed by law on the data user in connection with employment;
128 | (ii) in order to protect the vital interests of the data subject or another person, in a case
129 | where—
130 | (A) consent cannot be given by or on behalf of the data subject; or
131 | (B) the data user cannot reasonably be expected to obtain the consent of the data subject;
132 | (iii) in order to protect the vital interests of another person, in a case where consent by or
133 | on behalf of the data subject has been unreasonably withheld;
134 | (iv) for medical purposes and is undertaken by—
135 | (A) a healthcare professional; or
136 | (B) a person who in the circumstances owes a duty of confidentiality which is equivalent to that
137 | which would arise if that person were a healthcare professional;
138 | (v) for the purpose of, or in connection with, any legal proceedings;
139 | (vi) for the purpose of obtaining legal advice;
140 | (vii) for the purposes of establishing, exercising or defending legal rights;
141 | (viii) for the administration of justice;
142 | (ix) for the exercise of any functions conferred on any person by or under any written law;
143 | or
144 | (x) for any other purposes as the Minister thinks fit; or
145 | (c) the information contained in the personal data has been made public as a result of steps
146 | deliberately taken by the data subject.
147 | (2) The Minister may by order published in the Gazette exclude the application of subparagraph
148 | (1)(b)(i), (viii) or (ix) in such cases as may be specified in the order, or provide that, in such cases
149 | as may be specified in the order, the condition in subparagraph (1)(b)(i), (viii) or (ix) is not to be
150 | regarded as satisfied unless such further conditions as may be specified in the order are also
151 | satisfied.
152 | (3) A person who contravenes subsection (1) commits an offence and shall, on conviction, be
153 | liable to a fine not exceeding two hundred thousand ringgit or to imprisonment for a term not
154 | exceeding two years or to both.
155 | (4) For the purposes of this section—
156 | “medical purposes” includes the purposes of preventive medicine, medical diagnosis, medical
157 | research, rehabilitation and the provision of care and treatment and the management of
158 | healthcare services;
159 | “healthcare services” has the meaning assigned to it in the Private Healthcare Facilities and
160 | Services Act 1998 [Act 586]; “healthcare professional” means a medical practitioner, dental practitioner, pharmacist, clinical
161 | psychologist, nurse, midwife, medical assistant, physiotherapist, occupational therapist and other
162 | allied healthcare professionals and any other person involved in the giving of medical, health,
163 | dental, pharmaceutical and any other healthcare services under the jurisdiction of the Ministry of
164 | Health.
165 | 


--------------------------------------------------------------------------------
/kb/data_privacy/SG_PDPA.txt:
--------------------------------------------------------------------------------
 1 | Singapore Personal Data Protection Act 2014/()/()/
 2 | 
 3 | 
 4 | Personal Data Protection
 5 | Act 2012
 6 | 2020 REVISED EDITION
 7 | This revised edition incorporates all amendments up to and including 1 December 2021 and comes into operation on 31 December 2021
 8 | An Act to govern the collection, use and disclosure of personal data by organisations, and to establish the Do Not Call Register and to provide for its administration, and for matters connected therewith.
 9 | [22/2016]
10 | [Effective Dates:
11 |   2 January 2013: Parts I, II, VIII, IX (except sections 36 to 38, 41 and 43 to 48) and X (except section 67(1)), and the First, Seventh and Ninth Schedules;
12 |   2 December 2013: Sections 36, 37, 38 and 41;
13 |   2 January 2014: Sections 43 to 48 and 67(1) and the Eighth Schedule;
14 |   2 July 2014: Parts III to VII, and the Second to Sixth Schedules]
15 | 
16 | PART 1
17 | PRELIMINARY
18 | 
19 | Short Title
20 | 1. This Act is the Personal Data Protection Act 2012.
21 | 
22 | Interpretation
23 | 2.—(1) In this Act, unless the context otherwise requires —
24 |   “advisory committee” means an advisory committee appointed under section 7;
25 |   “Appeal Committee” means a Data Protection Appeal Committee constituted under section 48P(4), read with the Seventh Schedule;
26 |   “Appeal Panel” means the Data Protection Appeal Panel established by section 48P(1);
27 |   “authorised officer”, in relation to the exercise of any power or performance of any function or duty under any provision of this Act, means a person to whom the exercise of that power or performance of that function or duty under that provision has been delegated
28 | 


--------------------------------------------------------------------------------
/kb/data_privacy/uae_pdpl_2021.txt:
--------------------------------------------------------------------------------
  1 | Personal Data Protection Law 2021/()/()/
  2 | Place: United Arab Emirates
  3 | Effective Date: 2021-12-01
  4 | 
  5 | Article (2)
  6 | Scope of Application of the Decree by Law
  7 | 1.	Provisions of this Decree by Law shall apply to the processing of all or part of the Personal Data by means of electronic systems which operate automatically, or by other means, by the following:
  8 | a.	Each Data Subject residing in the State or having a place of business in it.
  9 | b.	Each Controller or Processor residing in the State and carrying out the activities of processing Personal Data of Data Subjects inside and outside the State.
 10 | c.	Each Controller or Processor residing outside the State and carrying out the activities of processing Personal Data of Data Subjects inside the State.
 11 | 2.	Provisions of this Decree by Law shall not apply to the following:
 12 | a.	Government Data
 13 | b.	Governmental entities which control or process Personal Data.
 14 | c.	Personal Data held by the security and judicial authorities
 15 | d.	A Data Subject who processes his/her data for personal purposes.
 16 | e.	Personal Health Data that has legislation regulating its protection and processing.
 17 | f.	Personal banking and credit data and information that have legislation regulating their protection and processing.
 18 | g.	Companies and establishments located in free zones in the Country and have special
 19 |  
 20 | legislations regarding Personal Data protection.
 21 | 
 22 | Article (3)
 23 | Bureau's Power of Exemption
 24 | Without prejudice to any other competencies prescribes for the Bureau under any other legislation, the Bureau may exempt some establishments that do not process a large volume of Personal Data from part, or all of the requirements of the personal data protection provisions stipulated in this Decree by Law, in accordance with the standards and controls set by the Executive Regulations of this Decree by Law.
 25 | 
 26 | Article (4)
 27 | Cases of Processing Personal Data without the Consent of its Owner
 28 | It is prohibited to process Personal Data without the consent of its owner. The following cases shall be excluded from such prohibition:
 29 | 1.	If the processing is necessary to protect public interest.
 30 | 2.	If the processing is related to Personal Data which has become available and known to all by an act of the Data Subject.
 31 | 3.	If the processing is necessary to initiate any procedures of legal claim or defense of rights or is related to judicial or security procedures.
 32 | 4.	If the processing is necessary for purposes of occupational or preventive medicine in order to assess the employees' ability of to work, performing medical diagnosis, providing health or social care, treatment or health insurance services, managing health or social care systems and services in accordance with the legislation in force in the State.
 33 |  
 34 | 5.	If the processing is necessary to protect public health, including protection from existing diseases and epidemics, or for the purposes of ensuring the safety and quality of healthcare, medicines, drugs and medical devices, in accordance with the legislation in force in the State.
 35 | 6.	If the processing is necessary for archival purposes or for scientific, historical and statistical studies in accordance with the legislation in force in the State.
 36 | 7.	If the processing is necessary to protect the interests of the Data Subject.
 37 | 8.	If the processing is necessary for the purposes of the Controller or Data Subject carrying out their obligations and exercising their legally established rights in the field of employment, social security or laws concerned with social protection, to the extent permitted by such Laws.
 38 | 9.	If the processing is necessary to perform a contract to which the Data Subject is a party, or to take measures at the request of the Data Subject with the aim of concluding, amending or terminating a contract.
 39 | 10.	If the processing is necessary to fulfil specific obligations stipulated in other laws in force in the State for the Controller.
 40 | 11.	Any other cases set out in the Executive Regulations of this Decree by Law.
 41 | 
 42 | Article (5)
 43 | Personal Data Processing Controls
 44 | Personal Data shall be processed according to the following controls:
 45 | 1.	Processing shall be carried out in a fair, transparent and lawful manner.
 46 | 2.	Personal Data shall be collected for a specific and clear purpose. It shall not be processed at
 47 |  
 48 | any later time in a manner incompatible with such purpose. However, it may be processed if the purpose is similar or close to the purpose for which this data is collected.
 49 | 3.	Personal Data shall be sufficient and limited to what is necessary in accordance with the purpose for which the processing is carried out.
 50 | 4.	Personal Data shall be accurate and correct and shall be updated whenever necessary.
 51 | 5.	The necessary measures shall be taken to ensure that incorrect Personal Data is deleted or corrected.
 52 | 6.	Personal Data shall be kept securely, including protecting it from any violation, penetration, or illegal or unauthorized processing through the development and use of appropriate technical and organizational measures and procedures in accordance with the laws and legislation in force in this regard.
 53 | 7.	Personal Data shall not be kept after the purpose of its processing has been exhausted. It may be kept if the identity of the Data Subject has been concealed using the "Anonymization Mechanism"
 54 | 8.	Any other controls set out in the Executive Regulations of this Decree by Law.
 55 | 
 56 | Article (6)
 57 | Terms of Consent to Data Processing
 58 | 1.	To be considered, the consent of the Data Subject to the processing of date shall require the following:
 59 | a.	The Controller shall be able to prove the consent of the Data Subject in the event that the processing of Personal Data is based on the consent of the Data Subject.
 60 | b.	The Consent shall be prepared in a clear, simple, unambiguous and easily accessible
 61 |  
 62 | manner, whether in writing or electronically.
 63 | c.	The Consent shall include the Data Subject's right to withdraw it easily.
 64 | 2.	The Data Subject may, at any time, withdraw their consent to the processing of Personal Data. Such withdrawal of consent shall not affect the legality of the processing based on the given consent before withdrawing it.
 65 | 
 66 | Article (7)
 67 | The Controller's General Obligations
 68 | The Controller shall abide by the following:
 69 | 1.	Take appropriate technical and organizational measures to implement the necessary standards to protect and secure Personal Data in order to preserve its confidentiality and privacy, and to ensure that it is not breached, destroyed, altered or tampered with, taking into account the nature, scope and purposes of processing and the possibility of risks to the confidentiality and privacy of the Data Subject's Personal Data.
 70 | 2.	Apply the appropriate measures, whether while determining the means of processing or while processing, in order to comply with the provisions of this Decree by Law, including the controls stipulated in Article (5). These measures include the Pseudonymisation Mechanism.
 71 | 3.	Apply appropriate technical and organizational measures with respect to automatic settings, to ensure that the processing of Personal Data is limited to the purpose for which it is intended. Such obligation shall apply to the volume and type of Personal Data collected, the type of processing which will be carried out, the period of storage and accessibility of such data.
 72 |  
 73 | 4.	Maintain a special record for Personal Data, provided that such record shall include the data of both the Controller and the Data Protection Officer, a description of the categories of Personal Data, details of the persons authorized to access the Personal Data, processing times, limitations and scope, the mechanism for erasing, modifying or processing Personal Data, the purpose of processing, any data related to the cross-border movement and processing of such data, and the technical and organizational measures related to information security and processing The Controller shall submit such record to the Bureau whenever requested to do so.
 74 | 5.	Appoint the Processor which has sufficient guarantees to implement technical and organizational measures in a manner which ensures that the processing meets the processing requirements, rules and controls stipulated in this Decree by Law, its Executive Regulations and the decisions issued to implement the same.
 75 | 6.	Provide the Bureau, pursuant to a decision made by the competent judicial authority, with any information it requests in implementation of its powers stipulated in this Decree by Law and its Executive Regulations.
 76 | 7.	Any other obligations set out in the Executive Regulations of this Decree by Law.
 77 | 
 78 | Article (8)
 79 | The Processor's General Obligations
 80 | The Processor shall abide by the following:
 81 | 1.	Carry out the processing in accordance with the instructions of the Controller and contracts and agreements concluded between them, which specify in particular the scope, subject, purpose, nature and type of Personal Data, and the category of the Data Subject.
 82 |  
 83 | 2.	Apply the appropriate technical and organizational procedures and measures to protect Personal Data at the design stage, whether during the identification of the means of processing or during the processing, taking into account the cost of implementing such procedures and the nature, scope and purposes of processing.
 84 | 3.	Carry out the processing according to the purpose and the period specified for it. If the processing exceeds the specified period, the Processor shall so notify the Controller to authorize it to extend such period or give appropriate instructions.
 85 | 4.	Erase data after the expiry of the processing period or upon handing it over to the Controller.
 86 | 5.	Avoid doing anything which would disclose Personal Data or results of processing, except in cases authorized by the law.
 87 | 6.	Protect and secure data processing, the electronic media and devices used in processing and the Personal Data they contain.
 88 | 7.	Maintain a special record of Personal Data which is processed on behalf of the Controller, provided that such record includes the data of the Controller, the Processor and the Data Protection Officer and a description of the categories of Personal Data they have, data of the persons authorized to access Personal Data, processing times, restrictions and scope, the mechanism of erasing, modifying or processing Personal Data, the purpose of processing, any data related to the cross-border movement and processing of such data and the technical and organizational measures related to information security and processing operations, provided that the Processor submits such record to the Bureau whenever it is requested to do so.
 89 | 8.	Provide all means to prove its commitment to the implementation of provisions of this Decree by Law when so requested by the Controller or the Bureau.
 90 |  
 91 | 9.	Carry out processing in accordance with rules, conditions and controls specified in this Decree by Law and its Executive Regulations, or pursuant to which instructions are issued by the Bureau.
 92 | 10.	In the event that more than one Processor participates in processing data, the processing shall be carried out in accordance with a written contract or agreement in which they clearly define their obligations, responsibilities and roles with regard to processing, otherwise they shall be deemed jointly responsible for the obligations and responsibilities contained in this Decree by Law and its Executive Regulations.
 93 | 11.	The Executive Regulations of this Decree by Law shall specify the procedures, controls, conditions, and technical standards related to such obligations.
 94 | 
 95 | Article (9)
 96 | Reporting Personal Data Breach
 97 | 1.	In addition to the obligations of the Controller stipulated in this Decree by Law, the Controller shall, at the time it becomes aware of the existence of any breach or violation of Personal Data of the Data Subject that would prejudice the privacy, confidentiality and security of data, notify the Bureau of such breach or violation and the investigation rights within the period and in accordance with the measures and requirements set by the Executive Regulations of this Decree by Law, provided that the reporting is accompanied by the following data and documents:
 98 | a.	A description of the nature of the breach or violation, its form, causes, approximate number and records.
 99 | b.	Details of the appointed Data Protection Officer.
100 |  
101 | c.	Potential and expected effects of the breach or violation.
102 | d.	Corrective measures and actions taken or suggested by it to confront such violation and reduce its negative impacts.
103 | e.	Documents of the violation and corrective actions taken by it.
104 | f.	Any other requirements required by the Bureau
105 | 2.	In all cases, the Controller shall notify the Data Subject in the event that the violation or breach would prejudice the privacy and confidentiality of the security of his/her Personal Data within the period and in accordance with the measures and requirements set by the Executive Regulations of this Decree by Law. It shall inform him/her of the measures taken by it.
106 | 3.	If the Processor becomes aware of any breach of Personal Data, it shall notify the Controller of such breach as soon as it becomes aware of the same. the Controller shall in turn inform the Bureau in accordance with Clause (1) of this Article.
107 | 4.	After receiving the notification from the Controller, the Bureau shall verify the reasons for the violation to ensure the integrity of the security measures taken, and impose the administrative penalties referred to in Article (26) of this Decree by Law in the event that a violation of its provisions and decisions issued in implementation of it is proven against the Controller or the Processor.
108 | 
109 | Article (10)
110 | Appointing Data Protection Officer
111 | 1.	The Controller and Processor shall appoint a Data Protection Officer, who has sufficient skills and knowledge of the Personal Data Protection Law, in any of the following cases:
112 |  
113 | a.	If processing would cause a high-level risk to the confidentiality and privacy of the Personal Data of the Data Subject as a result of adopting new technologies or with regard to the volume of data.
114 | b.	If processing would involve a systematic and comprehensive assessment of Sensitive Personal Data, including Profiling and Automated Processing.
115 | c.	If processing would be carried out on a large volume of Sensitive Personal Data.
116 | 2.	The Data Protection Officer may be an employer of the Controller or the Processor or authorized by them, whether inside or outside the State.
117 | 3.	The Controller or the Processor shall specify the contact details of the Data Protection Officer and notify the Bureau of the same.
118 | 4.	The Executive Regulations of this Decree by Law shall specify the types of technologies and criteria for determining the volume of data required in accordance with this Article.
119 | 
120 | Article (11)
121 | Roles of Data Protection Officer
122 | 1.	The Data Protection Officer shall ensure the extent of compliance of the Controller or the Processor with the application of provisions of this Decree by Law, its Executive Regulations and instructions issued by the Bureau. The Data Protection Officer shall, in particular, undertake the following tasks and powers:
123 | b. Verifying the quality and correctness of the procedures in place at the Controller and the Processor.
124 | b.	Receiving requests and complaints related to Personal Data in accordance with provisions of this Decree-Law and its Executive Regulations.
125 |  
126 | c.	Providing technical advice on evaluation procedures and periodic examination of personal data protection systems and intrusion prevention systems at the Controller and Processor, documenting the results of such evaluation and providing appropriate recommendations in this regard, including risk assessment procedures.
127 | d.	Acting as a link between the Controller or the Processor, as the case may be, and the Bureau regarding the application of personal data processing provisions stipulated in this Decree by Law.
128 | e.	Any other tasks or powers which are determined in accordance with the Executive Regulations of this Decree by Law.
129 | 2.	The Data Protection Officer shall maintain the confidentiality of information and data it receives in implementation of its duties and powers in accordance with provisions of this Decree by Law and its Executive Regulations and in accordance with the legislations in force in the State.
130 | 
131 | Article (12)
132 | Duties of the controller and the processor towards the Data Protection Officer
133 | 1.	The Controller and the Processor shall provide all means to ensure that the Data Protection Officer performs the duties and tasks assigned to it as stipulated in Article (11) of this Decree by Law in the required manner. In particular, this shall include the following:
134 | a.	Ensure that the Data Protection Officer is appropriately and timely involved in all matters relating to the protection of Personal Data.
135 | b.	Ensure that the Data Protection Officer is provided with all the necessary resources and the necessary support to carry out the tasks assigned to it.
136 |  
137 | c.	Not to terminate the Data Protection Officer services or impose any disciplinary penalty for a reason related to the performance of its duties in accordance with the provisions of this Decree by Law.
138 | d.	Ensure that the Data Protection Officer is not charged with duties which contradict its duties under this Law.
139 | 2.	The Data Subject may communicate directly with the Data Protection Officer about all matters relating to his/ her personal data processing to enable him/ her to exercise his/ her rights in accordance with the provisions of this Decree by Law.
140 | 
141 | Article (13)
142 | Right to Receive Information
143 | 1.	The Data Subject has the right, by submitting a request to the Controller without any consideration, to obtain the following information:
144 | a.	The types of its Personal Data that are being processed.
145 | b.	Purposes of processing.
146 | c.	Decisions made based on automated processing, including profiling.
147 | d.	The targeted sectors or establishments with whom its personal data will be shared from inside and outside the State.
148 | e.	Controls and standards for the period of storage and preservation of his/ her personal data.
149 | f.	Procedures for correcting, erasing or limiting processing and objection to his/ her personal data.
150 | g.	Protection measures for cross-border processing carried out in accordance with Articles
151 |  
152 | (22) and (23) of this By-Law.
153 | h.	Actions to be taken in the event of a breach or misuse of his/ her Personal Data, especially if the breach or misuse has a direct and serious threat to the privacy and confidentiality of his/her Personal Data.
154 | i.	How to submit complaints to the Bureau.
155 | 2.	In all cases, the Controller shall, before starting the processing, provide the Data Subject with the information stipulated in paragraphs (b), (d) and (g) of Paragraph (1) of this Article.
156 | 3.	The Controller may reject the Data Subject's request to obtain the information mentioned in Paragraph (1) of this Article, if the following is established:
157 | a.	The request is not related to the information referred to in Paragraph (1) of this Article, or it is excessively repetitive.
158 | b.	The request conflicts with judicial procedures or investigations conducted by competent authorities.
159 | c.	The request may negatively affect the efforts of the Controller to protect information security.
160 | d.	The request affects the privacy and confidentiality of Personal Data of third parties.
161 | 
162 | Article (14)
163 | Right to Request Transfer of Personal Data
164 | 1.	The Data Subject shall have the right to receive his/her personal data that has been provided to the Controller for processing, in an orderly and machine-readable manner, whenever the processing is based on the consent of the Data Subject, or it is necessary for the implementation of a contractual obligation, and it is carried out by automated means.
165 |  
166 | 2.	The Data Subject shall have the right to request the transfer of its Personal data to another Controller whenever it is technically feasible.
167 | 
168 | Article (15)
169 | Right to correction or erasure of Personal Data
170 | 1.	The Data Subject shall have the right to request the correction of his/her inaccurate Personal data, or request to complete the data held by the Controller without undue delay
171 | 2.	Without prejudice to the legislations in force in the State and what is required for the public interest, the Data Subject shall have the right to request erasure of his/ her Personal Data held by the Controller in any of the following cases:
172 | a.	His/her Personal Data is no longer necessary for the purposes for which it is collected or processed.
173 | b.	Withdrawal of the consent of Data Subject on which the processing is based.
174 | c.	The Data Subject's objection to the processing, or the absence of legitimate reasons for the Controller to continue the processing.
175 | d.	The Personal Data is processed in violation of the provisions of this Decree by Law and the applicable legislations, and the erasure process is necessary to comply with the legislations and approved standards in force in this regard.
176 | 3.	As an exception to what is stated in Paragraph (2) of this Article, the Data Subject is not entitled to request erasure of his/ her Personal Data held by the Controller in the following cases:
177 | a.	If the request is related to the erasure of his/her Personal Data related to public health in private facilities.
178 |  
179 | b.	If the request affects the investigation procedures and claiming and defending rights.
180 | c.	If the request contradicts other legislations to which the Controller is subject.
181 | d.	Any other cases determined by the Executive Regulation of this Decree by Law.
182 | 
183 | Article (16)
184 | Right to Restrict Processing
185 | 1.	The Data Subject shall have the right to oblige the Controller to restrict and stop processing in any of the following cases:
186 | a.	The Data Subject's objection to the accuracy of the Personal Data, in which case the processing shall be restricted for a specific period to allow the Controller to verify the data accuracy.
187 | b.	The Data Subject's objection to the processing of his/ her Personal Data in violation of the agreed-upon purposes.
188 | c.	The processing is carried out in violation of the provisions of this Decree by Law and the applicable legislations.
189 | 2.	The Data Subject shall have the right to request the Controller to continue to keep his/ her Personal Data after the completion of the processing purposes when such data is necessary to complete procedures related to claiming or defending rights and lawsuits.
190 | 3.	Notwithstanding what is stated in Paragraph (1) of this Article, the Controller may proceed with the processing of the Personal Data of the Data Subject without his/ her consent in any of the following cases:
191 | a.	If the processing is limited to storing Personal Data.
192 | b.	If the processing is necessary to pursue any of the procedures related to claiming or
193 |  
194 | defending rights and lawsuits or related to judicial proceedings.
195 | c.	If the processing is necessary to protect the rights of third parties.
196 | d.	If the processing is necessary to protect the public interest.
197 | 4.	In all cases, the Controller, if it lifts the restriction stipulated in this Article, shall notify the Data Subject of the same.
198 | 
199 | Article (17)
200 | Right to Stop Processing
201 | The Data Subject shall have the right to object to the processing of his/her Personal Data and stop it in any of the following cases:
202 | 1.	If the processing is intended for the purposes of direct marketing, including profiling related to direct marketing.
203 | 2.	If the processing is intended for the purposes of conducting statistical surveys, unless the processing is necessary to serve the public interest.
204 | 3.	If the processing is carried out in violation of Article (5) of this Decree by Law.
205 | 
206 | Article (18)
207 | Right to Processing and Automated Processing
208 | 1.	The Data Subject shall have the right to object to any decisions resulting from automated processing, including profiling, particularly those decisions which have legal impact on or adversely affect the Data Subject.
209 | 2.	Notwithstanding Paragraph 1 of this Article, the Data Subject may not object to the decisions resulting from automated processing in the following cases:
210 |  
211 | a.	If the automated processing is agreed upon under the contract made between the Data Subject and the Controller.
212 | b.	If the automated processing is required under other legislations which are applicable in the State.
213 | c.	If the Data Subject gives prior consent to the automated processing as set out in Article
214 | (6) of this Decree by Law.
215 | 3.	The Controller shall adopt appropriate measures to protect the privacy and confidentiality of the Data Subject's Personal Data in the cases referred to in Paragraph 2 of this article and shall not cause any prejudice to the Data Subject's rights.
216 | 4.	The Controller shall include the human element in reviewing automated processing decisions at the request of the Data Subject.
217 | 
218 | Article (19) Contacting the Controller
219 | The Controller shall provide clear and appropriate ways for the Data Subject to contact the Controller to request any of the rights set forth in this Decree by Law.
220 | 
221 | Article (20) Personal Data Security
222 | 1.	The Controller and the Processor shall develop and take appropriate technical and regulatory measures to ensure the highest standard of information security that is suitable for the risks related to data processing in accordance with the best international practices and standards. This shall include the following:
223 |  
224 | a.	Encryption of Personal Data and the application of Pseudonymisation.
225 | b.	Applying measures which ensure the continuous confidentiality, safety, accuracy and flexibility of data processing systems and services.
226 | c.	Applying measures which ensure timely retrieval of and access to Personal Data in case of any actual or technical failure.
227 | d.	Applying measures which ensure a seamless testing and evaluation of the effectiveness of the technical and regulatory measures to ensure the security of processing.
228 | 2.	When evaluating the information security level as set out in Paragraph1 of this Article, the following shall be observed:
229 | a.	Data processing risks, including damage, loss, accidental or illegal change and disclosure of or access to the Personal Data, whether being transferred, stored or processing.
230 | b.	The costs of data processing, and its nature, scope and purposes, in addition to potential risks impacting the confidentiality and privacy of the Data Subject's Personal Data.
231 | 
232 | Article 21
233 | Assessment of the Impact of Personal Data Protection
234 | 1.	Taking into account the nature, scope and purposes of data processing, the Controller shall, before carrying out the processing, evaluate the impact of the proposed processing operations on the protection of Personal Data, when using any of the modern technologies that would pose a high risk to the privacy and confidentiality of the Data Subject's Personal Data.
235 | 2.	The assessment of the impact provided for in Paragraph (1) of this Article shall be required in the following cases:
236 |  
237 | a.	If the processing includes a systematic and comprehensive assessment of the personal aspects of the Data Subject, using automated processing, including profiling, having legal consequences or serious impact on the Data Subject.
238 | b.	If processing would be carried out on a large volume of Sensitive Personal Data.
239 | 3.	The assessment stipulated in Paragraph (1) of this Article shall include, at a minimum, the following:
240 | a.	Clear and systematic explanation of the suggested processing operations for the protection of Personal Data and the purpose of processing.
241 | b.	Evaluation of how necessary the processing operations are and how they are suitable for the purpose of processing.
242 | c.	Evaluation of potential risks related to the privacy and confidentiality of the Data Subject's Personal Data.
243 | d.	The suggested procedures and measures aimed at reducing the potential risks related to the protection of Personal Data.
244 | 4.	The Controller may carry out one evaluation of a set of processing operations which have similar nature and risks.
245 | 5.	The Controller shall coordinate with the Data Protection Officer upon evaluating the impact of the protection of Personal Data.
246 | 6.	The Bureau shall prepare a list of processing operation types which do not require evaluation of the impact of the protection of Personal Data. The Bureau shall publish such list on its website.
247 | 7.	The Controller shall review the evaluation results on a regular basis to make sure that the processing is being carried out in accordance with the evaluation in case the processing risks
248 |  
249 | level changes.
250 | 
251 | Article (22)
252 | Cross-Border Transfer and Sharing of Personal Data for Processing Purposes if a Proper Protection Level is Available
253 | Personal Data may be transferred to outside of the State in the following cases approved by the Bureau:
254 | 1.	The State or Province to which the Personal Data is transferred shall have legislations addressing Personal Data Protection. This includes most significant provisions, measures, controls, stipulations and rules related to the protection of the privacy and confidentiality of the Date Subject's Personal Data, and his/her ability to exercise their legal rights. The State or the Province shall also have a judicial o regulatory authority imposing appropriate measures against the Controller or the Processor.
255 | 2.	If the State joins a bilateral or multilateral agreement related to the protection of Personal Data concluded with countries to which the Personal Data is transferred.
256 | 
257 | Article (23)
258 | Cross-Border Transfer and Sharing of Personal Data for Processing Purposes if a Proper Protection Level is not Available
259 | 1.	Notwithstanding Article (22) of this Decree by Law, Personal Data may be transferred to outside the State in the following cases:
260 | a.	Companies, operating in countries where there are no laws for Data Protection, may transfer data under a contract or agreement obligating the companies in such countries
261 |  
262 | to adopt measures, controls and requirements set out in this Decree by Law, in addition to provisions forcing the Controller or the Processor to adopt appropriate measures which are imposed by a judicial or regulatory authority in such countries as set out in the contract.
263 | b.	If there is an explicit consent granted by the Data Subject to transfer his/her Personal Data outside the State, provided that such transfer shall not contradict the public or security interest of the State.
264 | c.	If the transfer is necessary to fulfil obligations and establish rights before judicial entities, exercise or defend the same.
265 | d.	If the transfer is necessary to sign or implement a contract made between the Controller and the Data Subject, or between the Controller and third parties to serve the interest of the Data Subject.
266 | e.	If the transfer is necessary to implement an action related to an international judicial cooperation.
267 | f.	If the transfer is necessary to protect the public interest.
268 | 2.	The Executive Regulations of this Decree by Law set forth the controls and stipulations referred to in Paragraphs (1) of this Article, which should be observed during the transfer of data outside the State.
269 | 
270 | Article (24) Complaints
271 | 1.	The Data Subject shall have the right to submit complaints to the Bureau if he/she believes that there is a violation of this Decree by Law or that the Controller or the Processor is
272 |  
273 | processing his/ her Personal Data in violation of the rules and procedures set by the Bureau in this regard.
274 | 2.	The Bureau shall receive complaints from the Data Subject in accordance with Paragraph (1) of this Article and shall examine such complaints in coordination with the Controller and the Processor.
275 | 3.	The Bureau shall impose the administrative penalties referred to in Article (26) of this Decree by Law if it is proven that the Controller or the Processor violates its provisions, or the decisions issued in implementation of the same.
276 | 
277 | Article (25)
278 | Grievance against the Bureau's Decisions
279 | Any stakeholder may submit a written grievance to the General Director of the Bureau against any decision or administrative penalty or any other action taken by the Bureau against such stakeholder within (30) thirty days as of the date on which a notice of such administrative decision or penalty is given. Additionally, deciding upon such complaint shall be made within
280 | (30) thirty days as of the date on which the complaint is submitted.
281 | It is not permissible to challenge any decision issued by the Bureau in implementation of the provisions of this Decree by Law before submitting a grievance against the same. The Executive Regulations of this Decree by Law set out the procedures for submitting a grievance and deciding thereupon.
282 | 
283 | Article (26) Administrative Penalties
284 |  
285 | The Council of Ministers, based upon a suggestion from the General Director of the Bureau, shall issue a decision to limit the actions which constitute a violation of this Decree by Law and its Executive Regulations, including administrative penalties to be imposed.
286 | 
287 | Article (27) Authorization
288 | The Council of Ministers, based upon a suggestion from the General Director of the Bureau, may authorize any competent local government authority within the scope of its local competence, to exercise some of the Bureau' powers set out in this Decree by Law.
289 | 
290 | Article (28)
291 | The Executive Regulation
292 | The Council of Ministers, based upon a suggestion from the General Director of the Bureau, shall issue the Executive Regulations of this Decree by Law within six (6) months as of the date on which the Decree by Law is promulgated.
293 | 
294 | Article (29) Regularisation
295 | The Controller and the Processor shall regularize their status in compliance with the provisions of this Decree by Law within a period of no more than six (6) months as of the date on which its Executive Regulations are issued. The Council of Ministers may extend such period for another similar period.
296 |  
297 | Article (30) Repeals
298 | Any provision that violates or contradicts the provisions of this Decree by Law shall be repealed.
299 | 
300 | Article (31)
301 | Publication & Enforcement of this Decree by Law
302 | This Decree by Law shall by published in the Official Gazette and shall come into force as of 02 January 2022.
303 | 


--------------------------------------------------------------------------------
/kb/youth_safety/AU_CWSA_2024:
--------------------------------------------------------------------------------
  1 | Child Wellbeing and Safety Act
  2 | 2024 Revised Edition
  3 | Place: Australia
  4 | Effective Date: 2024-07-01
  5 | 
  6 | 
  7 | Part 5A—Reportable conduct scheme
  8 | 16A	Definition
  9 | In this Part and Part 5B— entity means an entity to which the reportable conduct scheme applies.
 10 | 16B	Principles 
 11 | 	(1)	The reportable conduct scheme is based on the fundamental principles that—
 12 | 	(a)	the protection of children is the paramount consideration in the context of child abuse or employee misconduct involving a child;
 13 | 	(b)	criminal conduct or suspected criminal conduct should be reported to the police;
 14 | 	(c)	a police investigation into the subject matter of a reportable allegation has priority and, unless the investigation may otherwise be conducted under any other Act, an investigation under the reportable conduct scheme must be suspended or must not be commenced until the police advise or agree that it may proceed;
 15 | 	(d)	the Commission and others involved in the reportable conduct scheme should work in collaboration to ensure the fair, effective and timely investigation of reportable allegations;
 16 | 	(e)	employees who are the subject of reportable allegations are entitled to receive natural justice in investigations into their conduct;
 17 | 
 18 | 	(f)	regulators have specific knowledge of the roles of the entities or the professional responsibilities of the employees they regulate and, if their functions permit, play an important role in the investigation of reportable allegations;
 19 | 	(g)	information should be shared during and after the conclusion of an investigation into a reportable allegation;
 20 | (h)	after the conclusion of an investigation into a reportable allegation, the Commission may share information with the Department of Justice and Community Safety for the purpose of a WWC check.
 21 | 	(2)	The Commission should educate and guide—
 22 | 	(a)	entities in order to improve their ability to identify reportable conduct and to report and investigate reportable allegations; and
 23 | 	(b)	regulators in order to promote compliance by entities with the reportable conduct scheme
 24 | 16C	Application of reportable conduct scheme
 25 | The reportable conduct scheme does not apply to an entity that does not exercise care, supervision or authority over children, whether as part of its primary functions or otherwise.
 26 | 16D	Administration, oversight and monitoring of scheme
 27 | The Commission is responsible for administering, overseeing and monitoring the reportable conduct scheme.
 28 | 	16E	Avoiding unnecessary duplication
 29 | The Commission must liaise with regulators—
 30 | 	(a)	to avoid unnecessary duplication in the oversight of the investigation of reportable allegations; and
 31 | (b)	to share information and provide advice and guidance about the protection of children.
 32 | 
 33 | 	16F	Objectives of Commission under this Part and Part 5B
 34 | Without limiting any other provision, the objectives of the Commission under this Part and Part 5B are—
 35 | 	(a)	to improve the ability of entities to identify reportable conduct and to report and investigate reportable allegations; and
 36 | 	(b)	to ensure that reportable allegations are properly investigated; and
 37 | 	(c)	to protect children by working with entities, regulators and other relevant bodies to prevent reportable conduct from occurring in entities; and
 38 | (d)	to share information with the Secretary to the Department of Justice and Community Safety for the purpose of WWC checks.
 39 | 
 40 | 	16G	Functions of Commission under this Part and Part 5B
 41 | The Commission has the following functions in relation to the reportable conduct scheme—
 42 | 	(a)	to educate and provide advice to entities in order to assist them to identify reportable conduct and to report and investigate reportable allegations;
 43 | 	(b)	to educate and provide advice to regulators to promote compliance by entities with the reportable conduct scheme;
 44 | 	(c)	to oversee the investigation of reportable allegations;
 45 | 
 46 | (d)	to investigate reportable allegations if—
 47 | 	(i)	it considers it to be in the public interest to do so; or
 48 | 	(ii)	an entity or regulator will not, or is unable to, investigate or engage an independent person or body to investigate;
 49 | 	(e)	if it considers it to be in the public interest to do so, to investigate whether reportable allegations have been inappropriately handled or responded to by an entity or a regulator; 
 50 | 	(f)	to make recommendations to entities to address the findings of investigations referred to in paragraph (d) or (e);
 51 | 
 52 | 	(g)	to exchange information (including the findings of investigations into reportable allegations and the reasons for those findings) with Victoria Police, regulators, entities and the Secretary to the Department of Justice and Community Safety;
 53 | 	(h)	to monitor the compliance of entities with the reportable conduct scheme;
 54 | (ha)	in relation to section 16M—
 55 | 	(i)	to monitor and enforce compliance with section 16M(1) by the head of an entity; and 
 56 | 	(ii)	to investigate contraventions of section 16M(4);
 57 | 	(i)	to report to the Minister and to Parliament on trends in the reporting and investigation of reportable allegations and the results of those investigations;
 58 | (j)	to perform any other function conferred on the Commission under this Part or Part 5B
 59 | 16H	Powers of the Commission
 60 | The Commission has all the powers that are necessary or convenient to perform its functions under this Part and Part 5B.
 61 | 16I	Exemption by Commission
 62 | 	(1)	The Commission, in accordance with the regulations, if any, may exempt the head of an entity or a class of entities from—
 63 | 	(a)	the requirements of section 16M in respect of a class or kind of conduct; or
 64 | 	(b)	the requirement under section 16M(1)(b) to provide information to the Commission in respect of a class or kind of conduct.
 65 | 	(2)	The Commission may give an exemption under subsection (1) if the Commission considers that—
 66 | 	(a)	the entity is competent to investigate, without the oversight of the Commission, a reportable allegation in respect of the class or kind of conduct to which the exemption relates; and
 67 | 	(b)	the entity has demonstrated competence in responding to reportable allegations in respect of that class or kind of conduct.
 68 | 	(3)	The Commission must—
 69 | 	(a)	notify the entity concerned of an exemption under subsection (1); and
 70 | 	(b)	publish the exemption on the Commission's website.
 71 | (4)	The head of an entity exempted under subsection (1)(b), or a regulator of the entity, that conducts an investigation into conduct of a class or kind exempted under subsection (1)(b) must inform the Commission of the findings, the reasons for the findings and the action taken in response to those findings as soon as practicable after the conclusion of the investigation or within a period agreed with the Commission.
 72 | 
 73 | 	16J	Exemption from whole of scheme
 74 | 	(1)	The regulations may prescribe an entity or a class of entities to be exempt from the reportable conduct scheme.
 75 | 16J	Exemption from whole of scheme
 76 | 	(1)	The regulations may prescribe an entity or a class of entities to be exempt from the reportable conduct scheme.
 77 | 
 78 | 
 79 | 	(2)	The regulations may prescribe a part of an entity, or a part of a class of entities, to be exempt from the reportable conduct scheme.
 80 | 	16K	Head of entity to have systems in place
 81 | 	(1)	The head of an entity must ensure that the entity has in place—
 82 | 	(a)	a system for preventing the commission of reportable conduct by an employee of the entity within the course of the person's employment; and
 83 | 	(b)	a system for enabling any person, including an employee of the entity, to notify the head of the entity of a reportable allegation of which the person becomes aware; and
 84 | 	(c)	a system for enabling any person, including an employee of the entity, to notify the Commission of a reportable allegation involving the head of the entity of which the person becomes aware; and
 85 | (d)	a system for investigating and responding to a reportable allegation against an employee of the entity.
 86 | 	(2)	If requested in writing by the Commission, an entity must provide to the Commission any information about a system referred to in subsection (1).
 87 | 	(3)	The Commission, after consulting with the relevant regulator, may make recommendations for action to be taken by an entity and may provide the entity with any necessary information relating to the recommendations if a reasonable concern with a system referred to in subsection (1) is identified.
 88 | 16L	Disclosure to Commission of reportable allegation
 89 | Any person may disclose a reportable allegation to the Commission.
 90 | 	16M	Head of entity to notify Commission of reportable allegation
 91 | 	(1)	If the head of an entity becomes aware of a reportable allegation against an employee of the entity, the head must notify the Commission in writing of the following—
 92 | 	(a)	within 3 business days after becoming aware of the reportable allegation—
 93 | 	(i)	that a reportable allegation has been made against an employee of the entity; and
 94 | 	(ii)	the name (including any former name and alias, if known) and date of birth, if known, of the employee concerned; and
 95 | 	(iii)	whether Victoria Police has been contacted about the reportable allegation; and
 96 | (iv)	the name, address and telephone number of the entity; and
 97 | 	(v)	the name of the head of the entity; and
 98 | 	(b)	as soon as practicable and within 30 days after becoming aware of the reportable allegation—
 99 | 	(i)	detailed information about the reportable allegation; and
100 | 	(ii)	whether or not the entity proposes to take any disciplinary or other action in relation to the employee and the reasons why it intends to take, or not to take, that action; and
101 | 	(iii)	any written submissions made to the head of the entity concerning the reportable allegation that the employee wished to have considered in determining what, if any, disciplinary or other action should be taken in relation to the employee.
102 | 	(2)	This section does not apply to the head of an entity, or an entity belonging to a class of entities, that the Commission has exempted under section 16I(1)(a) in respect of a class or kind or conduct that is the subject of the reportable allegation.
103 | 	(3)	Subsection (1)(b) does not apply to the head of an entity, or an entity belonging to a class of entities, that the Commission has exempted under section 16I(1)(b) in respect of a class or kind of conduct that is the subject of the reportable allegation.
104 | (4)	The head of an entity must not fail, without reasonable excuse, to comply with subsection (1).
105 | Penalty:	10 penalty units.
106 | 	(5)	It is a defence to a charge for an offence against subsection (4) for the person charged to prove that the person honestly and reasonably believed that another person had notified the Commission of the reportable allegation in accordance with subsection (1). 
107 | 16N	Head of entity to respond to reportable allegation
108 | 	(1)	As soon as practicable after the head of an entity becomes aware of a reportable allegation against an employee of the entity, the head must—
109 | 	(a)	investigate the reportable allegation or permit a regulator, or an independent investigator engaged by the entity or regulator, to investigate the reportable allegation; and
110 | 	(b)	inform the Commission of the identity of the body or person who will conduct the investigation.
111 | 	(2)	If the Commission requests in writing that the head of the entity provide to the Commission information or documents relating to a reportable allegation or an investigation, the head of the entity must comply with the request.
112 | 	(3)	As soon as practicable after an investigation has concluded, the head of the entity must give the Commission—
113 | 	(a)	a copy of the findings of the investigation and the reasons for those findings; and
114 | (b)	details of any disciplinary or other action that the entity proposes to take in relation to the employee and the reasons for that action; and
115 | (c)	if the entity does not propose to take any disciplinary or other action in relation to the employee, the reasons why no action is to be taken.
116 | 


--------------------------------------------------------------------------------
/kb/youth_safety/CA_SB976.txt:
--------------------------------------------------------------------------------
 1 | The California Senate 2024/()/()/
 2 | Senate Bill No. 976
 3 | CHAPTER 321
 4 | An act to add Chapter 24 (commencing with Section 27000) to Division 20 of the Health and Safety Code, relating to youth addiction.
 5 | 
 6 | LEGISLATIVE COUNSEL'S DIGEST
 7 | SB 976, Skinner. Protecting Our Kids from Social Media Addiction Act.
 8 | 
 9 | Existing law, the California Age-Appropriate Design Code Act, requires, beginning July 1, 2024, a business that provides an online service, product, or feature likely to be accessed by children to comply with certain requirements. The act requires the business to complete a data protection impact assessment addressing whether the design could harm children and whether and how the online product, service, or feature uses system design features to increase, sustain, or extend use by children, including the automatic playing of media, rewards for time spent, and notifications. Existing law prohibits the business from using the personal information of any child in a way that it knows, or has reason to know, is materially detrimental to the physical health, mental health, or well-being of a child.
10 | 
11 | Existing law, the Privacy Rights for California Minors in the Digital World, prohibits an operator of an internet website, online service, online application, or mobile application from specified conduct when minors are involved, including the marketing or advertising of alcoholic beverages, firearms, or certain other products or services. Existing law sets forth other related protections for minors, including under the California Consumer Privacy Act of 2018 and the California Privacy Rights Act of 2020.
12 | 
13 | This bill, the Protecting Our Kids from Social Media Addiction Act, would make it unlawful for the operator of an addictive internet-based service or application, as defined, to provide an addictive feed to a user, unless
14 | 


--------------------------------------------------------------------------------
/kb/youth_safety/EU_DSA_A28.txt:
--------------------------------------------------------------------------------
 1 | EU Digital Services Act 2022/()/()/
 2 | Article 28, Online Protection of Minors - the Digital Services Act (DSA)
 3 | 
 4 | 1. Providers of online platforms accessible to minors shall put in place appropriate and proportionate measures to ensure a high level of privacy, safety, and security of minors, on their service.
 5 | 
 6 | 2. Providers of online platforms shall not present advertisements on their interface based on profiling as defined in Article 4, point (4), of Regulation (EU) 2016/679 using personal data of the recipient of the service when they are aware with reasonable certainty that the recipient of the service is a minor.
 7 | 
 8 | 3. Compliance with the obligations set out in this Article shall not oblige providers of online platforms to process additional personal data in order to assess whether the recipient of the service is a minor.
 9 | 
10 | 4. The Commission, after consulting the Board, may issue guidelines to assist providers of online platforms in the application of paragraph 1.
11 | 


--------------------------------------------------------------------------------
/kb/youth_safety/FL_HB3.txt:
--------------------------------------------------------------------------------
 1 | The Florida Senate 2024/()/()/
 2 | 2024 Summary of Legislation Passed
 3 | Committee on Judiciary
 4 | CS/CS/HB 3 — Online Protections for Minors
 5 | By Judiciary Committee; Regulatory Reform & Economic Development Subcommittee; and
 6 | Reps. Tramont, Overdorf, Sirois, McFarland, Rayner, and others (CS/SB 1792 by Judiciary
 7 | Committee and Senators Grall and Garcia)
 8 | 
 9 | The bill requires regulated social media platforms to prohibit minors younger than 14 years of age from entering into contracts with social media platforms to become account holders. It allows minors who are 14 or 15 years of age to become account holders, but only with the consent of a parent or guardian. Social media platforms are regulated under the bill if they:
10 | - Allow users to upload content or view the content or activity of other users.
11 | - Satisfy certain daily active user metrics identified in the bill.
12 | - Employ algorithms that analyze user data or information on users to select content for users.
13 | - Have certain addictive features.
14 | 
15 | With respect to all accounts belonging to minors younger than 14, and to those accounts belonging to minors who are 14 or 15 years of age but for whom parents or guardians have not provided consent, the bill requires regulated social media platforms to terminate them and also allows the account holders or their parents or guardians to terminate them. Social media platforms must permanently delete all personal information held by them relating to terminated accounts unless otherwise required by law to maintain the personal information.
16 | 
17 | The bill also requires regulated commercial entities that knowingly and intentionally publish or distribute material harmful to minors on a website or application to prohibit access to such material by any person younger than 18 years of age, if their website or application contains a substantial portion of material that is harmful to minors. Such commercial entities must verify, using either an anonymous or standard age verification method, that the age of a person attempting to access the material harmful to minors satisfies the bill’s age requirements. If an anonymous age verification method is used, the verification must be conducted by a nongovernmental, independent third party organized under the laws of a state of the U.S. Any information used to verify age must be deleted once the age is verified.
18 | 
19 | Regulated social media platforms, commercial entities, and third parties performing age verification for commercial entities that knowingly and recklessly violate the bill’s requirements are subject to enforcement under the Florida Deceptive and Unfair Trade Practices Act. The Department of Legal Affairs may collect civil penalties of up to $50,000 per violation, reasonable attorney fees and court costs, and (under certain conditions) punitive damages. Account holders who are minors may also pursue up to $10,000 in damages.
20 | 


--------------------------------------------------------------------------------
/kb/youth_safety/INDIA_Juvenile_2015.txt:
--------------------------------------------------------------------------------
 1 | The Juvenile Justice (Care and Protection of Children) Act 2015/()/()/
 2 | Place: India
 3 | 
 4 | CHAPTER II
 5 | GENERAL PRINCIPLES OF CARE AND PROTECTION OF CHILDREN
 6 | 
 7 | Section 74.   Prohibition on disclosure of identity of children.
 8 | (1) No report in any newspaper, magazine, news-sheet or audio-visual media or other forms of communication regarding any inquiry or investigation or judicial procedure, shall disclose the name, address or school or any other particular, which may lead to the identification of a child in conflict with law or a child in need of care and protection or a child victim or witness of a crime, involved in such matter, under any other law for the time being in force, nor shall the picture of any such child be published:
 9 | Provided that for reasons to be recorded in writing, the Board or Committee, as the case may be, holding the inquiry may permit such disclosure, if in its opinion such disclosure is in the best interest of the child.
10 | (2) The Police shall not disclose any record of the child for the purpose of character certificate or otherwise 1[in the pending case or in the case which] has been closed or disposed of.
11 | (3) Any person contravening the provisions of sub-section (1) shall be punishable with imprisonment for a term which may extend to six months or fine which may extend to two lakh rupees or both.
12 | Section 75.   Punishment for cruelty to child.
13 | Whoever, having the actual charge of, or control over, a child, assaults, abandons, abuses, exposes or wilfully neglects the child or causes or procures the child to be assaulted, abandoned, abused, exposed or neglected in a manner likely to cause such child unnecessary mental or physical suffering, shall be punishable with imprisonment for a term which may extend to three years or with fine of one lakh rupees or with both:
14 | Provided that in case it is found that such abandonment of the child by the biological parents is due to circumstances beyond their control, it shall be presumed that such abandonment is not wilful and the penal provisions of this section shall not apply in such cases:
15 | Provided further that if such offence is committed by any person employed by or managing an organisation, which is entrusted with the care and protection of the child, he shall be punished with rigorous imprisonment which may extend up to five years, and fine which may extend up to five lakhs rupees:
16 | Provided also that on account of the aforesaid cruelty, if the child is physically incapacitated or develops a mental illness or is rendered mentally unfit to perform regular tasks or has risk to life or limb, such person shall be punishable with rigorous imprisonment, not less than three years but which may be extended up to ten years and shall also be liable to fine of five lakhs rupees.
17 | Section 76.   Employment of child for begging.
18 | (1) Whoever employs or uses any child for the purpose of begging or causes any child to beg shall be punishable with imprisonment for a term which may extend to five years and shall also be liable to fine of one lakh rupees:
19 | Provided that, if for the purpose of begging, the person amputates or maims the child, he shall be punishable with rigorous imprisonment for a term not less than seven years which may extend up to ten years, and shall also be liable to fine of five lakh rupees.
20 | (2) Whoever, having the actual charge of, or control over the child, abets the commission of an offence under sub-section (1), shall be punishable with the same punishment as provided for in subsection (1) and such person shall be considered to be unfit under sub-clause (v) of clause (14) of section 2:
21 | Provided that the said child, shall not be considered a child in conflict with law under any circumstances, and shall be removed from the charge or control of such guardian or custodian and produced before the Committee for appropriate rehabilitation.
22 | Section 77.   Penalty for giving intoxicating liquor or narcotic drug or psychotropic substance to a child.
23 | Whoever gives, or causes to be given, to any child any intoxicating liquor or any narcotic drug or tobacco products or psychotropic substance, except on the order of a duly qualified medical practitioner, shall be punishable with rigorous imprisonment for a term which may extend to seven years and shall also be liable to a fine which may extend up to one lakh rupees.
24 | Section 78.   Using a child for vending, peddling, carrying, supplying or smuggling any intoxicating liquor, narcotic drug or psychotropic substance.
25 | Whoever uses a child, for vending, peddling, carrying, supplying or smuggling any intoxicating liquor, narcotic drug or psychotropic substance, shall be liable for rigorous imprisonment for a term which may extend to seven years and shall also be liable to a fine up to one lakh rupees.
26 | Section 79.   Exploitation of a child employee.
27 | Notwithstanding anything contained in any law for the time being in force, whoever ostensibly engages a child and keeps him in bondage for the purpose of employment or withholds his earnings or uses such earning for his own purposes shall be punishable with rigorous imprisonment for a term which may extend to five years and shall also be liable to fine of one lakh rupees.
28 | Explanation.--For the purposes of this section, the term "employment" shall also include selling goods and services, and entertainment in public places for economic gain.
29 | Section 80.   Punitive measures for adoption without following prescribed procedures.
30 | If any person or organisation offers or gives or receives, any orphan, abandoned or surrendered child, for the purpose of adoption without following the provisions or procedures as provided in this Act, such person or organisation shall be punishable with imprisonment of either description for a term which may extend upto three years, or with fine of one lakh rupees, or with both:
31 | Provided in case where the offence is committed by a recognised adoption agency, in addition to the above punishment awarded to the persons in-charge of, and responsible for the conduct of the day-to-day affairs of the adoption agency, the registration of such agency under section 41 and its recognition under section 65 shall also be withdrawn for a minimum period of one year.
32 | Section 81.   Sale and procurement of children for any purpose.
33 | Any person who sells or buys a child for any purpose shall be punishable with rigorous imprisonment for a term which may extend to five years and shall also be liable to fine of one lakh rupees:
34 | Provided that where such offence is committed by a person having actual charge of the child, including employees of a hospital or nursing home or maternity home, the term of imprisonment shall not be less than three years and may extend up to seven years.
35 | Section 82.   Corporal punishment.
36 | (1) Any person in-charge of or employed in a child care institution, who subjects a child to corporal punishment with the aim of disciplining the child, shall be liable, on the first conviction, to a fine of ten thousand rupees and for every subsequent offence, shall be liable for imprisonment which may extend to three months or fine or with both.
37 | (2) If a person employed in an institution referred to in sub-section (1), is convicted of an offence under that sub-section, such person shall also be liable for dismissal from service, and shall also be debarred from working directly with children thereafter.
38 | (3) In case, where any corporal punishment is reported in an institution referred to in sub-section (1) and the management of such institution does not cooperate with any inquiry or comply with the orders of the Committee or the Board or court or State Government, the person in-charge of the management of the institution shall be liable for punishment with imprisonment for a term not less than three years and shall also be liable to fine which may extend to one lakh rupees.
39 | Section 83.   Use of child by militant groups or other adults.
40 | (1) Any non-State, self-styled militant group or outfit declared as such by the Central Government, if recruits or uses any child for any purpose, shall be liable for rigorous imprisonment for a term which may extend to seven years and shall also be liable to fine of five lakh rupees.
41 | (2) Any adult or an adult group uses children for illegal activities either individually or as a gang shall be liable for rigorous imprisonment for a term which may extend to seven years and shall also be liable to fine of five lakh rupees.
42 | Section 84.   Kidnapping and abduction of child.
43 | For the purposes of this Act, the provisions of sections 359 to 369 of the Indian Penal Code (45 of 1860), shall mutatis mutandis apply to a child or a minor who is under the age of eighteen years and all the provisions shall be construed accordingly.
44 | 


--------------------------------------------------------------------------------
/kb/youth_safety/uae_wadeema_2024.txt:
--------------------------------------------------------------------------------
  1 | Federal Law on Child Rights Law 2024/()/()
  2 | Place: United Arab Emirate
  3 | 
  4 | Chapter One: General Provisions
  5 | Article (1) Definitions
  6 | In implementation of the provisions of this Law, the following words and expressions shall bear the meanings assigned thereto herein respectively, unless the context otherwise indicates:
  7 | State: The United Arab Emirates. 
  8 | Ministry: Ministry of Social Affairs. 
  9 | Minister: Minister of Social Affairs. 
 10 | Competent Authorities: Federal authorities concerned with child affairs. 
 11 | Concerned Bodies: Local authorities concerned with child affairs. 
 12 | Child: Each and every human being born alive and below 18 years of age. 
 13 | Custodian: The person legally in charge of the child or who is entrusted with the child's custody. 
 14 | Foster Family: The alternative family entrusted with the custody and care of the child. 
 15 | Child Protection Specialist: The person licenses and assigned by the competent authority or the concerned bodies, as the case may be, to preserve the child's rights and protect him within his respective competence, as mentioned in this Law. 
 16 | Child Abuse: Each and every act or omission that would harm the child in a manner that prevents his upbringing and growth in a proper safe and healthy manner. 
 17 | Child Neglect: Failure of parents or custodians to take the measures necessary for preserving the child's life and physical, psychological, mental and moral wellness from danger and protecting his various rights. 
 18 | Violence Against Child: The deliberate use of force against any child by any individual or community that inflicts actual harm to the child's health or growth or life. 
 19 | Child's Best Interest: Is making the child's interest above any consideration and of priority and preference in all conditions, regardless of the interests of the other parties. 
 20 | Child Pornography: Production, display, publication, acquisition or exchange of a photo, film or drawing via a means of communication, social media, or any other means in which the child appears in an actual and real or fictional or simulated disgraceful situation in the sexual act or show. 
 21 | 
 22 | Article (2)
 23 | The competent authorities and bodies concerned shall secure the child's rights and preserve their best interests by developing necessary policies and programs that would:
 24 | 1. Preserve the child's right to life, survival and growth, provide all the opportunities necessary to facilitate that and enjoy a decent and safe life.
 25 | 2. Ensure the child's right to social care and protect them from violence, neglect, exploitation and abuse.
 26 | 3. Instill human values in the child and promote a culture of human fraternity within them.
 27 | 4. Educate and empower families to perform their fundamental role in raising the child with virtuous morals and teach, guide and provide the child with the necessary care to ensure proper development to the fullest.
 28 | 5. Ensure that the child's parents or custodian fulfill their responsibilities toward the child, maintain their rights, protect them from abuse and neglect, and educate them about the danger of committing crimes, especially cybercrimes or being exploited through cybercrimes.
 29 | 6. Educate the child about their rights and make them aware of the same in a language and manner that is easy for them to understand, particularly matters related to their protection from abuse and neglect, using appropriate means.
 30 | 7. Engage the child in community life activities according to their age, maturity level and abilities, so they grow up with qualities such as love for work, initiative, licit gain and self-reliance.
 31 | 8. Secure the rights prescribed for the child in this Law, without prejudice to the public order or public morals.
 32 |  
 33 | 
 34 | Article (3)
 35 | This Law shall ensure granting the child all the rights determined thereunder and under other legislation in force in the State and protecting him without discrimination due to his race, gender, country, religion, social status or disability.
 36 | 
 37 | Article (4)
 38 | 1. The natural family shall be the best environment to raise a child which existence, maintenance and protection is ensured by the State in order to achieve the child's rights and best interests. When necessary such family shall be replaced by an alternative family.
 39 | 2. Child protection and best interests shall have priority in all decisions and procedures taken relevant to him. The competent authorities and concerned bodies shall attempt to achieve that through taking the necessary procedures, including:
 40 | a. Ensuring fulfillment of the child's moral, psychological and physical needs in accordance with his age, health and family environment, particularly his right to guardianship;
 41 | b. Giving the child the priority of protection, care, relief and guidance in emergencies, disasters and armed conflicts and from any crime committed against him;
 42 | c. Protecting the child from psychological harm in all phases of collection of evidence, investigation and trial, whether he is a litigant or witness.
 43 | 
 44 | Article (5)
 45 | The child's privacy shall be respected in accordance with the public order and morals together with taking into account the rights and responsibilities the legal custodian.
 46 | 
 47 | Article (6)
 48 | The responsible concerned bodies shall implement the policies and programs developed by the competent authorities in all fields relevant to the child.
 49 | 
 50 | Chapter Two: Basic Rights
 51 | Article (7)
 52 | 1. The child shall have the right to life and safety.
 53 | 2. The State shall ensure the child's growth, development and protection in accordance with the Law.
 54 | 
 55 | Article (8)
 56 | The child shall be entitled, since his birth, to have a name not involving contempt or prejudice to his dignity or contradicting with the religious beliefs and customs.
 57 | 
 58 | Article (9)
 59 | The child shall be immediately registered in the birth register immediately after his birth in accordance with the legal system determined in this regard.
 60 | 
 61 | Article (10)
 62 | The child shall have a nationality in accordance with the provisions of the laws in force in the State.
 63 | 
 64 | Article (11)
 65 | 1. The child shall be entitled to be traced back to his legal parents in accordance with the laws in force in the State.
 66 | 2. The child's parents or legal guardians shall extract the papers that prove the child's birth, nationality in addition to all of the other identification papers in accordance with the laws in force in the State.
 67 | 
 68 | Article (12)
 69 | 1. The child shall be entitled to express his opinions freely pursuant to his age and maturity in consistency with the public order and morals and the laws in force in the State.
 70 | 2. The child shall be provided with the opportunity necessary to express his opinion with respect to the measures taken in his regard in accordance with the laws in force.
 71 | 
 72 | Article (13)
 73 | The child may not be exposed to any arbitrary intervention or illegal procedure in his life, family, home or correspondence. In addition, neither the child's honor nor reputation may be prejudiced. The State shall ensure child protection from all child pornography in accordance with the legislation in force.
 74 | 
 75 | Article (14)
 76 | The competent authorities and concerned bodies shall:
 77 | 1. Prohibit employment of children prior to reaching 15 years of age; and
 78 | 2. Prohibit the economic exploitation and recruitment in any works that expose children to danger, whether by virtue of their nature or for the circumstance of performance thereof.
 79 | The Executive Regulations of the Law and the Labor Law regulate the conditions and bases of child employment.
 80 | 
 81 | Chapter Three: Family Rights
 82 | Article (15)
 83 | 1. The child's parents and the like and custodians shall provide him with the requirements of family safety with the atmosphere of a family with strong and close relations.
 84 | 2. The child's custodian shall be entrusted with the responsibilities and duties vested in him with respect to educating, protecting, guiding and upbringing the child in the best way.
 85 | 
 86 | Article (16)
 87 | Subject to the laws in force, the child shall be entitled to be introduced to his natural family and parents and receive their care and to have personal relations and direct contact with both of them.
 88 | 
 89 | Article (17)
 90 | The child shall be entitled to custody, feeding, alimony and protecting himself, body, religion and property in accordance with the laws in force in the state.
 91 | 
 92 | Chapter Four: Health Rights
 93 | Article (18)
 94 | The child shall be entitled to receive health services in accordance with the laws and regulations of health care in force in the State.
 95 | 
 96 | Article (19)
 97 | The State shall develop it capabilities in the field of protective, therapeutic and psychological health care and health guidance relevant to child health, nutrition and protection.
 98 | 
 99 | Article (20)
100 | The competent authorities and concerned bodies shall provide health care to mothers before and after giving birth in accordance with the legislation in force.
101 | In addition, the competent authorities and concerned bodies shall take the possible measures to:
102 | 1. Protect the child from the risks and harms of environmental pollution and combat the same;
103 | 2. Play a constructive and effective role in awareness in the fields of child health and nutrition, advantages of breastfeeding, protection from disease and accidents and disadvantages of smoking; and develop the policies and programs necessary to improve health media in this regard;
104 | 3. The competent authorities and concerned bodies shall take the measures necessary to protect and children from the use of narcotics, intoxicants and doping substances in addition to all substances that affect the mind or from contribution in production, trading or promotion thereof;
105 | 4. Support the school health system in order to play its role in the field of protection, treatment and health guidance;
106 | 5. Protect from infection with infectious, dangerous and chronic diseases and provide the necessary vaccinations and immunizations;
107 | 6. Develop programs for training of workers in the maternal and child health sector and prepare them to achieve the objectives of this Law;
108 | 7. Provide psychological care in a manner that ensures the child's mental, emotional, social and linguistic growth; and
109 | 8. Take the measures necessary for early examination of children in order to diagnose disabilities and chronic diseases.
110 | 
111 | Article (21)
112 | No person may:
113 | 1. Sell or attempt to sell tobacco or its products to a child. The seller shall be entitled to request from the buyer to provide a proof of reaching 18 years of age;
114 | 2. Smoke in public and private means of transportation and indoors in case of the presence of a child;
115 | 3. Sell or attempt to sell intoxicants to a child in addition to any other substances that endangers his health which are determined under a Cabinet Resolution;
116 | 4. Import or trade in substances violating the specifications approved in the State for children's food, accessories, food or health or hormonal supplements, or toys.
117 | 
118 | Chapter Five: Social Rights
119 | Article (22)
120 | The State shall provide a standard of living appropriate for the physical, mental, psychological and social growth of the child in accordance with the laws in force.
121 | 
122 | Article (23)
123 | Children who neither have a competent sustainer nor a source of income shall be entitled to receive the State's aid in accordance with the laws in force.
124 | 
125 | Article (24)
126 | Subject to the laws of personal status and children of unknown parentage, the child who is permanently ore temporary deprived of his natural family environment shall be entitled to alternative care through:
127 | 1. A foster family;
128 | 2. Public or private social care institutions in case of the lack of a foster family.
129 | 
130 | Chapter Six: Cultural Rights
131 | Article (25)
132 | The child shall be entitled to acquire knowledge and means of innovation and creation. To this end, the child may participate in recreational, cultural, artistic and scientific programs that consistent with his age and the public order and morals. The competent authorities and concerned bodies shall develop the programs necessary for this purpose.
133 | 
134 | Article (26)
135 | The publication, display, trading, possession or production of any visual, audio or printed work or games intended for children that arouse the child's sexual instincts or urge him to commit the behaviors violating the public order and morals or encourage on deviance.
136 | 
137 | Article (27)
138 | It is prohibited to bring children into, or facilitate their entry into the places specified by the Executive Regulations of this Law. It is also prohibited to bring children into or facilitate their entry into other places in violation of the controls set by the Executive Regulations for entry into some other places.
139 | 
140 | Article (28)
141 | The managers of cinemas displaying movies and TV channels and the other similar places referred to in the preceding Paragraph shall announce prohibition of children's entrance in a prominent place in accordance with the provisions of the Executive Regulations hereof and the other regulations in force.
142 | 
143 | Article (29)
144 | Communications companies and internet providers shall notify the competent authorities or concerned bodies of any child pornography exchanged through websites. The same shall also provide necessary information and data on the persons, bodies or websites that exchange such materials or intend to mislead children.
145 | 
146 | Article (30)
147 | The State shall establish councils, associations, clubs and centers for children that are competent with developing the children's cultural, artistic, scientific, physical and other aspects.
148 | 
149 | Chapter Seven: Educational Rights
150 | Article (31)
151 | Each and every child shall be entitled to education. In addition, the State shall attempt to achieve equality of opportunities available to all children in accordance with the laws in force.
152 | 
153 | Article (32)
154 | In the field of education, the State shall take the following measures:
155 | 1. Prevent children's school dropout;
156 | 2. Promote the participation of children and their parents in the decisions relevant to children ;
157 | 3. Prohibition of all kinds of violence in educational institutions and preserving the child's dignity upon taking decisions or developing programs;
158 | 4. Develop the educational system including kindergartens in order to achieve its purpose to develop each child's mental, physical, emotional, social and ethical aspects;
159 | 5. Develop specific and organized programs for reporting and filing complaints in order to ensure investigation of acts and irregularities violating the educational rights set forth in this Law in the manner specified by the Executive Regulations.
160 | 
161 | Chapter Eight: Right to Protection
162 | Article (33)
163 | The following shall be particularly considered to be threatening the child's physical, psychological, ethical or mental safety and requires his right to protection:
164 | 1. Loss of parents and staying without a sustainer or guardian;
165 | 2.Suffering from rejection, neglect and displacement;
166 | 3. Obvious and continuous delinquency in education and care;
167 | 4. Frequent child abuse;
168 | 5. Sexual abuse or exploitation;
169 | 6. Exploitation by illegal organizations and in organized crimes, e.g.: introduction of intolerance and hatred or urging the child to commit acts of violence and intimidation;
170 | 7. Exposure to mendicancy or economic exploitation;
171 | 8. Failure of parents or custodians to protect or educate the child;
172 | 9. Exposure to kidnapping, sale or human trafficking for any purpose or exploitation in any form;
173 | 10. Experiencing mental or psychological disability that affects his cognition.
174 | 
175 | Article (34)
176 | The child's mental, psychological, physical or ethical safety may not be prejudiced whether by abandonment by the custodian or leaving him in a care facility or institution without a valid reason, rejecting the child by the custodian or refraining from treating him and taking care of his affairs.
177 | 
178 | Article (35)
179 | The child's custodian may neither expose him to abandonment, displacement or neglect, frequently leave him without supervision or control, quit guiding the child, refrain from taking care of his affairs, abstain from enrolling the child in an educational institution, nor leave him in case of school dropout without a valid reason during the stage of compulsory education.
180 | 
181 | Article (36)
182 | It is prohibited to expose the child to torture or physical assault or perform any act that would compromise the child's emotional, psychological, mental or moral safety.
183 | 
184 | Article (37)
185 | The following acts shall be prohibited:
186 | 1. Using or exploiting the child in filming, recording or producing any pornography;
187 | 2. Producing, publishing, distributing or facilitating children's access to pornography by any means;
188 | 3. Possessing child pornography regardless of the intent to distribute;
189 | 4. Downloading, uploading or sending any child pornography via the internet or any other communications or information technology means;
190 | 5. Custodian's contribution to child's participation in production or filming child pornography or any other sexual acts or allowing the child to do so or help him in any of such acts;
191 | 6. Direct or indirect sexual exploitation of the child by exposing or preparing him for acts of prostitution and debauchery whether or not against a consideration.
192 | 
193 | Article (38)
194 | The following acts shall be prohibited:
195 | 1. Using the child in mendicancy;
196 | 2. Recruiting the child in illegal circumstances; and
197 | 3. Engaging the child in a work that hinders his education or endangers his health or his physical, psychological, ethical or mental safety.
198 | 
199 | Chapter Nine: Protection Mechanisms
200 | Article (39)
201 | 1.The competent authorities and concerned bodies shall work in coordination with the Ministry on establishing child protection units aiming at developing and implementing child protection mechanisms and measures stipulated herein; and
202 | 2.The Executive Regulations of this Law shall determine the following:
203 |    a.Competences of the child protection units and the operating mechanisms thereof; and
204 |    b.Requirements to be met by the child protection specialist.
205 | 
206 | Article (40)
207 | The child protection specialist shall take the oath before exercising his functions and shall be competent to perform the following:
208 | 1. Preventive intervention in all cases in which the child's health and physical, psychological, ethical or mental safety are threatened or endangered; and
209 | 2. Therapeutic intervention in all cases of abuse, exploitation and negligence and all cases stipulated in Article (33) hereof.
210 |  
211 | 
212 | Article (41)
213 | The child protection specialist shall, when performing his functions, be entitled to have the following powers:
214 | 1. Collect evidence regarding the incidents that are the subject of the report and attend the investigative hearings and trials if necessary;
215 | 2. Enter by himself or accompanied by whoever he needs into any place where the child is present with the permission of the owner of that place and he shall present a card proving his capacity;
216 | 3. Take the preventative measures appropriate for the child in a manner determined by the Executive Regulations hereof; and
217 | 4. Utilize the social researches to reach a determination of the truth of the child's situation.
218 | 
219 | Article (42)
220 | 1. Anyone may inform the child protection specialist or the child protection units if there is a threat to the child's safety or physical, psychological, ethical or mental health; and
221 | 2. The reporting shall be mandatory for the custodians, physicians and social workers or those who are entrusted with the protection, care or education of the child.
222 | 
223 | Article (43)
224 | Whoever attains the age of majority shall help any child who asks him to report the competent authorities or concerned bodies of his suffering or the suffering of any of his brothers or any other child in any of the cases stipulated in Article (33) hereof.
225 | 
226 | Article (44)
227 | The identity of the reporter shall not be disclosed unless his approval is obtained. The disclosure of the identities of all parties to the incident and the witnesses in child abuse or maltreatment actions when using the information contained in the analyses or media reports or the publication of any material that could lead to the disclosure of his identity shall be prohibited.
228 | 
229 | Article (45)
230 | The concerned bodies and competent authorities shall provide protection to the witnesses in all stages of the criminal action.
231 | 
232 | Chapter Ten: Protection Measures
233 | Article (46)
234 | Subject to the provisions of Articles (47) and (51) hereof, the child protection specialist shall, in agreement with the custodian, take all the necessary measures if there is a threat to the child's safety or physical, psychological, ethical or mental health in a manner determined by the Executive Regulations hereof.
235 | 
236 | Article (47)
237 | Subject to the provision of Article (51) hereof, the child protection specialist shall submit the following proposals to the child's parents or custodian if it is proved to him that there is a threat to the child's safety or physical, psychological, ethical or mental health:
238 | 1. Keeping the child with his family, subject to:
239 |    a. The commitment of the child's parents or custodian, in writing, to take the measures required for removing the threat to the child and to keep the child under the periodic oversight of the child protection specialist;
240 |    b. The regulation of the methods of social intervention by the concerned bodies and competent authorities, as the case may be, concerned with providing the necessary social services and assistance to the child and his family; and
241 |   c. Taking the measures necessary for preventing any contact between the child and the threat to his safety or physical, psychological, ethical or mental health.
242 | 2. Placing the child temporarily in an alternative family, an association, or an appropriate social, educational or health institution, whether public or private, in accordance with the controls determined by the Executive Regulations hereof.
243 | 
244 | Article (48)
245 | If the child protection specialist achieves the appropriate measures in a form of agreement, such agreement shall be written, read and signed by the various parties including the child who reached 13 years of age.
246 | The child protection specialist shall periodically follow up the results of the taken agreement measures taken and shall decide, when necessary, to amend the same in a manner that ensures, as much as possible, keeping the child in his family environment.
247 | 
248 | Article (49)
249 | The child protection specialist shall inform the child's parents or custodian and the child who reached 13 years of age of their right to refuse the proposed measure.
250 | 
251 | Article (50)
252 | 1. The child protection specialist shall refer the matter to the body for which he works to take the necessary measure in the following two cases:
253 |    a. Failure to achieve an agreement within fifteen days as of the date of informing him of the case; and
254 |    b. Violating the agreement by the child's parent, custodian or the 13-year-old child.
255 | 2. The body for which the child protection specialist works shall take all actions necessary for referring the matter to the public prosecution.
256 | 
257 | Article (50) BIS
258 | 1. If an act attributed to the child's parents, one of them or custodian constitutes a violation of Article (27) or any of Articles from (34) to (38) of this Law, or a violation of the agreement stipulated in Article (48) of this Law, the Public Prosecution, after consulting a child protection specialist or at the request of the relevant authority, may order the violator to undergo one or more rehabilitation and guidance programs.
259 | 2. A grievance against the Public Prosecution's order shall be filed to the competent court, within (15) fifteen days from the date of being aware of it. The court shall promptly decide on the matter, and its decision shall be final and non-appealable.
260 | 3. The Public Prosecution may order the completion of the program if it finds that the person under the program is complying with the program, based on a report issued by the center indicating that such person will unlikely commit any act in the future that would violate the provisions of Article (27) or any of the provisions of Articles from (34) to (38) of this Law.
261 | 
262 | Article (51)
263 | 1. Subject to the provisions of Articles (33), (34), (35), (36), (37) and (38), each and every act or omission that would threaten the child's life, safety or physical, psychological, ethical or mental health in a manner that cannot be prevented by the time;
264 | 2. Taking into account the privacy of accommodations, the child protection specialist shall initiate, in the event of significant harm to the child or a threat thereto and before obtaining a judicial permit, to get the child out of the place where he exists and put him in a safe place under his own responsibility. The child protection specialist may ask for the assistance of the public authorities.
265 | 3. The child protection specialist shall obtain a court order to continue to take the measures stipulated in Clause (2) of this Article within (24) hours as of the time to get the child out of the place. The competent judge shall issue his decision within (24) hours as of the date of submitting the request.
266 | 
267 | Article (52)
268 | The child protection specialists determined by a resolution issued by the Minister of Justice shall, in agreement with the Minister and the concerned bodies, have the capacity of judicial officers to prove the occurrence of any violation to the provisions of this Law and the Regulations and Resolutions issued in implementation thereof.
269 | 
270 | Article (53)
271 | The public prosecution and judicial bodies shall ask for the assistance of the child protection specialist in the investigations and trials in which the child is present.
272 | 
273 | Article (54)
274 | 1. Whoever has been convicted of a sexual abuse crime or pornography crime shall be prohibited from engaging in any work or job that allows them directly communicate or interact with children even if such person has been rehabilitated;
275 | 2. The judge shall issue a judgment preventing the person who has been convicted of a sexual abuse crime committed a against a child from residing in the region where the abused child resides five kilometers away from the child's residence; and
276 | 3. In all cases, the person sentenced to confinement or imprisonment in a sexual abuse crime committed against a child shall not be released unless psychological tests and examinations are conducted to him before the termination of his confinement or imprisonment to ensure that he will not pose any danger to the society. In case of proving that, the court shall order to put him at a therapeutic shelter after the termination of his confinement or imprisonment. The Executive Regulations hereof shall determine the regulation of putting the sentenced person at a therapeutic shelter and the procedures for hearing the release requests.
277 | 
278 | Article (55)
279 | A register shall be established in the Ministry in coordination with the competent authorities to record all child abuse cases. Everything recorded in this register shall be confidential and shall not be accessed without the permission of the public prosecution or the competent court as the case may be.
280 | 
281 | Article (56)
282 | The competent authorities and concerned bodies shall, in coordination with the Ministry:
283 | 1. Specify the special engineering standards and specifications, construction laws and safety and security requirements that protect the child from any kind of harm. The Executive Regulations hereof shall determine the controls required for the implementation of these standards and specifications and the exceptions thereto;
284 | 2. Establish the controls and procedures required for the protection of the child's safety in public and recreational places and in public transport and the Executive Regulations shall determine such required controls and measures; and
285 | 3. The provisions of Clauses (1) and (2) of this Article shall apply to the public and private sectors, save for what is excluded therefrom by a special provision in the Executive Regulations.
286 | 
287 | Article (57)
288 | The competent authorities and concerned bodies shall take the following measures:
289 | 1. Ensure the product safety in order not to threaten the child's rights contained herein and establish the advertising controls that comply with the child's right to health, survival and growth;
290 | 2. Control the commercial activities so as to ensure that the child is not exposed to any environmental risks or harms.
291 | 
292 | Article (58)
293 | The competent authorities and concerned bodies shall ensure the child protection from the dangers of the traffic accidents in accordance with the provisions of the traffic law, as amended especially the following:
294 | 1. Prohibiting the sitting of children who are under the age of 10 in the front seats of the vehicles of all kinds; and
295 | 2. Establishing controls with regard to the children's use of bicycles.
296 | 
297 | Article (59)
298 | Subject to the provisions of the personal status law, the competent court shall, before issuing a judgment on the child custody, request the submission of a detailed report about the social, psychological and health status and the criminal status of the person applying for custody or the person for whom custody will be ordered by the court or the submission of a statement that he did not commit any crime outside the State. The Executive Regulations shall determine the procedures for preparing these report and statement.
299 | 
300 | Chapter Eleven: Penalties
301 | Article (60)
302 | Whoever violates any provision of Clause (2) of Article (11), Articles (28) and (34), Article (35) or Clause (2) of Article (42) hereof shall be punished by imprisonment or a fine of not less than (AED 5,000) UAE Dirhams five thousand.
303 | 
304 | Article (61)
305 | Whoever commits one of the following acts shall be punished by a fine of not less than (AED 5,000) UAE Dirhams five thousand and not more than (AED 50,000) UAE Dirhams fifty thousand:
306 | 1. Violating the provision of Article (43) hereof;
307 | 2. Preventing the child protection specialist from performing his functions or hindering his work; and
308 | 3. Giving false information or deliberately hiding the truth of the child's situation.
309 | 
310 | Article (62)
311 | Whoever violates any of the provisions of Clause (2) of Article (21) hereof shall be punished by a fine of not less than (AED 5,000) UAE Dirhams five thousand.
312 | 
313 | Article (63)
314 | Whoever violates any of the provisions of Clauses (1) and (3) of Article (21) hereof shall be punished by a term of imprisonment of not less than three months and/or a fine of not less than (AED 15,000) UAE Dirhams fifteen thousand.
315 | 
316 | Article (64)
317 | Whoever violates any of the provisions of Clause (4) of Article (21) or Article (29) hereof shall be punished by a term of imprisonment of not less than six months and/or a fine of not less than (AED 100,000) UAE Dirhams one hundred thousand and not more than (AED 1,000,000) UAE Dirhams one million.
318 | 
319 | Article (65)
320 | Whoever violates any of the provisions of Clauses (1), (2), (5) and (6) of Article (37) hereof shall be punished by a term of imprisonment of not less than ten years.
321 | 
322 | Article (66)
323 | Whoever violates any of the provisions of Article (26) or Clauses (3) and (4) of Article (37) hereof shall be punished by a term of imprisonment of not less than one year and/or a fine of not less than (AED 100,000) UAE Dirhams one hundred thousand and not more than (AED 400,000) UAE Dirhams four hundred thousand.
324 | 
325 | Article (67)
326 | Whoever violates any of the provisions of Article (27) hereof shall be punished by a term of imprisonment of not less than one month and not more than six months and by a fine of not less than (AED 5,000) UAE Dirhams five thousand.
327 | 
328 | Article (68)
329 | Whoever violates any of the provisions of Article (14) or the provision of Article (38) hereof shall be punished by imprisonment and/or a fine of not less than (AED 20,000) UAE Dirhams twenty thousand.
330 | If the work endangers the life or physical, mental or ethical safety of the child who is under the age of 15, this shall be deemed an aggravating circumstance.
331 | 
332 | Article (69)
333 | 1. A person who violates the provision of Article (36) of this Law shall be punished by imprisonment for a term not less than one year and/or a fine of not less than (AED 50,000) fifty thousand dirhams and not more than (AED 100,000) one hundred thousand dirhams.
334 | 2. If the act is attributed to the child's parents, one of them or the child's custodian, the court may, instead of imposing the penalty specified in paragraph (1) of this Article, rule, for a period determined by the court, to impose one or more of the following measures:
335 |     a. Performing a community service.
336 |     b. Placement in a therapeutic shelter.
337 |     c. Subjecting them to one or more rehabilitation and guidance programs.
338 |     d. Suspension of custody of the child, taking into account the provisions of applicable laws regarding custody of a person.
339 | If the court rules to suspend custody, it shall refer the matter to the competent family court to appoint a custodian for the child, pursuant to the legislation in force in the State.
340 | 3. The Executive Regulations of this Law shall set a mechanism for implementing rehabilitation and guidance programs, including conditions for rehabilitation and guidance centers and a mechanism for assessment of persons under the program and their compliance with the program.
341 |  
342 | 
343 | Article (69) BIS
344 | A person who refuses to undergo the rehabilitation and guidance program outlined in Article (50-bis) of this Law, or fails to comply with it according to the Executive Regulations of this Law, shall be punished by imprisonment for a term not less than (3) three months and/or a fine of not less than (AED 10,000) ten thousand dirhams and not more than (AED 100,000) one hundred thousand dirhams.
345 | 
346 | Article (70)
347 | In implementation of the provisions of this Law, the offender's claim that he did not know the age of the victim shall be disregarded.
348 | 
349 | Article (71)
350 | The penalties stipulated herein shall not prejudice any more severe penalty stipulated in any other law.
351 | 
352 | Chapter Twelve: Final Provisions
353 | Article (72)
354 | The provisions of this Law shall not prejudice any rights or aspects of protection that ensure that the child enjoys all rights and public freedoms in a better way and the aspects of protection and care stipulated in any other applicable legislation.
355 | 
356 | Article (73)
357 | The Cabinet shall, upon the proposal of the Minister, issue the Executive Regulations hereof within six months as of the date of publication in the Official Gazette.
358 | 
359 | Article (74)
360 | Any provision inconsistent with or repugnant to the provisions hereof is hereby repealed.
361 | 
362 | Article (75)
363 | This Law shall be published in the Official Gazette and shall enter into force three months following the date of publicating thereof.
364 | 


--------------------------------------------------------------------------------
/main.py:
--------------------------------------------------------------------------------
  1 | """
  2 | pilot.py - orchestrates the end-to-end compliance workflow.
  3 | 
  4 | Assumptions made:
  5 | - Each domain agent will initialise its own vector database by calling a yet-to-be-created
  6 |   utility helper. Therefore the pilot instantiates agents without handling VDB setup.
  7 | - The query preparation step uses `enhance_query` which returns a text summary of the
  8 |   feature title and description. This text is sent to downstream agents.
  9 | - Domain agents expose `analyze_feature(prepped_query)` and return a list of chunk
 10 |   dictionaries with at least `content`, `relevance_score` and optional `citation`
 11 |   and `domain_tag` fields.
 12 | - RerankerAgent.process, VerifierAgent.process, AggregatorAgent.process and
 13 |   ClassifierAgent.classify follow the interfaces defined in their respective modules.
 14 | - Low verifier confidence triggers the HITLAgent for a possible manual override.
 15 | """
 16 | 
 17 | from __future__ import annotations
 18 | 
 19 | import asyncio
 20 | from typing import List, Type
 21 | 
 22 | from agents.youth_safety_agent import YouthSafetyAgent
 23 | # from agents.data_privacy_agent import DataPrivacyAgent
 24 | # from agents.content_moderation_agent import ContentModerationAgent
 25 | # from agents.consumer_protection_agent import ConsumerProtectionAgent
 26 | # from agents.ai_governance_agent import AIGovernanceAgent
 27 | # from agents.ip_protection_agent import IPProtectionAgent
 28 | from agents.reranker_agent import RerankerAgent
 29 | from agents.verifier_agent import VerifierAgent
 30 | from agents.hitl_agent import HITLAgent
 31 | from agents.aggregator_agent import AggregatorAgent
 32 | from agents.classifier_agent import ClassifierAgent
 33 | 
 34 | from utils.inputqueryenhancer import enhance_query
 35 | 
 36 | 
 37 | def main(feature_title: str, feature_description: str):
 38 |     """Run the full compliance workflow."""
 39 |     # 1. Query preparation
 40 |     prepped_query = enhance_query(feature_title, feature_description)
 41 |     print("Prepared query:\n", prepped_query)
 42 |     yield "Prepared query:\n" + prepped_query
 43 | 
 44 |     # 2. Initialise domain agents
 45 |     # Assumes each agent handles its own VDB initialisation internally.
 46 |     domain_agent_classes: List[Type] = [
 47 |         YouthSafetyAgent
 48 |         # DataPrivacyAgent,
 49 |         # ContentModerationAgent,
 50 |         # ConsumerProtectionAgent,
 51 |         # AIGovernanceAgent,
 52 |         # IPProtectionAgent,
 53 |     ]
 54 |     domain_agents = [cls() for cls in domain_agent_classes]
 55 | 
 56 |     # 3. Retrieve chunks from all domain agents
 57 |     all_chunks = []
 58 |     for agent in domain_agents:
 59 |         chunks = agent.analyze_feature(prepped_query)
 60 |         # Expect each agent to return: List[{"content", "relevance_score", "citation"?, "domain_tag"?}]
 61 |         print(f"{agent.name} returned {len(chunks)} chunks")
 62 |         yield f"{agent.name} returned {len(chunks)} chunks"
 63 |         all_chunks.extend(chunks)
 64 | 
 65 |     # 4. Rerank and select diverse set of chunks
 66 |     reranker = RerankerAgent()
 67 |     selected_chunks = asyncio.run(reranker.process(all_chunks, prepped_query))
 68 |     print(f"Reranker selected {len(selected_chunks)} chunks")
 69 |     yield f"Reranker selected {len(selected_chunks)} chunks"
 70 | 
 71 |     # 5. Verification for confidence score
 72 |     verifier = VerifierAgent()
 73 |     verification = verifier.process(selected_chunks, prepped_query)
 74 |     print(f"Verification confidence: {verification['confidence']:.2f}")
 75 |     yield f"Verification confidence: {verification['confidence']:.2f}"
 76 | 
 77 |     # 6. Human-in-the-loop override if confidence low
 78 |     hitl_feedback = None
 79 |     if verification["escalate"]:
 80 |         hitl_feedback = HITLAgent().process(verification, prepped_query)
 81 | 
 82 |     # 7. Aggregation of context for classification
 83 |     aggregator = AggregatorAgent()
 84 |     aggregated = aggregator.process(verification["chunks"], hitl_feedback)
 85 | 
 86 |     # 8. Final classification
 87 |     classifier = ClassifierAgent()
 88 |     result = asyncio.run(classifier.classify(aggregated, prepped_query))
 89 | 
 90 |     # 9. Output results and audit trail
 91 |     print("\n=== FINAL OUTPUT ===")
 92 |     print(f"Flag: {result['flag']}")
 93 |     print(f"Reasoning: {result['reasoning']}")
 94 |     print(f"Regulations: {result['regulations']}")
 95 |     print("Audit trail:")
 96 |     for entry in result["audit_trail"]:
 97 |         print(f"- {entry}")
 98 |         yield f"- {entry}"
 99 | 
100 | 
101 | if __name__ == "__main__":
102 |     # Example invocation; replace with real feature details
103 |     main(
104 |         feature_title="Content visibility lock with NSP for EU DSA",
105 |         feature_description="To meet the transparency expectations of the EU Digital Services Act..."
106 |     )
107 | 


--------------------------------------------------------------------------------
/requirements.txt:
--------------------------------------------------------------------------------
 1 | chromadb
 2 | langchain
 3 | langchain-core
 4 | langchain-community
 5 | langchain-huggingface
 6 | langchain-openai
 7 | nltk
 8 | numpy
 9 | openai
10 | pydantic
11 | python-dotenv
12 | rank-bm25
13 | requests
14 | # sentence-transformers


--------------------------------------------------------------------------------
/utils/__pycache__/inputqueryenhancer.cpython-311.pyc:
--------------------------------------------------------------------------------
https://raw.githubusercontent.com/finnerrrrr/Tiktok-Techjam-Geo-Compliance-Classifier-WalaWalaOokOok-/124c2ba0a405c212bed7646e88ff39925ca85feb/utils/__pycache__/inputqueryenhancer.cpython-311.pyc


--------------------------------------------------------------------------------
/utils/__pycache__/rag.cpython-311.pyc:
--------------------------------------------------------------------------------
https://raw.githubusercontent.com/finnerrrrr/Tiktok-Techjam-Geo-Compliance-Classifier-WalaWalaOokOok-/124c2ba0a405c212bed7646e88ff39925ca85feb/utils/__pycache__/rag.cpython-311.pyc


--------------------------------------------------------------------------------
/utils/__pycache__/rag.cpython-313.pyc:
--------------------------------------------------------------------------------
https://raw.githubusercontent.com/finnerrrrr/Tiktok-Techjam-Geo-Compliance-Classifier-WalaWalaOokOok-/124c2ba0a405c212bed7646e88ff39925ca85feb/utils/__pycache__/rag.cpython-313.pyc


--------------------------------------------------------------------------------
/utils/__pycache__/semanticchunker.cpython-311.pyc:
--------------------------------------------------------------------------------
https://raw.githubusercontent.com/finnerrrrr/Tiktok-Techjam-Geo-Compliance-Classifier-WalaWalaOokOok-/124c2ba0a405c212bed7646e88ff39925ca85feb/utils/__pycache__/semanticchunker.cpython-311.pyc


--------------------------------------------------------------------------------
/utils/inputqueryenhancer.py:
--------------------------------------------------------------------------------
  1 | import openai
  2 | from langchain.chat_models import init_chat_model
  3 | from langchain_core.prompts import ChatPromptTemplate
  4 | from pydantic import BaseModel, Field
  5 | 
  6 | 
  7 | class QuerySummary(BaseModel):
  8 |     title: str = Field(
  9 |         description=(
 10 |             "title of the feature as per the original input"
 11 |         )
 12 |     )
 13 |     description: str = Field(
 14 |         description=(
 15 |             "description of the feature as per the origina input"
 16 |         )
 17 |     )
 18 |     requirements: list[str] = Field(
 19 |         description=(
 20 |             "A list of strings containing requirements (methods that need to be used or things that need to be collected) "
 21 |             "for the successful implementation of the feature, followed by the reasoning for the requirement. "
 22 |             "Each item MUST be phrased as: 'The feature needs <requirement> because <reason>'."
 23 |         )
 24 |     )
 25 |     effects: list[str] = Field(
 26 |         description=(
 27 |             "A list of strings describing potential impacts on different stakeholder groups (e.g., minors, general users, "
 28 |             "content creators, advertisers, moderators). Each item MUST be phrased as: "
 29 |             "'Impact on <group>: <effect> because <reason>'. If no clear impacts are stated or minimally implied, return []."
 30 |         )
 31 |     )
 32 |     regions: list[str] = Field(
 33 |         description=(
 34 |             "A list of strings representing the geographical regions where the feature will be tested or deployed. "
 35 |             "If no regions are specified, return ['Global']."
 36 |         )
 37 |     )
 38 | 
 39 | input_query_enhancing_prompt = ChatPromptTemplate.from_messages([
 40 |     (
 41 |         "system",
 42 |         "You are an extraction assistant for a backend compliance pre-processor. "
 43 |         "Your sole job is to read a short feature title and description and return ONLY the fields "
 44 |         "defined by the QuerySummary schema provided by the caller (handled via structured output). "
 45 |         "Do not add fields, explanations, or commentary."
 46 |         "\n\n"
 47 |         "Extraction rules:\n"
 48 |         "1) requirements (list[str]): Identify concrete implementation requirements that are NECESSARY "
 49 |         "   to build or operate the feature, and give a short reason for each. "
 50 |         "   Each item MUST be phrased as: 'The feature needs <requirement> because <reason>'.\n"
 51 |         "   - Allowed examples of <requirement>: collect <data/signal>, infer <attribute>, store <logs>, "
 52 |         "     run A/B tests, deploy <model/algorithm>, maintain <data retention>, implement <age gating>, "
 53 |         "     integrate <payment/subscription>, enable <geo-handler>, display <notice/consent>, etc.\n"
 54 |         "   - Base each requirement on explicit statements or minimally necessary implications from the text. "
 55 |         "     Do NOT speculate beyond the given content.\n"
 56 |         "   - If nothing is needed beyond generic app behavior, return an empty list [].\n"
 57 |         "\n"
 58 |         "2) effects (list[str]): Describe potential impacts on different stakeholder groups ONLY when the text clearly supports them "
 59 |         "   (explicitly or via minimal, necessary implication). "
 60 |         "   - Each item MUST be phrased as: 'Impact on <group>: <effect> because <reason>'.\n"
 61 |         "   - Examples of <group>: minors, general users, content creators, advertisers, moderators, parents/guardians.\n"
 62 |         "   - Keep effects concise and tied to the described feature; do NOT infer legal outcomes.\n"
 63 |         "   - If no clear impacts are supported, return [].\n"
 64 |         "\n"
 65 |         "3) regions (list[str]): Extract any explicit geographic constraints mentioned in EITHER the title "
 66 |         "   or the description (e.g., 'California', 'EU', 'UK', 'Singapore', 'US', 'APAC'). "
 67 |         "   - Return EXACT strings as written or common short forms if unambiguous (e.g., 'California' or 'US-CA' if stated as 'California').\n"
 68 |         "   - If multiple regions are stated, include all of them in a list (deduplicate; keep order of appearance).\n"
 69 |         "   - If NO geographic scope is stated, return ['Global'].\n"
 70 |         "\n"
 71 |         "Constraints:\n"
 72 |         "- Be concise and literal; do not infer legal/compliance conclusions.\n"
 73 |         "- No hallucinations: if not clearly supported by the text, omit it.\n"
 74 |         "- Output MUST conform to the QuerySummary schema (handled by structured output)."
 75 |         "For abbreviations, use the following:"
 76 |         """
 77 |             "NR":	"Not recommended",
 78 |             "PF":	"Personalized feed",
 79 |             "GH":	"Geo-handler; a module responsible for routing features based on user region",
 80 |             "CDS":	"Compliance Detection System",
 81 |             "DRT":	"Data retention threshold; duration for which logs can be stored",
 82 |             "LCP":	"Local compliance policy",
 83 |             "Redline":	"Flag for legal review (different from its traditional business use for 'financial loss')",
 84 |             "Softblock":	"A user-level limitation applied silently without notifications",
 85 |             "Spanner":	"A synthetic name for a rule engine (not to be confused with Google Spanner)",
 86 |             "ShadowMode":	"Deploy feature in non-user-impact way to collect analytics only",
 87 |             "T5":	"Tier 5 sensitivity data; more critical than T1‚ÄìT4 in this internal taxonomy",
 88 |             "ASL":	"Age-sensitive logic",
 89 |             "Glow":	"A compliance-flagging status, internally used to indicate geo-based alerts",
 90 |             "NSP":	"Non-shareable policy (content should not be shared externally)",
 91 |             "Jellybean":	"Feature name for internal parental control system",
 92 |             "EchoTrace":	"Log tracing mode to verify compliance routing",
 93 |             "BB":	"Baseline Behavior; standard user behavior used for anomaly detection",
 94 |             "Snowcap":	"A synthetic codename for the child safety policy framework",
 95 |             "FR":	"Feature rollout status",
 96 |             "IMT":	"Internal monitoring trigger"
 97 |         """
 98 |         "Please think 1 level deeper"
 99 |     ),
100 |     (
101 |         "human",
102 |         "Feature Title: {feature_title}\n"
103 |         "Feature Description: {feature_description}\n"
104 |         "\n"
105 |         "Return ONLY the fields in the QuerySummary schema (the runtime will enforce the structure)."
106 |     )
107 | ])
108 | 
109 | def init_llm():
110 |     try:
111 |         llm = init_chat_model("gpt-5", model_provider="openai")
112 |         structured_llm = llm.with_structured_output(QuerySummary)
113 |         return structured_llm
114 |     except openai.APIError as e:
115 |         print(f"An API error occurred: {e}")
116 | 
117 | def format_query_summary(summary) -> str:
118 |     # Safeguards
119 |     title = getattr(summary, "title", "") or ""
120 |     description = getattr(summary, "description", "") or ""
121 |     requirements = getattr(summary, "requirements", None) or []
122 |     effects = getattr(summary, "effects", None) or []
123 |     regions = getattr(summary, "regions", None) or ["Global"]
124 | 
125 |     # Join list fields into human-readable text
126 |     req_text = "; ".join(requirements) if requirements else "Unspecified"
127 |     eff_text = "; ".join(effects) if effects else "Unspecified"
128 |     reg_text = "; ".join(regions) if regions else "Global"
129 | 
130 |     return (
131 |         f"Feature title: {title}\n\n"
132 |         f"Feature description: {description}\n\n"
133 |         f"Feature requirements: {req_text}\n\n"
134 |         f"Potential impact(s): {eff_text}\n\n"
135 |         f"Regions for testing/rollout of feature: {reg_text}"
136 |     )
137 | 
138 | def enhance_query(feature_title, feature_description, llm=None, as_text=True):
139 |     if not llm:
140 |         llm = init_llm()
141 |     prompt = input_query_enhancing_prompt.invoke({"feature_title": feature_title, "feature_description": feature_description})
142 |     response = llm.invoke(prompt)
143 |     
144 |     if as_text:
145 |         return format_query_summary(response)
146 |     return response


--------------------------------------------------------------------------------
/utils/rag.py:
--------------------------------------------------------------------------------
  1 | # utils/rag.py
  2 | # -*- coding: utf-8 -*-
  3 | """
  4 | RAG utility for domain agents.
  5 | 
  6 | What this module does
  7 | ---------------------
  8 | 1) Build an in-memory VDB for a given *domain directory* (e.g. "utils/consumer_protection"):
  9 |    - Iterates all `.txt` files (recursive).
 10 |    - Uses `semanticchunker.get_chunks(path)` to produce (law_name, [chunks...]).
 11 |    - Stores chunks with metadata {law_name, domain, source, chunk_number}.
 12 |    - Creates BOTH:
 13 |        • Sentence-Transformer embeddings (L2-normalized) for semantic similarity
 14 |        • BM25 index over tokenized chunk text for lexical similarity
 15 | 
 16 | 2) Execute a **hybrid search** against the VDB using a *prepped query* (string or dict):
 17 |        hybrid_score = 0.60 * semantic_cosine + 0.40 * bm25_norm
 18 |    Returns ONLY the top-5 chunks as:
 19 |        { "law_name": str, "chunk": str, "relevance_score": float, "domain": str }
 20 | 
 21 | Notes
 22 | -----
 23 | - This module is pure Python with `sentence-transformers` and `rank_bm25`.
 24 | - The "prepped query" can be a dict from your Query Prep agent:
 25 |     {
 26 |       "feature_title": "...",
 27 |       "feature_description": "...",
 28 |       "feature_requirements": "...",
 29 |       "potential_impacts": "...",
 30 |       "regions": "EU"
 31 |     }
 32 |   We combine these into one search string (light weighting).
 33 | """
 34 | 
 35 | from __future__ import annotations
 36 | 
 37 | import os
 38 | import re
 39 | import math
 40 | from dataclasses import dataclass
 41 | from typing import Any, Dict, List, Optional, Tuple, Union
 42 | 
 43 | import numpy as np
 44 | from rank_bm25 import BM25Okapi
 45 | from sentence_transformers import SentenceTransformer
 46 | 
 47 | # Import your semantic chunker (must live next to this file as utils/semanticchunker.py)
 48 | from . import semanticchunker as sc
 49 | 
 50 | 
 51 | # ---------------------------
 52 | # Small tokenizer for BM25
 53 | # ---------------------------
 54 | _TOKEN_RE = re.compile(r"[A-Za-z0-9]+", re.UNICODE)
 55 | def _tok(text: str) -> List[str]:
 56 |     return _TOKEN_RE.findall(text.lower())
 57 | 
 58 | 
 59 | # ---------------------------
 60 | # Chunk container
 61 | # ---------------------------
 62 | @dataclass
 63 | class _Chunk:
 64 |     text: str
 65 |     law_name: str
 66 |     domain: str
 67 |     source: str
 68 |     chunk_number: int
 69 | 
 70 | 
 71 | # ---------------------------
 72 | # RAG Engine
 73 | # ---------------------------
 74 | class RAGEngine:
 75 |     """
 76 |     Build & query a domain-specific VDB.
 77 | 
 78 |     Usage:
 79 |         engine = RAGEngine.from_domain_dir("utils/consumer_protection")
 80 |         results = engine.search(prepped_query, top_k=5)
 81 |         # results: List[{"law_name","chunk","relevance_score","domain"}]
 82 |     """
 83 | 
 84 |     def __init__(self, model_name: str = "sentence-transformers/all-MiniLM-L6-v2"):
 85 |         self.model_name = model_name
 86 |         self.embedder = SentenceTransformer(model_name)
 87 | 
 88 |         self.domain: str = ""                # e.g. "consumer_protection"
 89 |         self.chunks: List[_Chunk] = []       # ordered list of chunks
 90 |         self._embeddings: Optional[np.ndarray] = None   # (N, d), L2-normalized
 91 |         self._bm25: Optional[BM25Okapi] = None
 92 |         self._doc_tokens: List[List[str]] = []
 93 | 
 94 |     # ---------- Build ----------
 95 |     @classmethod
 96 |     def from_domain_dir(cls, domain_dir: str, model_name: str = "sentence-transformers/all-MiniLM-L6-v2") -> "RAGEngine":
 97 |         """
 98 |         Build an engine by scanning a directory containing `.txt` files for a specific domain.
 99 |         Recursively walks the directory tree.
100 |         """
101 |         engine = cls(model_name=model_name)
102 |         if not os.path.isdir(domain_dir):
103 |             raise FileNotFoundError(f"Domain directory not found: {domain_dir}")
104 | 
105 |         engine.domain = os.path.basename(os.path.normpath(domain_dir)) or "general"
106 | 
107 |         txt_files: List[str] = []
108 |         for root, _dirs, files in os.walk(domain_dir):
109 |             for fname in files:
110 |                 if fname.lower().endswith(".txt"):
111 |                     txt_files.append(os.path.join(root, fname))
112 | 
113 |         if not txt_files:
114 |             raise ValueError(f"No .txt files found in {domain_dir}")
115 | 
116 |         # Chunk each file with semanticchunker
117 |         for path in txt_files:
118 |             try:
119 |                 law_name, chunk_list = sc.get_chunks(path)  # returns (law_name, [chunk_str, ...])
120 |             except Exception as e:
121 |                 print(f"[RAG] Skipping {os.path.basename(path)}: {e}")
122 |                 continue
123 |             if not chunk_list:
124 |                 continue
125 | 
126 |             rel_source = os.path.relpath(path, start=domain_dir)
127 |             for i, chunk_text in enumerate(chunk_list):
128 |                 engine.chunks.append(
129 |                     _Chunk(
130 |                         text=chunk_text,
131 |                         law_name=law_name or os.path.splitext(os.path.basename(path))[0],
132 |                         domain=engine.domain,
133 |                         source=rel_source,
134 |                         chunk_number=i,
135 |                     )
136 |                 )
137 | 
138 |         if not engine.chunks:
139 |             raise ValueError(f"semanticchunker produced 0 chunks in {domain_dir}")
140 | 
141 |         # Build BM25 + embeddings
142 |         engine._doc_tokens = [_tok(c.text) for c in engine.chunks]
143 |         engine._bm25 = BM25Okapi(engine._doc_tokens)
144 | 
145 |         texts = [c.text for c in engine.chunks]
146 |         emb = engine.embedder.encode(texts, normalize_embeddings=True, convert_to_numpy=True)
147 |         engine._embeddings = emb
148 | 
149 |         return engine
150 | 
151 |     # ---------- Query ----------
152 |     def search(
153 |         self,
154 |         prepped_query: Union[str, Dict[str, Any]],
155 |         top_k: int = 5,
156 |         semantic_weight: float = 0.60,
157 |         bm25_weight: float = 0.40,
158 |     ) -> List[Dict[str, Any]]:
159 |         """
160 |         Hybrid search over the engine's VDB and return the top_k chunks.
161 | 
162 |         Returns (each item):
163 |             {
164 |               "law_name": str,
165 |               "chunk": str,
166 |               "relevance_score": float,   # 0..10 (hybrid)
167 |               "domain": str
168 |             }
169 |         """
170 |         if not self.chunks or self._embeddings is None or self._bm25 is None:
171 |             raise RuntimeError("Engine not initialized. Use RAGEngine.from_domain_dir(...) first.")
172 | 
173 |         # 1) Prepare query text from dict or string
174 |         q_text = _combine_prepped_query(prepped_query)
175 | 
176 |         # 2) Semantic & BM25 scores for all docs
177 |         q_vec = self.embedder.encode([q_text], normalize_embeddings=True, convert_to_numpy=True)[0]
178 |         sem_scores = (self._embeddings @ q_vec)  # cosine similarity in [-1,1], mostly >= 0 for MiniLM
179 |         bm25_scores = self._bm25.get_scores(_tok(q_text))  # arbitrary positive scale
180 | 
181 |         # 3) Normalize each score vector to 0..1
182 |         sem_n = _minmax_norm(sem_scores.tolist())
183 |         bm25_n = _minmax_norm(bm25_scores.tolist())
184 | 
185 |         # 4) Hybrid score (fixed weights)
186 |         s = semantic_weight + bm25_weight
187 |         sw = semantic_weight / s
188 |         bw = bm25_weight / s
189 |         hybrid = [sw * s_ + bw * b_ for s_, b_ in zip(sem_n, bm25_n)]
190 | 
191 |         # 5) Rank and select top_k
192 |         order = np.argsort(-np.asarray(hybrid))[: top_k]
193 | 
194 |         results: List[Dict[str, Any]] = []
195 |         for idx in order:
196 |             score_0_10 = 10.0 * float(hybrid[idx])  # human-readable scale
197 |             c = self.chunks[idx]
198 |             results.append({
199 |                 "law_name": c.law_name,
200 |                 "chunk": c.text,
201 |                 "relevance_score": round(score_0_10, 3),
202 |                 "domain": c.domain,
203 |             })
204 | 
205 |         return results
206 | 
207 | 
208 | # ---------------------------
209 | # Helpers
210 | # ---------------------------
211 | def _minmax_norm(values: List[float]) -> List[float]:
212 |     if not values:
213 |         return []
214 |     vmin, vmax = float(min(values)), float(max(values))
215 |     if math.isclose(vmin, vmax):
216 |         return [0.5 for _ in values]
217 |     return [(v - vmin) / (vmax - vmin) for v in values]
218 | 
219 | 
220 | def _combine_prepped_query(q: Union[str, Dict[str, Any]]) -> str:
221 |     """
222 |     Convert a structured 'prepped query' into a single search string.
223 |     Lightly prioritizes title/description and keeps a 'region:<X>' hint if present.
224 |     """
225 |     if isinstance(q, str):
226 |         return q.strip()
227 | 
228 |     def _safe(s: Any) -> str:
229 |         return str(s).strip() if isinstance(s, (str, int, float)) else ""
230 | 
231 |     parts: List[str] = []
232 |     title   = _safe(q.get("feature_title"))
233 |     desc    = _safe(q.get("feature_description"))
234 |     reqs    = _safe(q.get("feature_requirements"))
235 |     impacts = _safe(q.get("potential_impacts"))
236 |     regions = _safe(q.get("regions"))
237 | 
238 |     if title:   parts.append(title)
239 |     if desc:    parts.append(desc)
240 |     if reqs:    parts.append(reqs)
241 |     if impacts: parts.append(impacts)
242 |     if regions: parts.append(f"region:{regions}")
243 | 
244 |     return " ".join(parts).strip()
245 | 


--------------------------------------------------------------------------------
/utils/semanticchunker.py:
--------------------------------------------------------------------------------
  1 | import nltk
  2 | import openai
  3 | import os
  4 | import re
  5 | from pathlib import Path
  6 | from dotenv import load_dotenv
  7 | from nltk.tokenize import sent_tokenize
  8 | from langchain.chat_models import init_chat_model
  9 | from langchain_core.prompts import ChatPromptTemplate
 10 | from pydantic import BaseModel, Field
 11 | import sys
 12 | sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
 13 | import config
 14 | from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
 15 | from typing import List
 16 | 
 17 | nltk.download('punkt')
 18 | 
 19 | project_root = Path(__file__).resolve().parent.parent
 20 | dotenv_path = project_root / '.env'
 21 | load_dotenv(dotenv_path=dotenv_path)
 22 | 
 23 | apikey = os.environ.get("OPENAI_API_KEY")
 24 | # print(apikey)
 25 | 
 26 | # _file = "C:\\Users\\Teh Ze Shi\\OneDrive\\schoolwork\TT Techjam 2025\\lol\\kb\\youth_safety\\CA_SB967.txt"
 27 | _file = "C:\\Users\\Teh Ze Shi\\OneDrive\\schoolwork\TT Techjam 2025\\lol\\kb\\youth_safety\\FL_HB3.txt"
 28 | 
 29 | class Chunk(BaseModel):
 30 |     """Chunk with chunk_index and sentence_indices"""
 31 |     chunk_index: int = Field(description="Integer chunk_index starting at 0")
 32 |     sentence_indices: List[int] = Field(
 33 |         description="Ordered sentence_indices that belong to this chunk"
 34 |     )
 35 | 
 36 | class SemanticChunks(BaseModel):
 37 |     """List of chunks"""
 38 |     chunks: List[Chunk] = Field(
 39 |         description="List of chunks; each has a chunk_index and its sentence_indices"
 40 |     )
 41 | 
 42 | def open_txt(txtfile):
 43 |     try:
 44 |         with open(txtfile, 'r', encoding='utf-8') as file:
 45 |             text = file.read()
 46 | 
 47 |         # Split to get title and content using your pattern
 48 |         if '/()/()/\n\n\n' in text:
 49 |             parts = text.split('/()/()/\n\n\n', 1)
 50 |             title = parts[0].strip()
 51 |             content = parts[1].strip()
 52 |             return title, content
 53 |         else:
 54 |             # Fallback if pattern not found
 55 |             print(f"Pattern not found in {txtfile}, using first line as title")
 56 |             lines = text.split('\n', 1)
 57 |             title = lines[0].strip()
 58 |             content = lines[1] if len(lines) > 1 else ""
 59 |             return title, content
 60 |             
 61 |     except Exception as e:
 62 |         print(f"Error reading {txtfile}: {e}")
 63 |         return None, None
 64 | 
 65 | # Initialize structured llm function
 66 | def init_llm():
 67 |     if (hf_token := config.get_token()):
 68 |         llm = HuggingFaceEndpoint(
 69 |             repo_id='openai/gpt-oss-20b',
 70 |             huggingfacehub_api_token = hf_token
 71 |         )
 72 |         
 73 |         llm = ChatHuggingFace(llm = llm, temperature = 0)
 74 |         structured_llm = llm.bind_tools([SemanticChunks])
 75 |         return structured_llm
 76 |     try:
 77 |         llm = init_chat_model("gpt-4o-mini", model_provider="openai")
 78 |         structured_llm = llm.with_structured_output(SemanticChunks)
 79 |         return structured_llm
 80 |     except openai.APIError as e:
 81 |         print(f"An API error occurred: {e}")
 82 | 
 83 | 
 84 | def split_and_index_doc(legi_doc_txt: str):
 85 |     legi_title, legi_doc = open_txt(legi_doc_txt)
 86 |     if not legi_doc or not legi_doc.strip():
 87 |         # make cause obvious to caller
 88 |         raise ValueError(f"Empty or unreadable file: {legi_doc_txt}")
 89 | 
 90 |     # normalize newlines
 91 |     legi_doc = legi_doc.replace("\r\n", "\n").replace("\r", "\n")
 92 | 
 93 |     # primary sentence split
 94 |     legi_doc_split = sent_tokenize(legi_doc)
 95 | 
 96 |     # fallback if tokenizer yields nothing
 97 |     if not legi_doc_split:
 98 |         # split on punctuation or newlines as a last resort
 99 |         legi_doc_split = [s.strip() for s in re.split(r'(?<=[\.\?\!])\s+|\n+', legi_doc) if s.strip()]
100 | 
101 |     # still nothing? raise
102 |     if not legi_doc_split:
103 |         raise ValueError(f"No sentences tokenized for: {legi_doc_txt}")
104 | 
105 |     sentence_idx = {}
106 |     legi_doc_split_idxed = []
107 |     for i, sentence in enumerate(legi_doc_split):
108 |         legi_doc_split_idxed.append(f"<{i}>{sentence}</{i}>")
109 |         sentence_idx[i] = sentence
110 | 
111 |     out_str = " ".join(legi_doc_split_idxed)
112 |     return legi_title, out_str, sentence_idx
113 | 
114 | 
115 | def get_chunks(doc, model=None):
116 |     if not model:
117 |         model = init_llm()
118 | 
119 |     law_name, processed_doc, reconstruction_index = split_and_index_doc(doc)
120 | 
121 |     # if somehow empty, bail out early (caller can skip file)
122 |     if not reconstruction_index:
123 |         return law_name, []
124 | 
125 |     chunking_prompt = ChatPromptTemplate.from_template(
126 |         """You are an expert at splitting text into smaller chunks without breaking context.
127 |         Each sentence in the input has a numeric index in <index>sentence</index> tags.
128 |         Return ONLY the fields defined in the SemanticChunks schema.
129 | 
130 |         Rules:
131 |         - Keep sentences in original order within each chunk.
132 |         - Do not skip indices you include; no duplicates within a chunk.
133 |         - Prefer 2-3 sentences per chunk if sentences are short, but just 1-2 if sentences are long.
134 | 
135 |         Text to split:
136 |         {text}"""
137 |     )
138 | 
139 |     chunking_prompt_w_text = chunking_prompt.invoke({"text": processed_doc})
140 |     chunks = model.invoke(chunking_prompt_w_text)
141 |     if (hf_token := config.get_token()):
142 |         chunks = SemanticChunks.model_validate(chunks.tool_calls[0]['args'])
143 | 
144 |     reconstructed_chunks = []
145 | 
146 |     # (optional) keep your prints if you like
147 |     # print(reconstruction_index.keys())
148 |     for chunk in chunks.chunks:
149 |         # print(chunk)
150 |         chunk_sentences = []
151 |         for sentence_idx in chunk.sentence_indices:
152 |             # **GUARD**: only append if index exists
153 |             if sentence_idx in reconstruction_index:
154 |                 chunk_sentences.append(reconstruction_index[sentence_idx])
155 |             # else silently skip bad indices from the model
156 |         if chunk_sentences:
157 |             reconstructed_chunks.append(" ".join(chunk_sentences))
158 | 
159 |     # If the model returned only bad indices, make a single fallback chunk
160 |     if not reconstructed_chunks:
161 |         reconstructed_chunks = [" ".join(reconstruction_index[i] for i in sorted(reconstruction_index))]
162 | 
163 |     return law_name, reconstructed_chunks
164 | 


--------------------------------------------------------------------------------

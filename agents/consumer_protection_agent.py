# agents/consumer_protection_agent.py
from .base_agent import BaseAgent
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import config
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint


class ConsumerProtectionAgent(BaseAgent):
    def __init__(self, retriever):
        super().__init__("Consumer Protection Agent", retriever)
        # Prompt keeps the agent focused on consumer-protection analysis and chunk citations
        self.prompt_template = ChatPromptTemplate.from_messages([
            ("system",
                """
                You are the Consumer Protection domain expert.
                Evaluate consumer-protection obligations and risks using ONLY the provided law chunks.
                Each chunk is labelled with a law name and chunk number.
                Only reference laws from this list: {laws_list}.
                Do not make final compliance decisions—simply report consumer-protection implications.
                """
            ),
            ("human",
                """
                Feature Summary:
                {feature_summary}

                Legal Excerpts:
                {context}

                Your Task:
                1. Identify any consumer-protection obligations or risks evident in these excerpts. Consider areas such as:
                   - unfair or deceptive acts or practices (UDAAP/UDAP),
                   - dark patterns/manipulative design,
                   - ranking/personalization transparency and disclosures,
                   - advertising/endorsement disclosures,
                   - trial-to-paid, auto-renewal, cancellation/refund rules,
                   - pricing clarity, hidden fees, or misleading claims,
                   - complaint handling and redress.
                2. For each cited point, include the jurisdiction and law name (from {laws_list}) and the chunk number(s).
                3. If no consumer-protection obligations are found, state 'None'.

                Respond in this format:
                - Consumer-Protection Concern: [Yes/No/Unclear]
                - Analysis: [reasoning with law name(s) and chunk number(s)]
                - Related Regulations: [list of cited laws or 'None']
                """
            )
        ])

    def analyze_feature(self, feature_summary: str) -> dict:
        # Create the LLM object (same pattern as other agents)
        if (hf_token := config.get_token()):
            hf_endpoint = HuggingFaceEndpoint(
                repo_id='openai/gpt-oss-20b',
                huggingfacehub_api_token=hf_token
            )
            llm = ChatHuggingFace(llm=hf_endpoint, temperature=0)
        else:
            llm = ChatOpenAI(model="gpt-3.5-turbo")

        # Step 1: Retrieve relevant context and laws
        retrieval_result = self._retrieve_context(feature_summary, k=5)
        context = "\n\n".join(
            f"{src.law} (Chunk {src.chunk_number}): {src.chunk_text}" for src in retrieval_result.sources
        )
        laws_list = retrieval_result.laws

        # Step 2: Fill in the prompt template with explicit laws list
        prompt = self.prompt_template.format_messages(
            feature_summary=feature_summary,
            context=context,
            laws_list=", ".join(laws_list) if laws_list else "No relevant laws found"
        )

        # Step 3: Get the analysis from the LLM
        analysis_result = llm.invoke(prompt).content

        # Step 4: Parse the result and add source information
        result = self._parse_llm_output(analysis_result)

        # Add source metadata to the reasoning for auditability
        source_info = self._format_source_info(retrieval_result.sources)
        result["reasoning"] = result["reasoning"] + f"\n\nSource References: {source_info}"

        return result

    def _parse_llm_output(self, text: str) -> dict:
        """Parses the LLM's text output into a structured dict (consistent with other agents)."""
        lines = [line.strip() for line in text.split('\n') if line.strip()]

        result = {
            "requires_geo_compliance": False,
            "reasoning": "Unable to parse LLM output",
            "related_regulations": "None"
        }

        try:
            for line in lines:
                if line.startswith("- Consumer-Protection Concern:"):
                    value = line.replace("- Consumer-Protection Concern:", "").strip()
                    result["requires_geo_compliance"] = value.lower() in ["yes", "y"]
                elif line.startswith("- Analysis:"):
                    result["reasoning"] = line.replace("- Analysis:", "").strip()
                elif line.startswith("- Related Regulations:"):
                    result["related_regulations"] = line.replace("- Related Regulations:", "").strip()
        except (IndexError, AttributeError):
            # Fallback if parsing fails
            result["reasoning"] = f"Raw LLM output: {text}"

        return result

    def _format_source_info(self, sources: list) -> str:
        """Formats source information for the audit trail (same pattern as other agents)."""
        if not sources:
            return "No sources retrieved"

        source_info = []
        for source in sources:
            info = f"{source.law} (Chunk {source.chunk_number})"
            source_info.append(info)

        return "; ".join(source_info)

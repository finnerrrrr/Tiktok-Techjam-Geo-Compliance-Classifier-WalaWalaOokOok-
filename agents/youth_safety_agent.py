# agents/youth_safety_agent.py
from .base_agent import BaseAgent, RetrievalResult
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate

class YouthSafetyAgent(BaseAgent):
    def __init__(self, retriever):
        super().__init__("Youth Safety Agent", retriever)
        # Define the prompt template here with explicit law guidance
        self.prompt_template = ChatPromptTemplate.from_messages([
            ("system", 
                """
                    You are a meticulous youth safety and protection compliance officer. Your goal is to prevent harm to minors. Analyze the following feature description using ONLY the context provided from relevant laws.

                    IMPORTANT INSTRUCTIONS:
                    - You MUST only reference laws from this explicit list: {laws_list}
                    - If a law is not in this list, you MUST NOT reference it, even if it appears in the context.
                    - If the feature doesn't relate to any law in this list, return 'None' for Related Regulations.
                    - If a feature could potentially harm minors or violate protections, you MUST flag it.
                """
            ),
            ("human", 
                """
                    **Feature Description to Analyze:**
                    {feature_description}

                    **Relevant Legal Context:**
                    {context}

                    **Your Task:**
                    1. Determine if this feature requires geo-specific compliance logic due to youth safety concerns.
                    2. If yes, list every country/region and cite the specific law and article that triggers the requirement (ONLY from the allowed list above).
                    3. Provide clear, auditable reasoning for your decision.
                    4. If no issues are found based on the context, state that.

                    Output your final analysis in the following structured format:
                    - Requires Geo-Compliance Logic: [Yes/No/Unclear]
                    - Reasoning: [Your reasoning here. MUST reference specific laws from the allowed list if applicable.]
                    - Related Regulations: [List of laws from the allowed list or 'None']
                """
            )
        ])

    def analyze_feature(self, feature_description: str) -> dict:
        # Create the LLM object
        llm = ChatOpenAI(model="gpt-3.5-turbo")
        
        # Step 1: Create an optimized query
        query = self._create_optimized_query(feature_description)
        
        # Step 2: Retrieve relevant context and laws
        retrieval_result = self._retrieve_context(query, k=5)
        context = retrieval_result.context
        laws_list = retrieval_result.laws
        
        # Step 3: Fill in the prompt template with explicit laws list
        prompt = self.prompt_template.format_messages(
            feature_description=feature_description,
            context=context,
            laws_list=", ".join(laws_list) if laws_list else "No relevant laws found"
        )
        
        # Step 4: Get the analysis from the LLM
        analysis_result = llm.invoke(prompt).content

        # Step 5: Parse the result and add source information
        result = self._parse_llm_output(analysis_result)
        
        # Add source metadata to the reasoning for auditability
        source_info = self._format_source_info(retrieval_result.sources)
        result["reasoning"] = result["reasoning"] + f"\n\nSource References: {source_info}"
        
        return result

    def _parse_llm_output(self, text: str) -> dict:
        """Parses the LLM's text output into a structured dict."""
        lines = [line.strip() for line in text.split('\n') if line.strip()]
        
        result = {
            "requires_geo_compliance": False,
            "reasoning": "Unable to parse LLM output",
            "related_regulations": "None"
        }
        
        try:
            for i, line in enumerate(lines):
                if line.startswith("- Requires Geo-Compliance Logic:"):
                    value = line.replace("- Requires Geo-Compliance Logic:", "").strip()
                    result["requires_geo_compliance"] = value.lower() in ["yes", "true", "y"]
                elif line.startswith("- Reasoning:"):
                    result["reasoning"] = line.replace("- Reasoning:", "").strip()
                elif line.startswith("- Related Regulations:"):
                    result["related_regulations"] = line.replace("- Related Regulations:", "").strip()
        except (IndexError, AttributeError):
            # Fallback if parsing fails
            result["reasoning"] = f"Raw LLM output: {text}"
        
        return result

    def _format_source_info(self, sources: list) -> str:
        """Formats source information for the audit trail."""
        if not sources:
            return "No sources retrieved"
        
        source_info = []
        for source in sources:
            info = f"{source.law} (Chunk {source.chunk_number})"
            source_info.append(info)
        
        return "; ".join(source_info)
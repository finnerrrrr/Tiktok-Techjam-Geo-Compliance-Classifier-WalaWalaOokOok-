# agents/youth_safety_agent.py
from .base_agent import BaseAgent
# Use the updated, non-deprecated import:
from langchain_openai import ChatOpenAI  # <- FIXED IMPORT
from langchain.prompts import ChatPromptTemplate




class YouthSafetyAgent(BaseAgent):
    def __init__(self, retriever):
        super().__init__("Youth Safety Agent", retriever)
        # Define the prompt template here
        self.prompt_template = ChatPromptTemplate.from_messages([
            ("system", "You are a meticulous youth safety and protection compliance officer. Your goal is to prevent harm to minors. Analyze the following feature description using ONLY the context provided from relevant laws. If a feature could potentially harm minors or violate protections, you MUST flag it."),
            ("human", """
            **Feature Description to Analyze:**
            {feature_description}

            **Relevant Legal Context:**
            {context}

            **Your Task:**
            1. Determine if this feature requires geo-specific compliance logic due to youth safety concerns.
            2. If yes, list every country/region and cite the specific law and article that triggers the requirement.
            3. Provide clear, auditable reasoning for your decision.
            4. If no issues are found based on the context, state that.

            Output your final analysis in the following structured format:
            - Requires Geo-Compliance Logic: [Yes/No/Unclear]
            - Reasoning: [Your reasoning here]
            - Related Regulations: [List of laws or 'None']
            """)
        ])

    def analyze_feature(self, feature_description: str) -> dict:
        # Create the LLM object HERE, when the method is called
        llm = ChatOpenAI(model="gpt-3.5-turbo")
        
        # Step 1: Create an optimized query
        query = self._create_optimized_query(feature_description)
        # Step 2: Retrieve relevant context and source metadata
        context, sources = self._retrieve_context(query, k=5)
        # Step 3: Fill in the prompt template
        prompt = self.prompt_template.format_messages(
            feature_description=feature_description,
            context=context
        )
        # Step 4: Get the analysis from the LLM
        analysis_result = llm.invoke(prompt).content

        # Step 5: Parse the result and add source information
        result = self._parse_llm_output(analysis_result)
        # Add source metadata to the reasoning
        source_info = f"\nSources: {sources}"
        result["reasoning"] = result["reasoning"] + source_info
        return result

    def _parse_llm_output(self, text: str) -> dict:
        """Parses the LLM's text output into a structured dict."""
        lines = text.split('\n')
        result = {
            "requires_geo_compliance": "Yes" in lines[0],
            "reasoning": lines[1].replace("- Reasoning: ", "").strip(),
            "related_regulations": lines[2].replace("- Related Regulations: ", "").strip()
        }
        return result
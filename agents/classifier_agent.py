# agents/youth_safety_agent.py

from agents.base_agent import BaseAgent
# Use the updated, non-deprecated import:
from langchain_openai import ChatOpenAI  # <- FIXED IMPORT
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain.prompts import ChatPromptTemplate
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import config
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint

class ClassifierAgent(BaseAgent):
    def __init__(self, retriever = None):
        super().__init__("Classifier Agent", retriever)
        # Define the prompt template here
        self.prompt_template = ChatPromptTemplate.from_messages([
            ("system", "You are a meticulous geo-compliance officer at TikTok. Your goal is to prevent harm to users. Analyze the following feature and understand the opinions of experts from each legal domain. Flag the feature if it requires geo-specific compliance logic."),
            ("human", """
            {feature_summary}

            **Expert Opinions:**
            {opinions}

            **Your Task:**
            1. Based on expert opinions, determine if this feature requires geo-specific compliance logic.
            2. If yes, list every country/region and cite the specific law and article that triggers the requirement.
            3. Provide clear, auditable reasoning for your decision.
            4. If no issues are found based on the context, state that.

            Output your final analysis in the following structured format:
            - Requires Geo-Compliance Logic: [Yes/No/Unclear]
            - Reasoning: [Your reasoning here]
            - Related Regulations: [List of laws or 'None']
            """)
        ])

    def analyze_feature(self, feature_summary: str, opinions: str) -> dict:
        # Create the LLM object HERE, when the method is called
        if (hf_token := config.get_token()):
            llm = HuggingFaceEndpoint(
                repo_id='openai/gpt-oss-20b',
                huggingfacehub_api_token = hf_token
            )
            
            llm = ChatHuggingFace(llm = llm, temperature = 0)
        else:
            llm = ChatOpenAI(model="gpt-3.5-turbo")

        # llm = ChatHuggingFace(llm = model, temperature = 0)
        
        # Step 1: Fill in the prompt template
        prompt = self.prompt_template.format_messages(
            feature_summary=feature_summary,
            opinions = opinions
        )
        # Step 2: Get the analysis from the LLM
        analysis_result = llm.invoke(prompt).content

        # Step 3: Parse the result and add source information
        result = self._parse_llm_output(analysis_result)
        # Add source metadata to the reasoning
        return result

    def _parse_llm_output(self, text: str) -> dict:
        """Parses the LLM's text output into a structured dict."""
        lines = text.split('\n')
        result = {
            "requires_geo_compliance": lines[0],
            "reasoning": lines[1].replace("- Reasoning: ", "").strip(),
            "related_regulations": lines[2].replace("- Related Regulations: ", "").strip()
        }
        return result

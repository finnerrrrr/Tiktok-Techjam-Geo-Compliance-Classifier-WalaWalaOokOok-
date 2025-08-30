import openai
from langchain.chat_models import init_chat_model
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel, Field


class QuerySummary(BaseModel):
    title: str = Field(
        description=(
            "title of the feature as per the original input"
        )
    )
    description: str = Field(
        description=(
            "description of the feature as per the origina input"
        )
    )
    requirements: list[str] = Field(
        description=(
            "A list of strings containing requirements (methods that need to be used or things that need to be collected) "
            "for the successful implementation of the feature, followed by the reasoning for the requirement. "
            "Each item MUST be phrased as: 'The feature needs <requirement> because <reason>'."
        )
    )
    effects: list[str] = Field(
        description=(
            "A list of strings describing potential impacts on different stakeholder groups (e.g., minors, general users, "
            "content creators, advertisers, moderators). Each item MUST be phrased as: "
            "'Impact on <group>: <effect> because <reason>'. If no clear impacts are stated or minimally implied, return []."
        )
    )
    regions: list[str] = Field(
        description=(
            "A list of strings representing the geographical regions where the feature will be tested or deployed. "
            "If no regions are specified, return ['Global']."
        )
    )

input_query_enhancing_prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        "You are an extraction assistant for a backend compliance pre-processor. "
        "Your sole job is to read a short feature title and description and return ONLY the fields "
        "defined by the QuerySummary schema provided by the caller (handled via structured output). "
        "Do not add fields, explanations, or commentary."
        "\n\n"
        "Extraction rules:\n"
        "1) requirements (list[str]): Identify concrete implementation requirements that are NECESSARY "
        "   to build or operate the feature, and give a short reason for each. "
        "   Each item MUST be phrased as: 'The feature needs <requirement> because <reason>'.\n"
        "   - Allowed examples of <requirement>: collect <data/signal>, infer <attribute>, store <logs>, "
        "     run A/B tests, deploy <model/algorithm>, maintain <data retention>, implement <age gating>, "
        "     integrate <payment/subscription>, enable <geo-handler>, display <notice/consent>, etc.\n"
        "   - Base each requirement on explicit statements or minimally necessary implications from the text. "
        "     Do NOT speculate beyond the given content.\n"
        "   - If nothing is needed beyond generic app behavior, return an empty list [].\n"
        "\n"
        "2) effects (list[str]): Describe potential impacts on different stakeholder groups ONLY when the text clearly supports them "
        "   (explicitly or via minimal, necessary implication). "
        "   - Each item MUST be phrased as: 'Impact on <group>: <effect> because <reason>'.\n"
        "   - Examples of <group>: minors, general users, content creators, advertisers, moderators, parents/guardians.\n"
        "   - Keep effects concise and tied to the described feature; do NOT infer legal outcomes.\n"
        "   - If no clear impacts are supported, return [].\n"
        "\n"
        "3) regions (list[str]): Extract any explicit geographic constraints mentioned in EITHER the title "
        "   or the description (e.g., 'California', 'EU', 'UK', 'Singapore', 'US', 'APAC'). "
        "   - Return EXACT strings as written or common short forms if unambiguous (e.g., 'California' or 'US-CA' if stated as 'California').\n"
        "   - If multiple regions are stated, include all of them in a list (deduplicate; keep order of appearance).\n"
        "   - If NO geographic scope is stated, return ['Global'].\n"
        "\n"
        "Constraints:\n"
        "- Be concise and literal; do not infer legal/compliance conclusions.\n"
        "- No hallucinations: if not clearly supported by the text, omit it.\n"
        "- Output MUST conform to the QuerySummary schema (handled by structured output)."
        "For abbreviations, use the following:"
        """
            "NR":	"Not recommended",
            "PF":	"Personalized feed",
            "GH":	"Geo-handler; a module responsible for routing features based on user region",
            "CDS":	"Compliance Detection System",
            "DRT":	"Data retention threshold; duration for which logs can be stored",
            "LCP":	"Local compliance policy",
            "Redline":	"Flag for legal review (different from its traditional business use for 'financial loss')",
            "Softblock":	"A user-level limitation applied silently without notifications",
            "Spanner":	"A synthetic name for a rule engine (not to be confused with Google Spanner)",
            "ShadowMode":	"Deploy feature in non-user-impact way to collect analytics only",
            "T5":	"Tier 5 sensitivity data; more critical than T1‚ÄìT4 in this internal taxonomy",
            "ASL":	"Age-sensitive logic",
            "Glow":	"A compliance-flagging status, internally used to indicate geo-based alerts",
            "NSP":	"Non-shareable policy (content should not be shared externally)",
            "Jellybean":	"Feature name for internal parental control system",
            "EchoTrace":	"Log tracing mode to verify compliance routing",
            "BB":	"Baseline Behavior; standard user behavior used for anomaly detection",
            "Snowcap":	"A synthetic codename for the child safety policy framework",
            "FR":	"Feature rollout status",
            "IMT":	"Internal monitoring trigger"
        """
        "Please think 1 level deeper"
    ),
    (
        "human",
        "Feature Title: {feature_title}\n"
        "Feature Description: {feature_description}\n"
        "\n"
        "Return ONLY the fields in the QuerySummary schema (the runtime will enforce the structure)."
    )
])

def init_llm():
    try:
        llm = init_chat_model("gpt-5", model_provider="openai")
        structured_llm = llm.with_structured_output(QuerySummary)
        return structured_llm
    except openai.APIError as e:
        print(f"An API error occurred: {e}")

def format_query_summary(summary) -> str:
    # Safeguards
    title = getattr(summary, "title", "") or ""
    description = getattr(summary, "description", "") or ""
    requirements = getattr(summary, "requirements", None) or []
    effects = getattr(summary, "effects", None) or []
    regions = getattr(summary, "regions", None) or ["Global"]

    # Join list fields into human-readable text
    req_text = "; ".join(requirements) if requirements else "Unspecified"
    eff_text = "; ".join(effects) if effects else "Unspecified"
    reg_text = "; ".join(regions) if regions else "Global"

    return (
        f"Feature title: {title}\n\n"
        f"Feature description: {description}\n\n"
        f"Feature requirements: {req_text}\n\n"
        f"Potential impact(s): {eff_text}\n\n"
        f"Regions for testing/rollout of feature: {reg_text}"
    )

def enhance_query(feature_title, feature_description, llm=None, as_text=True):
    if not llm:
        llm = init_llm()
    prompt = input_query_enhancing_prompt.invoke({"feature_title": feature_title, "feature_description": feature_description})
    response = llm.invoke(prompt)
    
    if as_text:
        return format_query_summary(response)
    return response
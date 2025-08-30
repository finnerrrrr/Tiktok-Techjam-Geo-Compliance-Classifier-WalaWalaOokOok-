# pilot.py
from agents.youth_safety_agent import YouthSafetyAgent
from agents.data_privacy_agent import DataPrivacyAgent
from agents.content_moderation_agent import ContentModerationAgent
from agents.consumer_protection_agent import ConsumerProtectionAgent
from agents.ai_governance_agent import AIGovernanceAgent
from agents.ip_protection_agent import IPProtectionAgent
from agents.classifier_agent import ClassifierAgent

from utils.rag import get_vector_db, embedding_model
import os
import config

# Helper function for DRY initialization
def load_agent(agent_class, kb_name: str):
    db_path = f"./kb/{kb_name}_chromadb"
    kb_path = f"./kb/{kb_name}"

    # Create or load vector DB
    if not os.path.exists(db_path):
        from utils.rag import create_vector_db_from_dir
        vectordb = create_vector_db_from_dir(kb_path, db_path, embedding_model)
    else:
        vectordb = get_vector_db(db_path, embedding_model)

    retriever = vectordb[0].as_retriever(search_kwargs={"k": 5})
    return agent_class(retriever)

# Initialize all agents with their respective knowledge bases
def initialize_agents():
    agents = []

    agents.append(load_agent(YouthSafetyAgent, "youth_safety"))
    agents.append(load_agent(DataPrivacyAgent, "data_privacy"))
    # agents.append(load_agent(ContentModerationAgent, "content_moderation"))
    agents.append(load_agent(ConsumerProtectionAgent, "consumer_protection"))
    # agents.append(load_agent(AIGovernanceAgent, "ai_governance"))
    # agents.append(load_agent(IPProtectionAgent, "ip_protection"))

    return agents

def main(feature_description, token = None):
    config.set_token(token)
    import nltk
    nltk.download('punkt_tab')
    # 1. Initialize all specialist agents
    print("Initializing agents and loading knowledge bases...")
    yield "Initializing agents and loading knowledge bases..."
    specialist_agents = initialize_agents()
    
    # 2. Get the feature description
    print(f"\nAnalyzing feature: {feature_description}")
    yield f"\nAnalyzing feature: {feature_description}"
    
    # 3. Send the feature to EVERY agent for analysis
    all_results = {}
    for agent in specialist_agents:
        print(f"\n--- Consulting {agent.name} ---")
        yield f"\n--- Consulting {agent.name} ---"
        result = agent.analyze_feature(feature_description)
        all_results[agent.name] = result
        print(f"Result: {result}")
        yield f"Result: {result}"
    
    # 4. Consolidate and present the final results
    opinions = ''
    print("\n=== FINAL COMPLIANCE ASSESSMENT ===")
    yield "\n=== FINAL COMPLIANCE ASSESSMENT ==="
    for agent_name, result in all_results.items():
        print(f"\n{agent_name}:")
        print(f"  Requires Geo-Compliance Logic: {result['requires_geo_compliance']}")
        print(f"  Reasoning: {result['reasoning']}")
        print(f"  Related Regulations: {result['related_regulations']}")
        yield f"\n{agent_name}:"
        yield f"  Requires Geo-Compliance Logic: {result['requires_geo_compliance']}"
        yield f"  Reasoning: {result['reasoning']}"
        yield f"  Related Regulations: {result['related_regulations']}"
        opinion = \
f"""

{agent_name}:
Requires Geo-Compliance Logic: {result['requires_geo_compliance']}
Reasoning: {result['reasoning']}
Related Regulations: {result['related_regulations']}
"""
        opinions += opinion
    
    print(opinions)
    # classifier

if __name__ == "__main__":
    feature = """
Feature Title: Mood-based personalized feed enhancements
Description: Adjust personalized feed recommendations based on inferred mood signals from emoji usage. This logic is soft-tuned using baseline behaviour and undergoes quiet testing in a non-user-impact way to collect analytics only.
"""
    main(feature)

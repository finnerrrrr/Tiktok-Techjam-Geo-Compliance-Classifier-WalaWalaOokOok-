# pilot.py
from agents.youth_safety_agent import YouthSafetyAgent
# from agents.data_privacy_agent import DataPrivacyAgent  # You'll create this similarly
from utils.rag import get_vector_db, embedding_model
import os

# Initialize all agents with their respective knowledge bases
def initialize_agents():
    agents = []
    
    # Initialize Youth Safety Agent
    youth_safety_db_path = "./kb/youth_safety_chromadb" # Path to store/load the vector DB
    youth_safety_kb_path = "./kb/youth_safety"          # Path to raw .txt files
    
    # Check if vector DB exists, if not, create it
    if not os.path.exists(youth_safety_db_path):
        from utils.rag import create_vector_db_from_dir
        youth_vectordb = create_vector_db_from_dir(
            youth_safety_kb_path, youth_safety_db_path, embedding_model
        )
    else:
        youth_vectordb = get_vector_db(youth_safety_db_path, embedding_model)
    
    youth_retriever = youth_vectordb.as_retriever(search_kwargs={"k": 5})
    agents.append(YouthSafetyAgent(youth_retriever))
    
    # Initialize Data Privacy Agent (Repeat the same process)
    # data_privacy_db_path = "./kb/data_privacy_chromadb"
    # data_privacy_kb_path = "./kb/data_privacy"
    # ... [Create/get vector DB]
    # agents.append(DataPrivacyAgent(data_retriever))
    
    return agents

def main():
    # 1. Initialize all specialist agents
    print("Initializing agents and loading knowledge bases...")
    specialist_agents = initialize_agents()
    
    # 2. Get the feature description (this could be from user input, a file, etc.)
    feature_description = """
    Feature Title: Mood-based personalized feed enhancements
    Description: Adjust personalized feed recommendations based on inferred mood signals from emoji usage. This logic is soft-tuned using baseline behaviour and undergoes quiet testing in a non-user-impact way to collect analytics only.
    """
    
    print(f"\nAnalyzing feature: {feature_description}")
    
    # 3. Send the feature to EVERY agent for analysis
    all_results = {}
    for agent in specialist_agents:
        print(f"\n--- Consulting {agent.name} ---")
        result = agent.analyze_feature(feature_description)
        all_results[agent.name] = result
        print(f"Result: {result}")
    
    # 4. Consolidate and present the final results
    print("\n=== FINAL COMPLIANCE ASSESSMENT ===")
    for agent_name, result in all_results.items():
        print(f"\n{agent_name}:")
        print(f"  Requires Geo-Compliance Logic: {result['requires_geo_compliance']}")
        print(f"  Reasoning: {result['reasoning']}")
        print(f"  Related Regulations: {result['related_regulations']}")

if __name__ == "__main__":
    main()
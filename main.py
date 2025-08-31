"""
pilot.py - orchestrates the end-to-end compliance workflow.

Assumptions made:
- Each domain agent will initialise its own vector database by calling a yet-to-be-created
  utility helper. Therefore the pilot instantiates agents without handling VDB setup.
- The query preparation step uses `enhance_query` which returns a text summary of the
  feature title and description. This text is sent to downstream agents.
- Domain agents expose `analyze_feature(prepped_query)` and return a list of chunk
  dictionaries with at least `content`, `relevance_score` and optional `citation`
  and `domain_tag` fields.
- RerankerAgent.process, VerifierAgent.process, AggregatorAgent.process and
  ClassifierAgent.classify follow the interfaces defined in their respective modules.
- Low verifier confidence triggers the HITLAgent for a possible manual override.
"""

from __future__ import annotations

import asyncio
from typing import List, Type

from agents.youth_safety_agent import YouthSafetyAgent
# from agents.data_privacy_agent import DataPrivacyAgent
# from agents.content_moderation_agent import ContentModerationAgent
# from agents.consumer_protection_agent import ConsumerProtectionAgent
# from agents.ai_governance_agent import AIGovernanceAgent
# from agents.ip_protection_agent import IPProtectionAgent
from agents.reranker_agent import RerankerAgent
from agents.verifier_agent import VerifierAgent
from agents.hitl_agent import HITLAgent
from agents.aggregator_agent import AggregatorAgent
from agents.classifier_agent import ClassifierAgent

from utils.inputqueryenhancer import enhance_query


def main(feature_title: str, feature_description: str):
    """Run the full compliance workflow."""
    # 1. Query preparation
    prepped_query = enhance_query(feature_title, feature_description)
    print("Prepared query:\n", prepped_query)
    yield "Prepared query:\n" + prepped_query

    # 2. Initialise domain agents
    # Assumes each agent handles its own VDB initialisation internally.
    domain_agent_classes: List[Type] = [
        YouthSafetyAgent
        # DataPrivacyAgent,
        # ContentModerationAgent,
        # ConsumerProtectionAgent,
        # AIGovernanceAgent,
        # IPProtectionAgent,
    ]
    domain_agents = [cls() for cls in domain_agent_classes]

    # 3. Retrieve chunks from all domain agents
    all_chunks = []
    for agent in domain_agents:
        chunks = agent.analyze_feature(prepped_query)
        # Expect each agent to return: List[{"content", "relevance_score", "citation"?, "domain_tag"?}]
        print(f"{agent.name} returned {len(chunks)} chunks")
        yield f"{agent.name} returned {len(chunks)} chunks"
        all_chunks.extend(chunks)

    # 4. Rerank and select diverse set of chunks
    reranker = RerankerAgent()
    selected_chunks = asyncio.run(reranker.process(all_chunks, prepped_query))
    print(f"Reranker selected {len(selected_chunks)} chunks")
    yield f"Reranker selected {len(selected_chunks)} chunks"

    # 5. Verification for confidence score
    verifier = VerifierAgent()
    verification = verifier.process(selected_chunks, prepped_query)
    print(f"Verification confidence: {verification['confidence']:.2f}")
    yield f"Verification confidence: {verification['confidence']:.2f}"

    # 6. Human-in-the-loop override if confidence low
    hitl_feedback = None
    if verification["escalate"]:
        hitl_feedback = HITLAgent().process(verification, prepped_query)

    # 7. Aggregation of context for classification
    aggregator = AggregatorAgent()
    aggregated = aggregator.process(verification["chunks"], hitl_feedback)

    # 8. Final classification
    classifier = ClassifierAgent()
    result = asyncio.run(classifier.classify(aggregated, prepped_query))

    # 9. Output results and audit trail
    print("\n=== FINAL OUTPUT ===")
    print(f"Flag: {result['flag']}")
    print(f"Reasoning: {result['reasoning']}")
    print(f"Regulations: {result['regulations']}")
    print("Audit trail:")
    for entry in result["audit_trail"]:
        print(f"- {entry}")
        yield f"- {entry}"


if __name__ == "__main__":
    # Example invocation; replace with real feature details
    main(
        feature_title="Content visibility lock with NSP for EU DSA",
        feature_description="To meet the transparency expectations of the EU Digital Services Act..."
    )

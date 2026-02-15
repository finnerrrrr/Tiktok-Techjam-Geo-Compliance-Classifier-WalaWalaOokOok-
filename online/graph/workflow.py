from __future__ import annotations

from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import END, START, StateGraph

from offline.qdrant_config import QdrantSettings
from offline.retriever import ComplianceRetriever
from online.graph.nodes import classify, finalize, query_enhance_route, rerank
from online.graph.nodes.retrieve import make_node as make_retrieve_node
from online.graph.state import WorkflowState


def build_app(settings: QdrantSettings | None = None):
    retriever = ComplianceRetriever(settings=settings)

    graph = StateGraph(WorkflowState)
    graph.add_node("query_enhance_route", query_enhance_route.make_node(retriever.available_domains))
    graph.add_node("retrieve", make_retrieve_node(retriever.search, retriever.available_domains))
    graph.add_node("rerank", rerank.run)
    graph.add_node("classify", classify.run)
    graph.add_node("finalize", finalize.run)

    graph.add_edge(START, "query_enhance_route")
    graph.add_edge("query_enhance_route", "retrieve")
    graph.add_edge("retrieve", "rerank")
    graph.add_edge("rerank", "classify")
    graph.add_edge("classify", "finalize")
    graph.add_edge("finalize", END)

    return graph.compile(checkpointer=MemorySaver())

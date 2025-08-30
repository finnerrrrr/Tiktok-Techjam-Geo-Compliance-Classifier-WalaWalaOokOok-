import asyncio
import platform
import requests
import json
import numpy as np
from collections import defaultdict

class RerankerAgent:
    def __init__(self, top_n=5, mmr_lambda=0.7):
        self.top_n = top_n
        self.mmr_lambda = mmr_lambda

    async def load_cross_encoder(self, model_url):
        """Load cross-encoder model with proper error handling"""
        try:
            response = requests.get(model_url)
            model_data = response.json()

            class CrossEncoder:
                def __init__(self):
                    self.initialized = True

                def predict(self, sentence_pairs, **kwargs):
                    # Enhanced mock scoring with better semantic simulation
                    scores = []
                    # sentence_pairs is a list of [query, chunk_content]
                    for query, chunk_content in sentence_pairs:
                        # Simulate semantic similarity with better heuristics
                        query_terms = set(query.lower().split())
                        content_terms = set(chunk_content.lower().split())
                        overlap = len(query_terms & content_terms)
                        jaccard_sim = overlap / len(query_terms | content_terms) if query_terms or content_terms else 0

                        # Boost score for having citations - simulate based on content presence
                        # The original 'chunk' object is not available here, so we simulate based on content
                        citation_boost = 0.2 if "citation" in chunk_content.lower() else 0 # Check for 'citation' keyword in content

                        score = jaccard_sim * 10 + citation_boost
                        scores.append(score)

                    return np.array(scores)

            return CrossEncoder()

        except Exception as e:
            print(f"Error loading cross-encoder: {e}")
            # Fallback to simple scoring
            return None

    async def rerank_chunks(self, cross_encoder, chunks, query):
        """Rerank chunks using cross-encoder scores combined with original relevance"""
        if not chunks:
            return []
          
        sentence_pairs = [[query, chunk["content"]] for chunk in chunks]


        # Get cross-encoder scores
        if cross_encoder:
            # Pass chunks if the mock predict needs original chunk data (it currently simulates based on content)
            # cross_scores = cross_encoder.predict(sentence_pairs, original_chunks=chunks)
            cross_scores = cross_encoder.predict(sentence_pairs) # Use the modified predict method

        else:
            # Fallback scoring if cross-encoder fails
            cross_scores = [chunk.get("relevance_score", 5) for chunk in chunks]

        # Combine scores (weighted average)
        combined_scores = []
        for i, chunk in enumerate(chunks):
            orig_score = chunk.get("relevance_score", 5)
            # Ensure cross_scores has the same length as chunks before accessing
            cross_score = cross_scores[i] if i < len(cross_scores) else 0
            combined = 0.6 * cross_score + 0.4 * orig_score
            combined_scores.append((chunk, combined))

        # Sort by combined score
        combined_scores.sort(key=lambda x: x[1], reverse=True)
        return [chunk for chunk, _ in combined_scores]

    def apply_mmr(self, chunks, query):
        """Apply Maximal Marginal Relevance for diversity"""
        if not chunks:
            return []

        selected = []
        remaining = chunks.copy()

        while len(selected) < self.top_n and remaining:
            scores = []

            for doc in remaining:
                # Similarity to query
                query_terms = set(query.lower().split())
                doc_terms = set(doc["content"].lower().split())
                sim_to_query = len(query_terms & doc_terms) / max(len(query_terms), 1)

                # Max similarity to already selected documents
                if selected:
                    sim_to_selected = max([
                        len(set(doc["content"].lower().split()) &
                           set(s["content"].lower().split())) /
                        max(len(doc["content"].split()), 1)
                        for s in selected
                    ])
                else:
                    sim_to_selected = 0

                # MMR score
                mmr_score = self.mmr_lambda * sim_to_query - (1 - self.mmr_lambda) * sim_to_selected
                scores.append((doc, mmr_score))

            # Select document with highest MMR score
            best_doc = max(scores, key=lambda x: x[1])[0]
            selected.append(best_doc)
            remaining.remove(best_doc)

        return selected

    def balance_facets(self, chunks):
        """Balance representation across different domains/facets"""
        if not chunks:
            return []

        # Group by domain tag
        facets = defaultdict(list)
        for chunk in chunks:
            domain = chunk.get("domain_tag", "Unknown")
            facets[domain].append(chunk)

        # Select top documents while maintaining facet balance
        balanced = []
        domains = list(facets.keys())

        # Round-robin selection from each facet
        while len(balanced) < self.top_n and any(facets.values()):
            for domain in domains:
                if facets[domain] and len(balanced) < self.top_n:
                    balanced.append(facets[domain].pop(0))

        return balanced

    async def process(self, chunks, query, model_url=None):
        """Main processing pipeline: rerank → MMR → facet balancing"""
        # Load cross-encoder
        cross_encoder = await self.load_cross_encoder(model_url or
                                                     "https://cdn.jsdelivr.net/npm/cross-encoder/ms-marco-MiniLM-L-6-v2/model.json")

        # Rerank with cross-encoder
        reranked = await self.rerank_chunks(cross_encoder, chunks, query)

        # Apply MMR for diversity
        diverse = self.apply_mmr(reranked, query)

        # Balance facets
        final_selection = self.balance_facets(diverse)

        return final_selection

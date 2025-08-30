import numpy as np

class VerifierAgent:
    def __init__(self, threshold=7.0, weights=None):
        self.threshold = threshold
        self.weights = weights or {
            'relevance': 0.4,
            'consistency': 0.3,
            'citation_quality': 0.2,
            'diversity': 0.1
        }

    def compute_relevance(self, chunks, query):
        """Compute relevance score (0-10)"""
        if not chunks:
            return 0.0
        query_terms = set(query.lower().split())
        avg_overlap = np.mean([
            len(query_terms & set(chunk['content'].lower().split())) / max(len(query_terms), 1)
            for chunk in chunks
        ])
        return avg_overlap * 10

    def compute_consistency(self, chunks):
        """Compute consistency score (0-10)"""
        if len(chunks) < 2:
            return 10.0
        consistencies = []
        for i in range(len(chunks)):
            for j in range(i+1, len(chunks)):
                set1 = set(chunks[i]['content'].lower().split())
                set2 = set(chunks[j]['content'].lower().split())
                overlap = len(set1 & set2) / len(set1 | set2) if set1 or set2 else 0
                consistencies.append(overlap)
        return np.mean(consistencies) * 10 if consistencies else 10.0

    def compute_citation_quality(self, chunks):
        """Compute citation quality score (0-10)"""
        if not chunks:
            return 0.0
        valid_citations = sum(1 for chunk in chunks if chunk.get('citation') and chunk['citation'] != 'No Citation')
        return (valid_citations / len(chunks)) * 10

    def compute_diversity(self, chunks):
        """Compute diversity score (0-10)"""
        if not chunks:
            return 0.0
        unique_domains = len(set(chunk.get('domain_tag', 'Unknown') for chunk in chunks))
        return min(unique_domains / (len(chunks) / 2.0), 1.0) * 10

    def compute_confidence(self, chunks, query):
        """Compute overall confidence score"""
        scores = {
            'relevance': self.compute_relevance(chunks, query),
            'consistency': self.compute_consistency(chunks),
            'citation_quality': self.compute_citation_quality(chunks),
            'diversity': self.compute_diversity(chunks)
        }
        confidence = sum(scores[component] * weight for component, weight in self.weights.items())
        return confidence, scores

    def process(self, chunks, query):
        """Process chunks and return confidence, detailed scores, and escalation flag"""
        confidence, detailed_scores = self.compute_confidence(chunks, query)
        escalate = confidence < self.threshold
        return {
            'confidence': confidence,
            'detailed_scores': detailed_scores,
            'escalate': escalate,
            'chunks': chunks
        }

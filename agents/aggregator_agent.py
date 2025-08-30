class AggregatorAgent:
    def __init__(self):
        pass

    def process(self, chunks, hitl_feedback=None):
        """Aggregate chunks into a cohesive context bundle, incorporate HITL feedback"""
        aggregated = {
            'chunks': chunks,
            'summary': ' '.join([chunk['content'][:50] for chunk in chunks]),
            'audit_trail': []
        }
        if hitl_feedback:
            aggregated['hitl_override'] = {
                'flag': hitl_feedback.get('override_flag'),
                'rationale': hitl_feedback.get('override_rationale')
            }
            aggregated['chunks'] = hitl_feedback.get('updated_chunks', chunks)
            aggregated['audit_trail'].append("HITL Override Applied")

        return aggregated

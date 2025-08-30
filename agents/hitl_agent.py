class HITLAgent:
    def __init__(self):
        pass

    def process(self, verification_result, query):
        """Handle human-in-the-loop interaction"""
        chunks = verification_result['chunks']
        print("\n--- HITL Review Required ---")
        print(f"Query: {query}")
        print("Current Chunks:")
        for i, chunk in enumerate(chunks, 1):
            print(f"Chunk {i}: {chunk['content'][:100]}... (Citation: {chunk['citation']}, Domain: {chunk['domain_tag']})")
        print(f"Confidence: {verification_result['confidence']:.2f}")
        print("Detailed Scores:", verification_result['detailed_scores'])

        override = input("\nDo you want to override? (yes/no): ").strip().lower()
        if override == 'yes':
            print("Enter corrections:")
            new_flag = input("New flag (✅/❌/❓): ").strip()
            new_rationale = input("New rationale: ").strip()
            modify_chunks = input("Modify chunks? (yes/no): ").strip().lower()
            if modify_chunks == 'yes':
                new_content = input("New chunk content: ")
                new_citation = input("New citation: ")
                new_domain = input("New domain tag: ")
                new_chunk = {
                    "content": new_content,
                    "citation": new_citation,
                    "domain_tag": new_domain,
                    "relevance_score": 10.0
                }
                chunks.append(new_chunk)
            feedback = {
                'override_flag': new_flag,
                'override_rationale': new_rationale,
                'updated_chunks': chunks
            }
        else:
            feedback = None

        return feedback

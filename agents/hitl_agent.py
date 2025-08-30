class HITLAgent:
    def process(self, verification_result, query):
        """Handle human-in-the-loop interaction"""

        chunks = verification_result['chunks']
        print("\n--- HITL Review Required ---")
        print(f"Query: {query}")
        print("Current Chunks:")
        for i, chunk in enumerate(chunks, 1):
            print(f"Chunk {i}: {chunk['content'][:100]}... (Citation: {chunk['citation']}, Domain: {chunk['domain']}, Relevance score: {chunk['relevance_score']})")
        print(f"Verifier score: {verification_result['score']}")

        audit_trail = []
        audit_trail.append(f'HITL started review with query: "{query}" and verifier score: {verification_result["score"]}')

        # Ask for human input
        override = input("\nDo you want to override question flag? (yes/no): ").strip().lower()
        if override == 'yes':
            print("Enter corrections:")
            while (new_flag := input("New flag (tick/cross): ").strip().lower()) not in ['tick', 'cross']:
                print("Invalid flag. Please enter 'tick' or 'cross'.")
                        
            rationale = input("Rationale: ").strip()

            audit_trail.append(f'HITL changed flag from question to {new_flag} with rationale: "{rationale}"')

            # Optionally modify chunks (simple example: add a new chunk)
            modify_chunks = input("Add chunk? (yes/no): ").strip().lower()
            if modify_chunks == 'yes':
                new_content = input("New chunk content: ")
                new_citation = input("New citation: ")
                new_domain = input("New domain: ")
                new_chunk = {
                    "content": new_content,
                    "citation": new_citation,
                    "domain": new_domain,
                    "relevance_score": 10.0  # Assume high for override
                }
                chunks.append(new_chunk)
                audit_trail.append(f'HITL added new chunk: Chunk {len(chunks)}: {new_chunk["content"]}, (Citation: {new_chunk["citation"]}, Domain: {new_chunk["domain"]}, Relevance score: {new_chunk["relevance_score"]})')
            feedback = {
                'flag': new_flag,
                'summary': rationale,
                'chunks': chunks,
                'audit_trail': audit_trail
            }
        else:
            rationale = input("Rationale: ").strip()
            audit_trail.append(f'HITL did not change flag with rationale: "{rationale}"')
            feedback = {
                'flag': 'question',
                'summary': rationale,
                'chunks': chunks,
                'audit_trail': audit_trail
            }

        return feedback

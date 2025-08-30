class HITLAgent:
    def __init__(self):
        pass

    def process(self, verification_result, query):
        """Handle human-in-the-loop interaction with basic validation."""
        # --- basic structure checks (minimal) ---
        if not isinstance(verification_result, dict):
            raise ValueError("verification_result must be a dict.")
        for key in ("chunks", "confidence", "detailed_scores"):
            if key not in verification_result:
                raise ValueError(f"verification_result missing required key: '{key}'")

        chunks = verification_result["chunks"]
        print("\n--- HITL Review Required ---")
        print(f"Query: {query}")
        print("Current Chunks:")
        for i, chunk in enumerate(chunks, 1):
            # tolerate missing keys in chunk dicts
            content = (chunk.get("content") or "")[:100]
            citation = chunk.get("citation", "N/A")
            domain = chunk.get("domain_tag", "N/A")
            print(f"Chunk {i}: {content}... (Citation: {citation}, Domain: {domain})")
        print(f"Confidence: {verification_result['confidence']:.2f}")
        print("Detailed Scores:", verification_result["detailed_scores"])

        # --- override yes/no ---
        override = input("\nDo you want to override? (yes/no): ").strip().lower()
        if override not in {"yes", "no"}:
            raise ValueError("Override must be 'yes' or 'no'.")

        if override == "yes":
            print("Enter corrections:")

            # --- label normalization & validation ---
            new_flag_raw = input("New label (yes/no/uncertain): ").strip().lower()  # normalize just in case
            if new_flag_raw in {"y", "yes"}:
                new_flag = "yes"
            elif new_flag_raw in {"n", "no"}:
                new_flag = "no"
            elif new_flag_raw in {"u", "unsure", "uncertain", "?"}:
                new_flag = "uncertain"
            else:
                raise ValueError("New label must be 'yes', 'no', or 'uncertain'.")

            # --- rationale required ---
            new_rationale = input("New rationale: ").strip()
            if not new_rationale:
                raise ValueError("Rationale cannot be blank.")

            # --- modify chunks? ---
            modify_chunks = input("Modify chunks? (yes/no): ").strip().lower()
            if modify_chunks not in {"yes", "no"}:
                raise ValueError("Modify chunks must be 'yes' or 'no'.")

            if modify_chunks == "yes":
                # minimal field presence checks
                new_content = input("New chunk content: ").strip()
                if not new_content:
                    raise ValueError("New chunk content cannot be blank.")

                new_citation = input("New citation: ").strip()
                if not new_citation:
                    raise ValueError("New citation cannot be blank.")

                new_domain = input("New domain tag: ").strip()
                if not new_domain:
                    raise ValueError("New domain tag cannot be blank.")

                new_chunk = {
                    "content": new_content,
                    "citation": new_citation,
                    "domain_tag": new_domain,
                    "relevance_score": 10.0,  # keep your existing default
                }
                chunks.append(new_chunk)

            feedback = {
                "override_flag": new_flag,            # 'yes' | 'no' | 'uncertain'
                "override_rationale": new_rationale,
                "updated_chunks": chunks,
            }
        else:
            feedback = None

        return feedback

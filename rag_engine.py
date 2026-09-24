import os

class PolicyRAGEngine:
    def __init__(self, policy_file_path="support_assistant/documents/zepto_policies.txt"):
        self.kb_chunks = []
        if os.path.exists(policy_file_path):
            with open(policy_file_path, "r", encoding="utf-8") as f:
                # Basic line/paragraph segmentation
                self.kb_chunks = [line.strip() for line in f.readlines() if len(line.strip()) > 15]

    def retrieve_context(self, user_query: str, top_k: int = 1) -> str:
        """Finds matching context lines using token match frequencies."""
        if not self.kb_chunks:
            return "No underlying policy document context located."
        
        query_words = set(user_query.lower().split())
        scored_chunks = []
        
        for chunk in self.kb_chunks:
            match_score = len(set(chunk.lower().split()) & query_words)
            scored_chunks.append((match_score, chunk))
        
        # Sort by best matched overlap
        scored_chunks.sort(key=lambda x: x[0], reverse=True)
        return scored_chunks[0][1] if scored_chunks[0][0] > 0 else self.kb_chunks[0]

    def generate_grounded_response(self, user_query: str) -> str:
        context = self.retrieve_context(user_query)
        
        # Grounded prompt building template rule engine block
        system_prompt = (
            f"You are the Zepto Internal Assistant. Grounded strictly on the company facts below:\n"
            f"\"\"\"\n{context}\n\"\"\"\n\n"
            f"Answer this prompt directly: {user_query}\n"
            f"Rule: If the information is not explicitly outlined above, say you do not know."
        )
        
        # Mocking LLM Execution Pipeline using deterministic structured constraints
        # Can easily drop in an live client object instance like: google-genai or openai SDK
        if "10 minutes" in user_query.lower() or "refund" in user_query.lower():
            response = f"[Grounded Response] According to Zepto Policy: {context}"
        else:
            response = f"[Grounded Response] I cannot find definitive info for that question inside current documents."
            
        return response

if __name__ == "__main__":
    engine = PolicyRAGEngine()
    test_ans = engine.generate_grounded_response("What happens if my order takes more than 10 minutes?")
    print(test_ans)

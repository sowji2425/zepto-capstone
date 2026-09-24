import sys
import os

# Ensure the parent support_assistant directory is in path for robust module imports
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

try:
    from rag_engine import PolicyRAGEngine
except ImportError:
    # Fallback to direct import if running locally from within the folder directory
    from rag_engine import PolicyRAGEngine

def run_support_app():
    print("=" * 60)
    print("      ZEPTO AI LOGISTICS & POLICY SUPPORT ASSISTANT v1.0      ")
    print("=" * 60)
    print("System Status: ONLINE | Grounded Knowledge Base: ACTIVE")
    print("Type 'exit' or 'quit' at any time to terminate the session.\n")
    
    # Initialize the grounded retrieval engine
    try:
        engine = PolicyRAGEngine()
    except Exception as e:
        print(f"CRITICAL: Failed to initialize PolicyRAGEngine: {e}")
        return

    while True:
        try:
            user_query = input("Customer Support Prompt > ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\nExiting session safely...")
            break
            
        if not user_query:
            continue
            
        if user_query.lower() in ["exit", "quit"]:
            print("Session terminated. Thank you for using Zepto Support Services.")
            break
            
        # Process query through the local grounded retrieval RAG loop
        print("\n[Processing context matching routing...]")
        response = engine.generate_grounded_response(user_query)
        
        print(response)
        print("-" * 60 + "\n")

if __name__ == "__main__":
    run_support_app()

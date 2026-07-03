import os
import json
from dotenv import load_dotenv
from groq import Groq
from services.analyzer import analyze_situation
from services.generator import generate_drafts
from services.validator import validate_response

env_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path=env_path, override=True)

def run_wingman_pipeline(situation: str):
    print(f"\n--- Running Sparkeefy Wingman Pipeline ---")
    print(f"Situation: {situation}\n")
    
    api_key = os.environ.get("GROQ_API_KEY")
    if not api_key:
        raise ValueError("GROQ_API_KEY not found in environment variables. Please check your .env file.")
        
    client = Groq(api_key=api_key)
    
    print("1. Analyzer: Reading energy...")
    analysis = analyze_situation(client, situation)
    print(f"   [+] Energy Read: {analysis.get('energy_read')}")
    
    print("2. Generator: Drafting strategies...")
    drafts = generate_drafts(client, situation, analysis)
    suggested = drafts.get('suggested_messages', [])
    print(f"   [+] Drafted {len(suggested)} messages.")
    
    print("3. Cringe Detector: Validating and filtering...")
    final_output = validate_response(client, situation, analysis, drafts)
    
    print("\n--- Final JSON Output ---")
    print(json.dumps(final_output, indent=2))
    
    return final_output

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        situation = " ".join(sys.argv[1:])
    else:
        situation = input("Enter the texting situation: ")
        
    run_wingman_pipeline(situation)

import os
import json
import time
from dotenv import load_dotenv

# Ensure we can import from parent directory
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from app import run_wingman_pipeline

load_dotenv(override=True)

def run_evaluation():
    prompts_file = os.path.join(os.path.dirname(__file__), '..', 'tests', 'test_prompts.json')
    results_file = os.path.join(os.path.dirname(__file__), 'eval_results.json')
    
    print(f"Loading prompts from {prompts_file}...")
    with open(prompts_file, 'r') as f:
        prompts = json.load(f)
        
    results = []
    
    print(f"Running evaluation on {len(prompts)} prompts...")
    for i, item in enumerate(prompts):
        category = item.get('category')
        prompt_text = item.get('prompt')
        
        print(f"\n--- [{i+1}/{len(prompts)}] Evaluating: {category} ---")
        try:
            # Add sleep to avoid rate limits (12s to avoid 6000 TPM limit)
            if i > 0:
                time.sleep(12)
                
            output = run_wingman_pipeline(prompt_text)
            
            result_item = {
                "id": i + 1,
                "category": category,
                "prompt": prompt_text,
                "wingman_response": output.get('wingman_response'),
                "suggested_messages": output.get('suggested_messages'),
                "energy_read": output.get('energy_read'),
                "safety_flag": output.get('safety_flag'),
                "confidence": output.get('confidence'),
                # Placeholders for human evaluation
                "human_score": None,
                "tone_score": None,
                "copy_ready_score": None
            }
            results.append(result_item)
            print("[+] Success")
            
        except Exception as e:
            print(f"[-] Error processing prompt {i+1}: {e}")
            result_item = {
                "id": i + 1,
                "category": category,
                "prompt": prompt_text,
                "error": str(e)
            }
            results.append(result_item)
            
    print(f"\nSaving results to {results_file}...")
    with open(results_file, 'w') as f:
        json.dump(results, f, indent=2)
        
    print("Evaluation complete!")

if __name__ == "__main__":
    run_evaluation()

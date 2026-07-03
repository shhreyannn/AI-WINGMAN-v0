import os
import json
from groq import Groq

def validate_response(client: Groq, situation: str, analysis: dict, drafts: dict) -> dict:
    with open(os.path.join(os.path.dirname(__file__), "..", "prompts", "cringe_detector.txt"), "r") as f:
        system_instruction = f.read()
        
    model = os.environ.get("GROQ_MODEL", "llama-3.3-70b-versatile")
    
    prompt = f"Situation: {situation}\nAnalysis: {json.dumps(analysis)}\nDrafted Messages: {json.dumps(drafts)}"
    
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": system_instruction},
            {"role": "user", "content": prompt}
        ],
        response_format={"type": "json_object"},
        temperature=0.2 # Lower temperature for validation and structuring
    )
    
    content = response.choices[0].message.content
    return json.loads(content)

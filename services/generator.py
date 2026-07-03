import os
import json
from groq import Groq

def generate_drafts(client: Groq, situation: str, analysis: dict) -> dict:
    base_dir = os.path.join(os.path.dirname(__file__), "..")
    
    with open(os.path.join(base_dir, "prompts", "generator.txt"), "r") as f:
        system_prompt = f.read()
        
    with open(os.path.join(base_dir, "tone_dna.md"), "r") as f:
        tone_dna = f.read()
        
    system_instruction = system_prompt.replace("{tone_dna}", tone_dna)
    model = os.environ.get("GROQ_MODEL", "llama-3.3-70b-versatile")
    
    prompt = f"Situation: {situation}\nAnalysis: {json.dumps(analysis)}"
    
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": system_instruction},
            {"role": "user", "content": prompt}
        ],
        response_format={"type": "json_object"},
        temperature=0.7,
        max_tokens=800
    )
    
    content = response.choices[0].message.content
    return json.loads(content)

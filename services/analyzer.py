import os
import json
from pydantic import BaseModel, Field
from groq import Groq

def analyze_situation(client: Groq, situation: str) -> dict:
    with open(os.path.join(os.path.dirname(__file__), "..", "prompts", "analyzer.txt"), "r") as f:
        system_instruction = f.read()
        
    model = os.environ.get("GROQ_MODEL", "llama-3.3-70b-versatile")
    
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": system_instruction},
            {"role": "user", "content": f"Situation: {situation}"}
        ],
        response_format={"type": "json_object"},
        temperature=0.4,
        max_tokens=500
    )
    
    content = response.choices[0].message.content
    return json.loads(content)

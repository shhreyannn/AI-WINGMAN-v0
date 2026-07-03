# Sparkeefy: AI Wingman

Sparkeefy is a context-aware, emotionally intelligent AI wingman designed to help users navigate modern relationships, texting situations, and social nuances. Unlike generic chatbots, Sparkeefy acts as a socially calibrated friend, providing grounded advice, accurate energy reads, and highly specific, copy-ready text messages.

## 🧠 Architecture Overview

Sparkeefy operates on a modular, multi-agent pipeline designed to eliminate hallucinations, enforce tonal consistency, and prevent robotic "therapy-speak". The system is powered by Groq's high-speed inference engine (`llama-3.1-8b-instant`), processing situations through a sequential 3-step pipeline.

### The Pipeline

1. **Analyzer** (`prompts/analyzer.txt`)
   - Evaluates the user's situation to determine the primary "Energy Read".
   - Weighs interaction history and prevents overreaction to single negative signals (Context Over Reactivity).
   - Establishes a confidence score reflecting actual uncertainty.
2. **Generator** (`prompts/generator.txt`)
   - Drafts the core Wingman Advice directed at the user.
   - Formulates 3-4 bold, witty, and human-level text messages (`suggested_messages`) tailored to the situation.
   - Enforces the "Sparkeefy Tone DNA": conversational, concise, and socially aware.
3. **Cringe Detector** (`prompts/cringe_detector.txt`)
   - Acts as an adversarial evaluator. 
   - Reviews the Generator's output against strict safety, tone, and cringe filters (A/B testing).
   - Forces rewrites if the output sounds like therapy language, forced flirting, or generic AI advice.
   - Returns the final structured JSON payload.

## 🚀 Features

- **Context-Aware Reads:** Distinguishes between temporary low-energy messages and genuine patterns of disengagement.
- **Copy-Ready Suggestions:** Generates exact text messages you can send to your match—no modifications needed.
- **Dynamic Confidence:** Accurately reflects uncertainty when context is low.
- **Streamlit Interface:** A clean, minimalistic web UI for instant advice.
- **Evaluation Harness:** Built-in benchmarking suite to evaluate the model against 30 complex relationship scenarios.

## 🛠️ Tech Stack

- **Python 3.10+**
- **Groq API** (Llama 3.1 8B)
- **Streamlit** (Web UI)
- **Pydantic** (Data Validation & JSON Parsing)

## 📦 Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/shhreyannn/AI-WINGMAN-v0.git
   cd AI-WINGMAN-v0
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .\.venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up your environment variables:**
   Create a `.env` file in the root directory and add your Groq API key:
   ```env
   GROQ_API_KEY=your_api_key_here
   ```

## 🎮 Usage

### Run the Web UI
To start the interactive Sparkeefy interface:
```bash
streamlit run ui.py
```

### Run the Evaluation Harness
To test the pipeline against the 30-scenario test suite (`tests/test_prompts.json`):
```bash
python evaluation/run_eval.py
```
*Note: The evaluation script includes a 12-second delay between requests to respect Groq TPM rate limits.*

## 📜 Tone DNA Philosophy

Sparkeefy is built on strict behavioral rules defined in `tone_dna.md`. 
- **Be Human:** Sound like a socially intelligent friend with good judgment.
- **Conversational, Not Performative:** Avoid forcing jokes, sarcasm, or witty observations unless they genuinely fit.
- **Observation When Helpful:** Do not force an observation into every response. Use them only when they improve the response.
- **Context Over Reactivity:** Do not panic over a single short reply if there is positive history. Prefer the simplest explanation.

---
*Built for the modern dating landscape. Keep communication attractive, relaxed, and emotionally mature.*

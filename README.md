# Grid07 Cognitive Routing & RAG

AI Engineering Assignment implementation using Python + Local LLM (Ollama).

## Features

### Phase 1: Vector-Based Persona Matching
Routes incoming posts to relevant bots using TF-IDF + cosine similarity + keyword boosting.

### Phase 2: Autonomous Content Engine
Bots generate opinionated social posts using persona + external context from a mock search tool.

### Phase 3: Deep Thread RAG + Prompt Injection Defense
Bots analyze thread context and defend their stance while resisting malicious prompt injection attempts.

---

## Tech Stack

- Python
- LangChain
- Ollama
- scikit-learn

---

## Setup

## 1 Install Dependencies
pip install -r requirements.txt

## 2 Start Ollama
ollama serve

## 3 Pull Model
ollama pull phi3:mini

## 4 Run Project
python app.py

---

## Output Example

### Routing
[{'bot_id': 'A', 'score': 0.5}]

### Generated Post
{
  "bot_id": "A",
  "topic": "crypto optimism",
  "post_content": "AI and crypto are the future..."
}

### Defense Reply
Prompt tricks don't change facts. Modern EV batteries retain strong capacity beyond 3 years.

---

## Prompt Injection Defense Strategy

- Remove malicious trigger phrases
- Enforce hard system rules
- Reject apology / role-switch outputs
- Preserve original persona identity

---

## Folder Structure

grid07/
├── app.py
├── personas.py
├── router.py
├── tools.py
├── graph_engine.py
├── rag_engine.py
├── requirements.txt
├── .env.example
└── README.md
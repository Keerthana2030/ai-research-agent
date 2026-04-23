# AI Research Agent (RAG + LangGraph + FastAPI)

> Built as part of hands-on exploration into Agentic AI systems, combining RAG pipelines, LLM reasoning, and API deployment.

An autonomous AI agent that answers user queries by retrieving relevant context from a vector database and generating responses using LLMs.

---

## Features

- Semantic Search using FAISS + embeddings  
- LangGraph workflow for multi-step reasoning  
- LLM-based answer generation  
- FastAPI backend with REST API endpoints  
- Fallback mechanism for stable outputs  
- Prompt engineering for controlled responses  

---

## Architecture


User Query
↓
Retriever (FAISS + Embeddings)
↓
LangGraph Agent Workflow
↓
LLM (HuggingFace / OpenAI)
↓
Final Answer (via FastAPI API)


---

## Example

**Input:**

Why did Tesla stock drop?


**Output:**

Tesla stock dropped due to weak quarterly earnings and market volatility.


---

## Tech Stack

- Python  
- LangChain / LangGraph  
- FAISS (Vector Database)  
- HuggingFace Transformers  
- FastAPI  

---

## Setup & Run Locally

git clone https://github.com/Keerthana2030/ai-research-agent.git
cd ai-research-agent

python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt

uvicorn main:api --reload
 API Usage
POST /ask

Query:

Why did Tesla stock drop?

Response:

{
  "query": "Why did Tesla stock drop?",
  "answer": "Tesla stock dropped due to weak quarterly earnings."
}
 
## Future Improvements
- Stronger LLM integration (GPT / Mistral)
- Add conversational memory
- Multi-agent workflows
- Real-time data ingestion
- Docker deployment

## Author

Keerthana Velukati

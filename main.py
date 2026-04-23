from fastapi import FastAPI
from agent import app

api = FastAPI()

@api.get("/")
def home():
    return {"message": "AI Research Agent is running 🚀"}

@api.post("/ask")
def ask(query: str):
    result = app.invoke({
        "query": query
    })
    
    return {
        "query": query,
        "answer": result["answer"]
    }

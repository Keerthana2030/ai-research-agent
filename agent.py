from langgraph.graph import StateGraph
from typing import TypedDict
from rag import retrieve
from transformers import pipeline

generator = pipeline(
    "text-generation",
    model="distilgpt2"
)
# Define state
class AgentState(TypedDict):
    query: str
    context: list
    answer: str

# Step 1: Retrieve context
def retrieve_node(state):
    context = retrieve(state["query"])
    return {"context": context}

# Step 2: Generate answer using FREE LLM
def generate_node(state):
    context = " ".join(state["context"])

    prompt = f"Context: {context}\nQuestion: {state['query']}\nAnswer:"

    response = generator(
        prompt,
        max_new_tokens=60,
        do_sample=False
    )

    text = response[0]["generated_text"]

    # Try extracting answer
    if "Answer:" in text:
        answer = text.split("Answer:")[-1].strip()
    else:
        answer = text.strip()

    # Remove junk safely (but don’t over-clean)
    if "Question:" in answer:
        answer = answer.split("Question:")[0].strip()

    # FINAL SAFETY (important)
    if len(answer) == 0:
        answer = context[:150]  # fallback to retrieved context

    return {"answer": answer}
# Build graph
graph = StateGraph(AgentState)

graph.add_node("retrieve", retrieve_node)
graph.add_node("generate", generate_node)

graph.set_entry_point("retrieve")
graph.add_edge("retrieve", "generate")

app = graph.compile()

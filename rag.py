from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)
# Sample knowledge base
texts = [
    "Tesla stock dropped due to weak quarterly earnings.",
    "Tech stocks often fall due to market volatility and interest rate hikes.",
    "Investors react negatively to revenue misses and poor guidance."
]

# Create vector DB
db = FAISS.from_texts(texts, embeddings)

# Retrieval function
def retrieve(query):
    docs = db.similarity_search(query, k=2)
    return [doc.page_content for doc in docs]

from agent import app

query = "Why did Tesla stock drop?"

result = app.invoke({
    "query": query
})

print("\nFINAL ANSWER:\n")
print(result["answer"])

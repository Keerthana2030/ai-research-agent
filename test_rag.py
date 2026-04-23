from rag import retrieve

query = "Why did Tesla stock drop?"
results = retrieve(query)

print("Results:")
for r in results:
    print("-", r)

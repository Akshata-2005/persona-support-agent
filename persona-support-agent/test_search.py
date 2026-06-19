from src.rag_pipeline import store_documents, search_documents

store_documents()

query = "How do I reset my password?"

results = search_documents(query)

print(results)
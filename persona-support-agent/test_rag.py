from src.rag_pipeline import chunk_documents

chunks = chunk_documents()

print("Total Chunks:", len(chunks))

for chunk in chunks[:5]:
    print("\nSOURCE:", chunk["source"])
    print(chunk["text"])
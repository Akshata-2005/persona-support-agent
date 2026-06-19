from langchain_text_splitters import RecursiveCharacterTextSplitter
import chromadb
import os

client = chromadb.Client()
collection = client.get_or_create_collection("support_docs")


def load_documents():
    docs = []

    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    DATA_DIR = os.path.join(BASE_DIR, "data")

    for file in os.listdir(DATA_DIR):
        path = os.path.join(DATA_DIR, file)

        if file.endswith(".md") or file.endswith(".txt"):
            with open(path, "r", encoding="utf-8") as f:
                docs.append({
                    "source": file,
                    "content": f.read()
                })

    return docs

def store_documents():

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=300,
        chunk_overlap=50
    )

    docs = load_documents()

    for i, doc in enumerate(docs):

        chunks = splitter.split_text(doc["content"])

        for j, chunk in enumerate(chunks):

            collection.add(
                documents=[chunk],
                ids=[f"{i}_{j}"],
                metadatas=[{"source": doc["source"]}]
            )


def search_documents(query):

    results = collection.query(
        query_texts=[query],
        n_results=3
    )

    return results

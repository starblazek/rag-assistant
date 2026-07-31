from rag.loader.loader import load_documents



documents = load_documents()

for doc in documents:
    print(doc["source"])
    print(len(doc["text"]))
    print("-" * 30)
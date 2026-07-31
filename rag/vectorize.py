from rag.storage import load_chunks, save_chunks
from rag.embedding import create_embedding



def vectorize_chunks():
    chunks = load_chunks()
    print("Vectorizing chunks...")
    for chunk in chunks:
        vector = create_embedding(chunk["text"])
        chunk["embedding"] = vector
    save_chunks(chunks)

if __name__ == "__main__":
    vectorize_chunks()
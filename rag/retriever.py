from config import SIMILARITY_THRESHOLD, TOP_K
from .embedding import create_embedding
from .storage import load_chunks
from .similarity import cosine_similarity

def retrieve(question):
    results = []
    embedding_question = create_embedding(question)
    chunks = load_chunks()
    for chunk in chunks:
        score = cosine_similarity(embedding_question, chunk["embedding"])
        if score >=git --version SIMILARITY_THRESHOLD:
            results.append({
            "score": score,
            "text": chunk["text"],
            "source": chunk["source"],
            "chunk_id": chunk["chunk_id"],
            })
    sorted_results = sorted(
    results,
    key=lambda result: result["score"],
    reverse=True)

    return sorted_results[:TOP_K]


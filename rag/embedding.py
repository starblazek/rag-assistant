from config import EMBEDDING_MODEL
from ollama import embed

def create_embedding(text):
    embedding = embed(model=EMBEDDING_MODEL, input=text, )
    return embedding["embeddings"][0]



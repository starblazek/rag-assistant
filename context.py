from rag.loader import load_documents


documents = load_documents()


def get_context():
    return "\n\n".join(documents) 
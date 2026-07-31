from rag.splitter import split_document
from rag.loader.loader import load_documents
from rag.storage import save_chunks




def create_index():
    chunks = []
    documents = load_documents()
    for document in documents:
        chunks.extend(split_document(document))
    save_chunks(chunks)


if __name__ == "__main__":
    create_index()
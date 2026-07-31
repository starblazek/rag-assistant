from config import CHUNK_SIZE, CHUNK_OVERLAP


def split_document(document):
    chunks = []

    text = document["text"]
    source = document["source"]

    position = 0
    chunk_id = 0

    while position < len(text):
        chunk_text = text[position:position + CHUNK_SIZE]

        chunks.append({
            "text": chunk_text,
            "source": source,
            "chunk_id": chunk_id
        })

        chunk_id += 1
        position += CHUNK_SIZE - CHUNK_OVERLAP

    return chunks
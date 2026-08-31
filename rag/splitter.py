from config import CHUNK_SIZE, CHUNK_OVERLAP


def split_document(document):
    chunks = []

    source = document["source"]
    chunk_id = 0

    for section in document.get("sections", []):
        text = section.get("text", "")
        metadata = section.get("metadata", {})
        position = 0

        while position < len(text):
            chunk_text = text[position:position + CHUNK_SIZE].strip()

            if chunk_text:
                chunks.append({
                    "text": chunk_text,
                    "source": source,
                    "metadata": metadata.copy(),
                    "chunk_id": chunk_id
                })

                chunk_id += 1

            position += CHUNK_SIZE - CHUNK_OVERLAP

    return chunks

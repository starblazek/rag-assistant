import json
from config import CHUNKS_PATH

def save_chunks(chunks):
    with open(CHUNKS_PATH, "w", encoding="utf-8") as file:
        json.dump(chunks, file, indent=4, ensure_ascii=False)


def load_chunks():
    try:
        with open(CHUNKS_PATH, "r", encoding="utf-8") as file:
            chunks = json.load(file)
            return chunks
    except FileNotFoundError:
        return []
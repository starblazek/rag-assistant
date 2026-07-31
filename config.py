from pathlib import Path
OLLAMA_URL = "http://localhost:11434"
MODEL_NAME = "qwen3:8b"
EMBEDDING_MODEL = "bge-m3"

MAX_HISTORY = 20

CHUNK_SIZE = 500
CHUNK_OVERLAP = 100

BASE_DIR = Path(__file__).resolve().parent
CHUNKS_PATH = BASE_DIR / "storage" / "chunks.json"
HISTORY_PATH = BASE_DIR / "storage" / "history.json"
KNOWLEDGE_PATH = BASE_DIR / "knowledge"

TOP_K = 3
SIMILARITY_THRESHOLD = 0.78
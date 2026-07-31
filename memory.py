import json
from config import HISTORY_PATH

def load_history():
    try:
        with open(HISTORY_PATH, "r", encoding="utf-8") as file:
            history = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        history = []
    return history

history = load_history()

def save_history():
    with open(HISTORY_PATH, "w", encoding="utf-8") as file:
        json.dump(history, file, indent=4, ensure_ascii=False)


def add_message(message):
    history.append(message)
    save_history()

def get_history():
    return history

def clear_history():
    history.clear()
    save_history()
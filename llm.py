from config import MODEL_NAME

from ollama import chat


def ask_llm(messages):
    try:
        response = chat(model=MODEL_NAME, messages = messages)
        return response.message.content
    except:
        return "Ошибка Ollama"


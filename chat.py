from memory import get_history, add_message
from llm import ask_llm
from prompts import SYSTEM_PROMPT
from context import get_context

def chat(question):
    add_message({
        'role': 'user',
        'content': question
    })
    messages = [
        {
            'role': 'system',
            'content': SYSTEM_PROMPT
        }
    ]
    context = get_context()

    messages.append({
        'role': 'system',
        'content': f"Материалы курса:\n{context}"
    })

    messages.extend(get_history())
    answer = ask_llm(messages)
    add_message({
        'role': 'assistant',
        'content': answer
    })
    return answer



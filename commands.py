from memory import clear_history, get_history


def commands(command):
    if command == "/clear":
        clear_history()
        print("История очищена")
        return True

    if command == "/history":
        print("Ваша история:")
        print(get_history())
        return True

    if command == "/exit":
        return "exit"

    return False

from chat import chat
from commands import commands
from utils import print_message

while True:
    question = input("Введите текст: ")

    result = commands(question)

    if result == "exit":
        break

    if result:
        continue

    answer = chat(question)
    print_message(answer)
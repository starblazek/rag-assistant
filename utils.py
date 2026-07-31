import shutil
import textwrap


def print_message(text):
    width = shutil.get_terminal_size().columns
    print("\nAI:")
    print(textwrap.fill(text, width=width))
    print()




def load_txt(path):
    with open(path, "r", encoding="utf-8") as file:
        text = file.read()

    return {
        "text": text,
        "source": path.name
    }
from pypdf import PdfReader


def load_pdf(path):
    doc = PdfReader(path)
    parts = []

    for page in doc.pages:
        text = page.extract_text()
        if text:
            parts.append(text)

    return {
        "text": "\n".join(parts),
        "source": path.name
    }

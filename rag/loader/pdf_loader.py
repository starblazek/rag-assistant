from pypdf import PdfReader


def load_pdf(path):
    doc = PdfReader(path)
    sections = []

    for page_number, page in enumerate(doc.pages, start=1):
        text = page.extract_text()
        if text and text.strip():
            sections.append({
                "text": text,
                "metadata": {
                    "page": page_number
                }
            })

    return {
        "source": path.name,
        "sections": sections
    }

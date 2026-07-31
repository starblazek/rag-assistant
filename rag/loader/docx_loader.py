from docx import Document


def load_docx(path):
    doc = Document(path)

    parts = []

    for paragraph in doc.paragraphs:
        if paragraph.text.strip():
            parts.append(paragraph.text)

    for table in doc.tables:
        for row in table.rows:
            for cell in row.cells:
                if cell.text.strip():
                    parts.append(cell.text)

    return {
        "text": "\n".join(parts),
        "source": path.name
    }
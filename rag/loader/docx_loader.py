from docx import Document


def load_docx(path):
    doc = Document(path)

    sections = []

    for paragraph_number, paragraph in enumerate(doc.paragraphs, start=1):
        if paragraph.text.strip():
            sections.append({
                "text": paragraph.text,
                "metadata": {
                    "paragraph": paragraph_number
                }
            })

    for table_number, table in enumerate(doc.tables, start=1):
        for row in table.rows:
            for cell in row.cells:
                if cell.text.strip():
                    sections.append({
                        "text": cell.text,
                        "metadata": {
                            "table": table_number
                        }
                    })

    return {
        "source": path.name,
        "sections": sections
    }

from pptx import Presentation

def load_pptx(path):
    doc = Presentation(path)
    sections = []

    for slide_number, slide in enumerate(doc.slides, start=1):
        parts = []
        for shape in slide.shapes:

            if shape.has_text_frame:
                text = shape.text.strip()
                if text:
                    parts.append(text)

        slide_text = "\n".join(parts)
        if slide_text.strip():
            sections.append({
                "text": slide_text,
                "metadata": {
                    "slide": slide_number
                }
            })

    return {
        "source": path.name,
        "sections": sections
    }

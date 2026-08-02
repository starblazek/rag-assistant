from pptx import Presentation

def load_pptx(path):
    doc = Presentation(path)
    parts = []

    for slide in doc.slides:
        for shape in slide.shapes:

            if shape.has_text_frame:
                text = shape.text
                if text:
                    parts.append(shape.text)

    return {
        "text": "\n".join(parts),
        "source": path.name
    }

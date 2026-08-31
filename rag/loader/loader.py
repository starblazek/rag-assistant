from config import KNOWLEDGE_PATH
from .txt_loader import load_txt
from .pdf_loader import load_pdf
from .docx_loader import load_docx
from .pptx_loader import load_pptx

LOADERS = {
    ".docx": load_docx,
    ".pdf": load_pdf,
    ".pptx": load_pptx,
    ".txt": load_txt
}

def load_documents():
    documents = []
    if not KNOWLEDGE_PATH.exists():
        print(f"Knowledge directory not found: {KNOWLEDGE_PATH}")
        return documents

    for file in KNOWLEDGE_PATH.iterdir():
        if not file.is_file():
            continue

        extension = file.suffix.lower()

        loader = LOADERS.get(extension)

        if loader:
            document = loader(file)

            if has_text(document):
                documents.append(document)
            else:
                print(f"Empty document: {file.name}")
        else:
            print(f"Unsupported file: {file.name}")
    return documents


def has_text(document):
    for section in document.get("sections", []):
        if section.get("text", "").strip():
            return True
    return False


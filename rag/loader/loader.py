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
    for file in KNOWLEDGE_PATH.iterdir():
        extension = file.suffix.lower()

        loader = LOADERS.get(extension)

        if loader:
            document = loader(file)

            if document["text"].strip():
                documents.append(document)
            else:
                print(f"Empty document: {file.name}")
        else:
            print(f"Unsupported file: {file.name}")
    return documents


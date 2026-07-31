from config import KNOWLEDGE_PATH
from .docx_loader import load_docx
#from .pdf_loader import load_pdf
#from .pptx_loader import load_pptx
from .txt_loader import load_txt

LOADERS = {
    ".docx": load_docx,
    #".pdf": load_pdf,
    #".pptx": load_pptx,
    ".txt": load_txt
}

def load_documents():
    documents = []
    for file in KNOWLEDGE_PATH.iterdir():
        extension = file.suffix.lower()

        loader = LOADERS.get(extension)

        if loader:
            document = loader(file)
            documents.append(document)
        else:
            print(f"Unsupported file: {file.name}")
    return documents


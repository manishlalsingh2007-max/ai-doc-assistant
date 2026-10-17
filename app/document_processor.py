from io import BytesIO
from pypdf import PdfReader


def extract_text(filename: str, content: bytes) -> str:
    if filename.lower().endswith(".txt"):
        return content.decode("utf-8")

    if filename.lower().endswith(".pdf"):
        reader = PdfReader(BytesIO(content))
        pages = [
            page.extract_text() or ""
            for page in reader.pages
        ]
        return "\n".join(pages)

    raise ValueError("Unsupported file type")
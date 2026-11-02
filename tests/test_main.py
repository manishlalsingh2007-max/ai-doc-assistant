
from io import BytesIO

from fastapi.testclient import TestClient
from reportlab.pdfgen import canvas

from main import app

client = TestClient(app)


def create_pdf(text="Hello AI Document Assistant!"):
    buffer = BytesIO()
    pdf = canvas.Canvas(buffer)
    pdf.drawString(100, 750, text)
    pdf.save()
    return buffer.getvalue()


def create_blank_pdf():
    buffer = BytesIO()
    pdf = canvas.Canvas(buffer)
    pdf.save()
    return buffer.getvalue()


def test_health_check():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}


def test_txt_upload():
    response = client.post(
        "/documents/upload",
        files={"file": ("notes.txt", b"Hello AI Assistant", "text/plain")}
    )

    assert response.status_code == 200
    assert response.json()["extracted_text"] == "Hello AI Assistant"


def test_pdf_upload():
    response = client.post(
        "/documents/upload",
        files={
            "file": (
                "sample.pdf",
                create_pdf(),
                "application/pdf"
            )
        }
    )

    assert response.status_code == 200
    assert "Hello AI Document Assistant!" in response.json()["extracted_text"]


def test_unsupported_file():
    response = client.post(
        "/documents/upload",
        files={"file": ("notes.docx", b"Some content", "application/docx")}
    )

    assert response.status_code == 400


def test_empty_file():
    response = client.post(
        "/documents/upload",
        files={"file": ("empty.txt", b"", "text/plain")}
    )

    assert response.status_code == 400


def test_pdf_without_readable_text():
    response = client.post(
        "/documents/upload",
        files={
            "file": (
                "blank.pdf",
                create_blank_pdf(),
                "application/pdf"
            )
        }
    )

    assert response.status_code == 422
    assert response.json()["detail"] == (
        "No readable text found. The PDF may be scanned."
    )

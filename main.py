from fastapi import FastAPI, UploadFile, File, HTTPException
from app.document_processor import extract_text

app = FastAPI()


@app.get("/health")
def health_check():
    return {"status": "healthy"}


@app.post("/documents/upload")
async def upload_document(file: UploadFile = File(...)):
    if not file.filename:
        raise HTTPException(
            status_code=400,
            detail="No filename provided"
        )

    if not file.filename.lower().endswith((".txt", ".pdf")):
        raise HTTPException(
            status_code=400,
            detail="Only TXT and PDF files are supported"
        )

    content = await file.read()

    if not content:
        raise HTTPException(
            status_code=400,
            detail="The uploaded file is empty"
        )

    try:
        text = extract_text(file.filename, content)
    except UnicodeDecodeError:
        raise HTTPException(
            status_code=400,
            detail="The TXT file must use UTF-8 encoding"
        )
    except Exception as exc:
        raise HTTPException(
            status_code=400,
            detail="Could not extract text from this file"
        ) from exc

    if not text.strip():
        raise HTTPException(
            status_code=422,
            detail="No readable text found. The PDF may be scanned."
        )

    return {
        "filename": file.filename,
        "size_bytes": len(content),
        "text_characters": len(text),
        "extracted_text": text,
        "message": "Text extracted successfully"
    }
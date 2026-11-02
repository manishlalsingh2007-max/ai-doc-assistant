# AI Document Assistant

A lightweight document-processing API built with **Python, FastAPI and Docker** that extracts readable text from PDF and TXT files.

## Overview

AI Document Assistant provides an API for uploading documents, validating file formats and extracting their text content.

The application is containerised using Docker, making it easier to run consistently across different environments.

## Features

- Upload PDF documents.
- Upload TXT documents.
- Extract text from PDF files using `pypdf`.
- Extract UTF-8 text from TXT files.
- Validate file formats.
- Handle empty and unreadable documents.
- Return extracted text through a REST API.
- Automated testing with Pytest.
- Docker containerisation.

## Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| FastAPI | REST API framework |
| Uvicorn | ASGI server |
| pypdf | PDF text extraction |
| Pytest | Automated testing |
| HTTPX | API testing |
| Docker | Application containerisation |

## Project Structure

```text
ai-document-assistant/
│
├── app/
│   └── document_processor.py
│
├── tests/
│   └── test_main.py
│
├── main.py
├── requirements.txt
├── requirements-dev.txt
├── Dockerfile
├── .dockerignore
├── .gitignore
└── README.md
```

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/manishlalsingh2007-max/ai-document-assistant.git

cd ai-document-assistant
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it:

**Windows PowerShell**

```powershell
.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

Install application and development dependencies:

```bash
pip install -r requirements-dev.txt
```

### 4. Start the application

```bash
uvicorn main:app --reload
```

The API will be available at:

`http://localhost:8000`

Interactive API documentation:

`http://localhost:8000/docs`

## API Endpoints

### Health Check

`GET /health`

Checks whether the application is running.

Example response:

```json
{
  "status": "healthy"
}
```

### Upload Document

`POST /documents/upload`

Accepts PDF and TXT files through multipart form-data.

**Successful response example:**

```json
{
  "filename": "notes.txt",
  "size_bytes": 18,
  "text_characters": 18,
  "extracted_text": "Hello AI Assistant",
  "message": "Text extracted successfully"
}
```

**Validation:**

| Condition | HTTP Status |
|---|---:|
| Successful upload | 200 |
| Unsupported file type | 400 |
| Empty file | 400 |
| No readable text | 422 |

## Docker Setup

Docker allows the application to run in an isolated container without relying on the host machine's Python environment.

### 1. Build the image

```bash
docker build -t ai-document-assistant:v1 .
```

### 2. Run the container

```bash
docker run -d -p 8000:8000 --name ai-document-assistant ai-document-assistant:v1
```

### 3. Check running containers

```bash
docker ps
```

### 4. Access the application

- Health check: `http://localhost:8000/health`
- API documentation: `http://localhost:8000/docs`

### 5. Stop and remove the container

```bash
docker rm -f ai-document-assistant
```

## Running Tests

Run the automated test suite:

```bash
python -m pytest -v
```

The test suite covers:

- Health endpoint.
- TXT upload and extraction.
- PDF upload and extraction.
- Unsupported file formats.
- Empty file validation.
- PDF without readable text.

**Latest verification:** 6 tests passed.

## Future Improvements

- LLM-powered document question answering.
- Retrieval-Augmented Generation (RAG).
- Vector database integration.
- Document summarisation.
- Multiple document support.
- Authentication and persistent document storage.

## Author

**Manish Lal Singh**

B.Tech Artificial Intelligence — SRM Institute of Science and Technology

GitHub: [manishlalsingh2007-max](https://github.com/manishlalsingh2007-max)

---

*Built as part of a hands-on journey into backend engineering, AI systems and production-ready application development.*
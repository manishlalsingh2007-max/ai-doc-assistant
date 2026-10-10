# AI Document Assistant

A document-processing system designed to simplify how business documents are ingested, processed, stored, and accessed.

## Overview

Businesses work with large volumes of documents, including invoices, reports, PDFs, and legal records. Manually processing these documents can be time-consuming and make information harder to organise and retrieve.

The AI Document Assistant aims to establish a structured document-processing workflow that transforms document inputs into accessible, organised information. Future iterations will explore AI-powered information extraction, document summarisation, and question answering.

## Planned Workflow

The initial development roadmap includes:

1. **Document Input** — accept supported document files.
2. **Text Extraction** — extract readable text from supported documents.
3. **Data Storage** — store extracted content and relevant document metadata.
4. **API Layer** — expose document-processing functionality through a REST API.
5. **Testing and Reliability** — validate expected behaviour and handle errors.
6. **Containerisation** — package the application with Docker for consistent execution.

AI-powered document understanding is planned as a future extension.

## Technology Stack

* **Python** — core application logic and document processing.
* **FastAPI** — planned REST API layer.
* **SQL** — planned structured data storage.
* **Git** — version control.
* **Docker** — planned application containerisation.
* **Automated Testing** — planned validation of application behaviour.

## Project Structure

```text
ai-document-assistant/
├── app/
│   └── document_processor.py
├── tests/
├── sample_documents/
├── main.py
├── README.md
└── .gitignore
```

## Current Status

**Development stage: Initial project setup**

The repository currently contains the initial directory structure and placeholder files. The document-processing logic, API, database integration, automated tests, and Docker configuration have not yet been implemented.

Development will proceed incrementally, with functionality added and tested as each component is introduced.

## Development Goals

* Build a maintainable, modular Python application.
* Establish a reliable document-ingestion pipeline.
* Keep application logic separate from API and storage responsibilities.
* Introduce automated testing and error handling.
* Prepare the application for containerised deployment.
* Establish a foundation for future AI-powered document capabilities.

## License

A license has not yet been selected.

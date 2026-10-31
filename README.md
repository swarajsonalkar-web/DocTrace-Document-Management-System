# DocTrace — Document Management System

A document management workspace designed to simplify file uploading, organization, downloading, and basic document conversion.

**Built by Swaraj Sonalkar**

## Overview

DocTrace is a document management application that provides a centralized workspace for handling commonly used document formats.

The application uses FastAPI for backend operations, SQLite for metadata storage, and ReportLab for generating PDF documents.

## Features

- Upload documents
- Store document metadata
- Download uploaded files
- Support for PDF files
- Support for TXT and Markdown
- Image document uploads
- TXT to PDF conversion
- Markdown to PDF conversion
- File size validation
- SQLite database integration

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Backend |
| FastAPI | REST API |
| SQLite | Database |
| ReportLab | PDF generation |
| HTML5 | Structure |
| CSS3 | Styling |
| JavaScript | Frontend |

## Supported Formats

- PDF
- TXT
- MD
- DOCX
- PNG
- JPG
- JPEG

## Project Structure

```text
DOCTRACE/
├── app.py
├── doctrace.db
├── requirements.txt
├── README.md
├── uploads/
└── static/
    ├── index.html
    ├── style.css
    └── app.js
```

## Installation

**1. Clone the repository**

```bash
git clone https://github.com/swarajsonalkar-web/DocTrace.git
cd DocTrace
```

**2. Create a virtual environment**

```bash
python -m venv .venv
```

**3. Activate the environment**

```bash
source .venv/bin/activate
```

**4. Install dependencies**

```bash
pip install -r requirements.txt
```

**5. Start the application**

```bash
uvicorn app:app --reload --port 8003
```

Open: http://127.0.0.1:8003

## Future Improvements

- Full PDF editing functionality
- OCR-based scanned document recognition
- PDF merging and splitting
- File format conversion
- Document preview
- Advanced document search
- User authentication
- Cloud storage integration

## Developer

**Swaraj Sonalkar**

GitHub: https://github.com/swarajsonalkar-web

Email: swarajsonalkar99@gmail.com

---

*Transforming document management into a simpler digital experience.*

Make a separate static in oroject directory and then paste the html,css and javascript file.

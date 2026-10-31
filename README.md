# DocTrace — Document Workspace
FastAPI + SQLite document upload/library MVP.
Run: `pip install -r requirements.txt` then `uvicorn app:app --reload --port 8003`.
Open http://127.0.0.1:8003.
Supports PDF, TXT, MD, DOCX and common image uploads (10 MB max); converts TXT/MD to PDF. This is not a full PDF editor or OCR system. Uploaded files stay in the local `uploads` folder. Do not deploy publicly without authentication and storage protections.

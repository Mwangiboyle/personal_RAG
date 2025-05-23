from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
from pathlib import Path
import os

app = FastAPI(title="Welcome to RAG fastapi endpoint")

# Configuration
UPLOAD_DIR = "uploaded_pdfs"
MAX_FILE_SIZE = 10 * 1024 * 1024  # 10MB in bytes
ALLOWED_EXTENSIONS = {".pdf"}

# Create upload directory if it doesn't exist
os.makedirs(UPLOAD_DIR, exist_ok=True)

def validate_pdf_file(file: UploadFile) -> bool:
    '''Validate that the uploaded file is actually a PDF'''
    file_extension = Path(file.filename).suffix.lower()
    if file_extension not in ALLOWED_EXTENSIONS:
        return False
    
    file_content = file.file.read(2048)
    file.file.seek(0)
    
    try:
        mime_
    except:

@app.post
@app.post("/welcome")
async def root():
    return f"Welcome to my fastapi"


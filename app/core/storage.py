# app/core/storage.py
import os
import shutil
from fastapi import UploadFile
from app.core.exceptions import StorageUploadError

# Define the target directory inside your workspace mimicking the WP Arena hierarchy
UPLOAD_DIR = os.path.join(os.getcwd(), "wp_arena_storage")

# Ensure the upload directory directory tree exists at application boot
os.makedirs(UPLOAD_DIR, exist_ok=True)

async def save_manuscript_file(file: UploadFile) -> str:
    """Accepts an incoming web file and streams it onto the local disk space context."""
    # Enforce standard manuscript file type validation rules
    allowed_extensions = [".pdf", ".docx", ".doc"]
    file_ext = os.path.splitext(file.filename)[1].lower()
    
    if file_ext not in allowed_extensions:
        raise StorageUploadError(
            message=f"Invalid file format '{file_ext}'. Only PDF and Word documents are permitted."
        )
        
    # Generate a clean system destination filepath
    safe_filename = f"manuscript_{file.filename}"
    destination_path = os.path.join(UPLOAD_DIR, safe_filename)
    
    try:
        print(f"[STORAGE] Commencing stream transfer for: {file.filename} to disk space.")
        with open(destination_path, "wb") as buffer:
            # Stream the file content chunks to handle large payloads efficiently without ram bloat
            shutil.copyfileobj(file.file, buffer)
            
        print(f"[STORAGE] Stream successfully finalized at: {destination_path}")
        return destination_path
    except Exception as e:
        # Fallback tracking if disk partition writes fail
        raise StorageUploadError(message=f"System failed to write payload to disk repository: {str(e)}")
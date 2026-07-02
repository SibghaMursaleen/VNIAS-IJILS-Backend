from fastapi import APIRouter, Depends, status, Form, UploadFile, File, HTTPException
from app.core.dependencies import get_db
from app.schemas.manuscripts import ManuscriptCreate

router = APIRouter(prefix='/manuscripts', tags=['Manuscripts'])

@router.get('/')
async def get_manuscripts_stub():
    return {"message": "Manuscripts fetch stub working"}

# Older JSON payload endpoint
@router.post('/', status_code=status.HTTP_201_CREATED)
async def submit_manuscript(payload: ManuscriptCreate, db=Depends(get_db)):
    print(f"[ROUTE] Passed advanced validation for manuscript: {payload.title}")
    return {
        "message": "Manuscript advanced validation successful!",
        "title": payload.title,
        "orcid_validated": payload.orcid
    }

# NEW: Day 5 Endpoint handling combined Form fields and File Uploads
@router.post('/submit-with-file', status_code=status.HTTP_201_CREATED)
async def submit_manuscript_with_file(
    title: str = Form(...),                        # Text input from a form field
    manuscript_file: UploadFile = File(...),       # File input
    db=Depends(get_db)
):
    # Enforce standard VNIAS security constraint: Only PDF files accepted
    if manuscript_file.content_type != "application/pdf":
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail="Invalid file type. Only PDF files are accepted."
        )
        
    print(f"[ROUTE] Form received: Title='{title}' | File='{manuscript_file.filename}'")
    return {
        "message": "Form text and file uploaded successfully!",
        "received_title": title,
        "filename": manuscript_file.filename,
        "content_type": manuscript_file.content_type
    }
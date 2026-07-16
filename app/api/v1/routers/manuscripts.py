# app/api/v1/routers/manuscripts.py
from fastapi import APIRouter, Depends, UploadFile, File, status
from app.core.dependencies import get_db
from app.repositories.manuscript_repo import ManuscriptRepository
from app.core.storage import save_manuscript_file  # Import your storage asset

router = APIRouter(prefix='/manuscripts', tags=['Manuscripts'])

@router.get('/')
async def get_manuscripts_stub():
    return {"message": "Manuscripts fetch stub working"}

@router.get('/repo-test/{ms_id}')
async def test_repository_layer(ms_id: int, db=Depends(get_db)):
    repo = ManuscriptRepository(db)
    manuscript = await repo.get_by_id(ms_id)
    if not manuscript:
        from app.core.exceptions import ManuscriptNotFoundError
        raise ManuscriptNotFoundError(manuscript_id=ms_id)
    return {"message": "Repository query successfully processed cleanly!", "data": manuscript}

# --- Brand New Week 2 File Upload Testing Endpoint ---
@router.post('/upload', status_code=status.HTTP_201_CREATED)
async def upload_manuscript_document(file: UploadFile = File(...)):
    # Pass incoming file straight to your sandboxed storage utility engine
    saved_path = await save_manuscript_file(file)
    
    return {
        "status": "success",
        "filename": file.filename,
        "saved_location": saved_path,
        "message": "File successfully isolated and stored inside the WP Arena sandbox environment."
    }
# app/api/v1/routers/manuscripts.py (Append to the bottom)

@router.get('/author/{author_id}/slim')
async def get_slim_manuscripts(author_id: int, db=Depends(get_db)):
    """
    Performance-optimized endpoint returning only essential metadata columns 
    to reduce system payload size.
    """
    repo = ManuscriptRepository(db)
    slim_data = await repo.get_slim_author_manuscripts(author_id)
    return {
        "status": "success",
        "author_id": author_id,
        "count": len(slim_data),
        "data": slim_data
    }
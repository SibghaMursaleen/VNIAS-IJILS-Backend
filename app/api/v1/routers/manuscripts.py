from fastapi import APIRouter, Depends, status
from app.core.dependencies import get_db

router = APIRouter(prefix='/manuscripts', tags=['Manuscripts'])

@router.get('/')
async def get_manuscripts_stub():
    return {"message": "Manuscripts fetch stub working"}

# Injecting get_db into our POST endpoint
@router.post('/', status_code=status.HTTP_201_CREATED)
async def submit_manuscript(db=Depends(get_db)):
    # Your endpoint can now use 'db' to talk to the database safely!
    print("[ROUTE] Executing submit_manuscript business logic...")
    return {
        "message": "Manuscript submission stub working",
        "database_status": "Connected via injected dependency"
    }
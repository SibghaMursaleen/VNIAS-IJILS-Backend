from fastapi import APIRouter, Depends, status
from app.core.dependencies import get_db

router = APIRouter(prefix='/manuscripts', tags=['Manuscripts'])

@router.get('/')
async def get_manuscripts_stub():
    return {"message": "Manuscripts fetch stub working"}
@router.post('/', status_code=status.HTTP_201_CREATED)
async def submit_manuscript(db=Depends(get_db)):
    print("[ROUTE] Executing submit_manuscript business logic...")
    return {
        "message": "Manuscript submission stub working",
        "database_status": "Connected via injected dependency"
    }
# User management endpoints
from fastapi import APIRouter

router = APIRouter(prefix='/users', tags=['Users'])

@router.get('/')
async def get_users_stub():
    return {"message": "Users fetch stub working"}

@router.post('/')
async def create_user_stub():
    return {"message": "User creation stub working"}
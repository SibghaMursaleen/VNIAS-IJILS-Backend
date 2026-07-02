# Authentication endpoints (login, register, token refresh)
from fastapi import APIRouter

router = APIRouter(prefix='/auth', tags=['Authentication'])

@router.post('/register')
async def register_stub():
    return {"message": "User registration stub working"}

@router.post('/login')
async def login_stub():
    return {"message": "User login stub working"}

@router.post('/refresh')
async def refresh_token_stub():
    return {"message": "Token refresh stub working"}

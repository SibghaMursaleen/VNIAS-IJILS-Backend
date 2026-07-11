# app/api/v1/routers/users.py
from fastapi import APIRouter, status
from app.schemas.users import UserCreate
from app.core.security import hash_password  # Import your new hashing tool

router = APIRouter(prefix='/users', tags=['Users'])

@router.get('/')
async def get_users_stub():
    return {"message": "Users fetch stub working"}

@router.post('/', status_code=status.HTTP_201_CREATED)
async def create_user(payload: UserCreate):
    # Hash the password securely right after validation passes
    secured_hash = hash_password(payload.password)
    
    print(f"[SECURITY] Raw password encrypted for user: {payload.email}")
    print(f"[SECURITY] Generated Hash: {secured_hash}")
    
    return {
        "message": "User registration validation and encryption complete!",
        "user_email": payload.email,
        "hashed_password_preview": secured_hash  # In production, never return this field!
    }
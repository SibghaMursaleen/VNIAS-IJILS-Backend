from fastapi import APIRouter, status
from app.schemas.users import UserCreate

router = APIRouter(prefix='/users', tags=['Users'])

@router.get('/')
async def get_users_stub():
    return {"message": "Users fetch stub working"}

# FastAPI will now automatically validate the incoming request body using UserCreate!
@router.post('/', status_code=status.HTTP_201_CREATED)
async def create_user(payload: UserCreate):
    print(f"[ROUTE] Input validation passed for user: {payload.email}")
    return {
        "message": "User validation successful!",
        "user_email": payload.email
    }
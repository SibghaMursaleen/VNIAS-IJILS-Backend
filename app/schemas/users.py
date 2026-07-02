from pydantic import BaseModel, Field, EmailStr, field_validator

class UserCreate(BaseModel):
    email: EmailStr
    password: str = Field(..., min_length=8, description="Password must be at least 8 characters long")

    @field_validator('password')
    @classmethod
    def validate_password_strength(cls, v: str) -> str:
        # Check if at least one character in the password is a digit
        if not any(char.isdigit() for char in v):
            raise ValueError('Password must contain at least one numeric digit.')
        return v
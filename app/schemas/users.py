# app/schemas/users.py
from pydantic import BaseModel, Field, EmailStr, field_validator

class UserCreate(BaseModel):
    email: EmailStr
    # Enforce a secure minimum layout while safely staying under bcrypt's 72-byte maximum limit!
    password: str = Field(..., min_length=8, max_length=71, description="Password must be between 8 and 71 characters.")

    @field_validator('password')
    @classmethod
    def validate_password_strength(cls, v: str) -> str:
        if not any(char.isdigit() for char in v):
            raise ValueError("Password must contain at least one digit.")
        return v
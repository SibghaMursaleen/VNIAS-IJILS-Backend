from pydantic import BaseModel, Field, EmailStr
from typing import Optional

class ManuscriptCreate(BaseModel):
    title: str = Field(..., min_length=10, max_length=500)
    abstract: str = Field(..., min_length=100, max_length=3000)
    corresponding_author_email: EmailStr
    # Validates standard 4-4-4-4 digit ORCID structure
    orcid: Optional[str] = Field(None, pattern=r'^\d{4}-\d{4}-\d{4}-\d{3}[0-9X]$')
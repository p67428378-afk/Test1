from datetime import date, datetime
from typing import Optional, Dict, Any
from uuid import UUID, uuid4
from pydantic import BaseModel, Field, EmailStr

class ApplicantBase(BaseModel):
    first_name: str = Field(..., min_length=1, max_length=100)
    last_name: str = Field(..., min_length=1, max_length=100)
    date_of_birth: date
    address: Dict[str, Any] # Using Dict for JSONB/TEXT address
    phone_number: str = Field(..., min_length=10, max_length=20)
    email: EmailStr
    social_security_number: str = Field(..., min_length=9, max_length=11) # Encrypted representation

class ApplicantCreate(ApplicantBase):
    pass

class Applicant(ApplicantBase):
    applicant_id: UUID = Field(default_factory=uuid4)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        from_attributes = True

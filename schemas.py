
from datetime import date
from typing import Optional

from pydantic import BaseModel, EmailStr

# Card Schemas
class CardBase(BaseModel):
    name: str
    description: str
    features: str
    apr: str
    annual_fee: str
    eligibility_criteria: str
    terms_conditions_url: str

class CardCreate(CardBase):
    pass

class Card(CardBase):
    card_id: int

    class Config:
        from_attributes = True

# Applicant Schemas
class ApplicantBase(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    phone_number: str
    date_of_birth: str # Will be encrypted in real app
    ssn: str # Will be encrypted in real app
    address: str

class ApplicantCreate(ApplicantBase):
    pass

class Applicant(ApplicantBase):
    applicant_id: int

    class Config:
        from_attributes = True

# Application Schemas
class ApplicationBase(BaseModel):
    applicant_id: int
    card_id: int
    employment_status: str
    annual_income: str # Will be encrypted in real app
    existing_debts: str # Will be encrypted in real app
    consent_credit_check: bool

class ApplicationCreate(ApplicationBase):
    pass

class Application(ApplicationBase):
    application_id: int
    submission_date: date
    status: str

    class Config:
        from_attributes = True

# Document Schemas
class DocumentBase(BaseModel):
    application_id: int
    document_type: str
    storage_path: str
    upload_date: date
    encrypted: bool

class DocumentCreate(DocumentBase):
    pass

class Document(DocumentBase):
    document_id: int

    class Config:
        from_attributes = True

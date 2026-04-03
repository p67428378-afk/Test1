
from datetime import date
from typing import Optional, List
from pydantic import BaseModel, Field, EmailStr, validator
import re

class CreditCardOfferBase(BaseModel):
    name: str
    description: str
    apr: float
    annual_fee: float
    rewards_program: Optional[str] = None
    eligibility_criteria: Optional[str] = None

class CreditCardOfferCreate(CreditCardOfferBase):
    pass

class CreditCardOffer(CreditCardOfferBase):
    id: str

    class Config:
        from_attributes = True

class ApplicantBase(BaseModel):
    first_name: str
    last_name: str
    address: str
    phone_number: str
    email: EmailStr
    date_of_birth: date

    @validator('phone_number')
    def validate_phone_number(cls, v):
        # Basic phone number validation (e.g., ###-###-#### or ##########)
        if not re.match(r'^\d{3}[-\s]?\d{3}[-\s]?\d{4}$', v):
            raise ValueError('Invalid phone number format')
        return v

class ApplicantCreate(ApplicantBase):
    pass

class ApplicantUpdateFinancial(BaseModel):
    annual_income: float = Field(..., gt=0, description="Annual income must be positive")
    credit_score: int = Field(..., ge=300, le=850, description="Credit score must be between 300 and 850")

class ApplicantUpdateEmployment(BaseModel):
    employer_name: str
    employer_address: str
    job_title: str
    employment_start_date: date

    @validator('employment_start_date')
    def validate_employment_start_date(cls, v):
        if v > date.today():
            raise ValueError('Employment start date cannot be in the future')
        return v

class Applicant(ApplicantBase):
    id: str
    annual_income: Optional[float] = None
    credit_score: Optional[int] = None
    employer_name: Optional[str] = None
    employer_address: Optional[str] = None
    job_title: Optional[str] = None
    employment_start_date: Optional[date] = None
    account_statement_ref: Optional[str] = None

    class Config:
        from_attributes = True

class ApplicationBase(BaseModel):
    applicant_id: str
    credit_card_offer_id: str

class ApplicationCreate(ApplicationBase):
    pass

class Application(ApplicationBase):
    id: str
    status: str
    submission_date: date

    class Config:
        from_attributes = True

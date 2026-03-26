from pydantic import BaseModel, Field, EmailStr, PastDate, PositiveFloat, PositiveInt, model_validator
from datetime import date
from typing import Optional

class PersonalInfoBase(BaseModel):
    first_name: str = Field(..., min_length=1, max_length=100)
    last_name: str = Field(..., min_length=1, max_length=100)
    date_of_birth: PastDate # Ensures date is in the past
    ssn: str = Field(..., pattern=r"^\d{3}-\d{2}-\d{4}$", description="Social Security Number (XXX-XX-XXXX)")
    address: str = Field(..., min_length=5, max_length=255)
    phone_number: str = Field(..., pattern=r"^\d{3}-\d{3}-\d{4}$", description="Phone number (XXX-XXX-XXXX)")
    email_address: EmailStr

    @model_validator(mode='after')
    def validate_age(self):
        today = date.today()
        age = today.year - self.date_of_birth.year - ((today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day))
        if age < 18:
            raise ValueError("Applicant must be at least 18 years old.")
        return self

class EmploymentInfoBase(BaseModel):
    employer_name: str = Field(..., min_length=1, max_length=255)
    job_title: str = Field(..., min_length=1, max_length=100)
    annual_income: PositiveFloat
    employment_start_date: PastDate # Ensures date is in the past

class FinancialInfoBase(BaseModel):
    bank_account_number: str = Field(..., min_length=5, max_length=20)
    routing_number: str = Field(..., min_length=5, max_length=15)
    credit_score: int = Field(..., ge=300, le=850, description="Credit score between 300 and 850")
    existing_debts: Optional[str] = None # Stored as JSON/Text in HLD, keeping as string for simplicity for now
    assets: Optional[str] = None # Stored as JSON/Text in HLD, keeping as string for simplicity for now

class LoanDetailsBase(BaseModel):
    loan_amount: PositiveFloat
    loan_purpose: str = Field(..., min_length=1, max_length=255)
    repayment_period_months: PositiveInt

class LoanApplicationCreate(BaseModel):
    personal_info: PersonalInfoBase
    employment_info: EmploymentInfoBase
    financial_info: FinancialInfoBase
    loan_details: LoanDetailsBase

class LoanApplicationResponse(BaseModel):
    application_id: str
    applicant_id: str
    submission_date: date
    status: str
    kyc_status: str
    credit_check_status: str

    class Config:
        from_attributes = True

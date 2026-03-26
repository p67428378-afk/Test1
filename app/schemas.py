from pydantic import BaseModel, Field
from datetime import date
from typing import Optional

class PolicyholderBase(BaseModel):
    name: str
    date_of_birth: date
    address: str
    contact_info: str
    ssn: str  # This would be encrypted in a real system
    medical_history: str # This would be encrypted in a real system

class PolicyholderCreate(PolicyholderBase):
    pass

class Policyholder(PolicyholderBase):
    policyholder_id: str

    class Config:
        from_attributes = True

class PolicyBase(BaseModel):
    policy_type: str
    start_date: date
    end_date: date
    coverage_details: str
    status: str

class PolicyCreate(PolicyBase):
    pass

class PolicyUpdate(BaseModel):
    policy_type: Optional[str] = None
    start_date: Optional[date] = None
    end_date: Optional[date] = None
    coverage_details: Optional[str] = None
    status: Optional[str] = None

class Policy(PolicyBase):
    policy_id: str
    policyholder_id: str

    class Config:
        from_attributes = True

class PolicyCreateRequest(BaseModel):
    policyholder: PolicyholderCreate
    policy: PolicyCreate

class PolicyResponse(BaseModel):
    policyholder: Policyholder
    policy: Policy

    class Config:
        from_attributes = True

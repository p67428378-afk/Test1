from pydantic import BaseModel
from typing import Optional

class PolicyBase(BaseModel):
    policy_holder_name: str
    vehicle_type: str
    ncb_years: int
    vehicle_risk_factor: float

class PolicyCreate(PolicyBase):
    pass

class Policy(PolicyBase):
    policy_id: str
    calculated_premium: float

    class Config:
        from_attributes = True

class PremiumCalculationRequest(BaseModel):
    ncb_years: int
    vehicle_risk_factor: float
    policy_holder_name: str
    vehicle_type: str

class PremiumCalculationResponse(BaseModel):
    calculated_premium: float
    policy_id: str

from pydantic import BaseModel, Field
from datetime import date

class PremiumCalculationRequest(BaseModel):
    vehicle_type: str
    no_claims_bonus_percentage: float = Field(..., ge=0.2, le=0.5)
    vehicle_multiplier: float = Field(..., ge=0.8, le=1.6)

class PolicyDetails(BaseModel):
    vehicle_type: str
    no_claims_bonus_percentage: float
    vehicle_multiplier: float
    base_premium: float

class PremiumCalculationResponse(BaseModel):
    calculated_premium: float
    policy_details: PolicyDetails

class Policy(BaseModel):
    policy_id: str
    policy_holder_name: str
    vehicle_type: str
    no_claims_bonus_percentage: float
    vehicle_multiplier: float
    base_premium: float
    calculated_premium: float
    effective_date: date
    expiry_date: date

    class Config:
        from_attributes = True

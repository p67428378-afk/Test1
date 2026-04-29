
from pydantic import BaseModel

class PolicyBase(BaseModel):
    customer_id: int
    vehicle_id: int
    base_premium: float
    ncb_tier: float
    vehicle_multiplier: float

class PolicyCreate(PolicyBase):
    pass

class Policy(PolicyBase):
    id: int
    calculated_premium: float

    class Config:
        from_attributes = True

class PremiumCalculationRequest(BaseModel):
    vehicle_details: dict
    ncb_tier: float

class PremiumCalculationResponse(BaseModel):
    calculated_premium: float
    base_premium: float
    ncb_applied: float
    vehicle_multiplier_applied: float

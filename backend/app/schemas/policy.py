from pydantic import BaseModel
from typing import Optional
import datetime

class VehicleBase(BaseModel):
    make: str
    model: str
    year: int
    type: str
    risk_factor: float

class VehicleCreate(VehicleBase):
    pass

class Vehicle(VehicleBase):
    id: str

    class Config:
        from_attributes = True

class PolicyholderBase(BaseModel):
    name: str
    address: str
    contact_info: str

class PolicyholderCreate(PolicyholderBase):
    pass

class Policyholder(PolicyholderBase):
    id: str

    class Config:
        from_attributes = True

class PolicyBase(BaseModel):
    base_rate: float
    ncb_years: int
    start_date: datetime.date
    end_date: datetime.date

class PolicyCreate(PolicyBase):
    policyholder_id: str
    vehicle_id: str

class Policy(PolicyBase):
    id: str
    policyholder: Policyholder
    vehicle: Vehicle
    calculated_premium: float

    class Config:
        from_attributes = True

class PremiumCalculationRequest(BaseModel):
    base_rate: float
    ncb_years: int
    vehicle_multiplier: float

class PremiumCalculationResponse(BaseModel):
    calculated_premium: float

from pydantic import BaseModel, ConfigDict
from typing import Optional

class PremiumCalculationRequest(BaseModel):
    ncb_years: int
    vehicle_make: str
    vehicle_model: str
    vehicle_year: int
    engine_size_cc: int

class PremiumCalculationResponse(BaseModel):
    premium: float

class Customer(BaseModel):
    id: Optional[str] = None
    name: str
    email: str
    phone: str

    model_config = ConfigDict(from_attributes=True)

class Vehicle(BaseModel):
    id: Optional[str] = None
    vin: str
    make: str
    model: str
    year: int
    engine_size_cc: int

    model_config = ConfigDict(from_attributes=True)

class Policy(BaseModel):
    id: Optional[str] = None
    customer: Customer
    vehicle: Vehicle
    base_premium: float
    ncb_years: int
    ncb_discount_percentage: float
    vehicle_multiplier: float
    final_premium: float

    model_config = ConfigDict(from_attributes=True)

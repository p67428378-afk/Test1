from pydantic import BaseModel

class PremiumRequest(BaseModel):
    ncb_level: str
    vehicle_make: str
    vehicle_model: str
    vehicle_year: int
    vehicle_type: str

class PremiumResponse(BaseModel):
    calculated_premium: float

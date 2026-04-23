import uuid
from sqlalchemy import Column, Integer, String, Float, DateTime, func
from .database import Base

def generate_uuid():
    return str(uuid.uuid4())

class Policy(Base):
    __tablename__ = "policies"

    policy_id = Column(String, primary_key=True, default=generate_uuid)
    policy_holder_name = Column(String, index=True)
    vehicle_type = Column(String)
    ncb_years = Column(Integer)
    vehicle_risk_factor = Column(Float)
    base_premium = Column(Float, default=500.0)
    ncb_discount_percentage = Column(Float)
    vehicle_multiplier_applied = Column(Float)
    calculated_premium = Column(Float)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

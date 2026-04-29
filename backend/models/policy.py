
from sqlalchemy import Column, Integer, String, Float
from backend.database import Base

class Policy(Base):
    __tablename__ = "policies"

    id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(Integer, index=True)
    vehicle_id = Column(Integer, index=True)
    base_premium = Column(Float)
    ncb_tier = Column(Float)
    vehicle_multiplier = Column(Float)
    calculated_premium = Column(Float)

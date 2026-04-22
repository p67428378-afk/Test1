from sqlalchemy import Column, String, Float, Date, DateTime
from sqlalchemy.dialects.postgresql import UUID
import uuid
from datetime import datetime
from app.core.database import Base

class Policy(Base):
    __tablename__ = "policies"

    policy_id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    policy_holder_name = Column(String)
    vehicle_type = Column(String)
    no_claims_bonus_percentage = Column(Float)
    vehicle_multiplier = Column(Float)
    base_premium = Column(Float, default=500.0)
    calculated_premium = Column(Float)
    effective_date = Column(Date)
    expiry_date = Column(Date)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

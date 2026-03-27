import uuid
from sqlalchemy import Column, String, Float, Text, DateTime
from sqlalchemy.sql import func
from backend.core.database import Base, JSONEncodedDict

class Claim(Base):
    __tablename__ = "claims"

    claim_id = Column(String, primary_key=True, index=True, default=lambda: str(uuid.uuid4()))
    claim_type = Column(String, index=True) # Enum: AUTO, HEALTH, PROPERTY
    claimant_name = Column(String, index=True)
    policy_number = Column(String, unique=True, index=True)
    claim_amount = Column(Float)
    incident_description = Column(Text)
    document_references = Column(JSONEncodedDict) # Use custom type
    status = Column(String, default="PENDING") # Enum: PENDING, SIMPLE_APPROVED, COMPLEX_REVIEW, AI_SUMMARIZED
    created_at = Column(DateTime, server_default=func.now()) # Removed timezone=True
    updated_at = Column(DateTime, onupdate=func.now()) # Removed timezone=True
    approved_by_agent_id = Column(String, nullable=True) # Foreign Key to Agent, Nullable
    ai_summary = Column(Text, nullable=True)
    complexity_score = Column(Float, nullable=True)

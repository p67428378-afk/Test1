from sqlalchemy import Column, String, DateTime, Float, Text
from sqlalchemy.sql import func
import uuid
from backend.database import Base # Import Base from database.py

class Claim(Base):
    __tablename__ = "claims"

    claim_id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    claim_type = Column(String, index=True) # Enum: AUTO, HEALTH, PROPERTY
    claimant_name = Column(String, index=True)
    policy_number = Column(String, unique=True, index=True)
    claim_amount = Column(Float)
    incident_description = Column(Text)
    document_references = Column(Text) # Storing as JSON string or comma-separated paths
    status = Column(String, default="PENDING") # Enum: PENDING, SIMPLE_APPROVED, COMPLEX_REVIEW, AI_SUMMARIZED
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    approved_by_agent_id = Column(String,  nullable=True) # Foreign Key to Agent
    ai_summary = Column(Text, nullable=True)
    complexity_score = Column(Float, nullable=True)

class Agent(Base):
    __tablename__ = "agents"

    agent_id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    password_hash = Column(String)
    role = Column(String) # Enum: AGENT, ADJUSTER, ADMIN
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

class AuditLog(Base):
    __tablename__ = "audit_logs"

    log_id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    claim_id = Column(String) # Foreign Key to Claim
    agent_id = Column(String, nullable=True) # Foreign Key to Agent
    action = Column(String) # e.g., CLAIM_SUBMITTED, CLAIM_APPROVED, AI_SUMMARIZED
    details = Column(Text) # Storing as JSON string
    timestamp = Column(DateTime(timezone=True), server_default=func.now())

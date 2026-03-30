
from sqlalchemy import Column, String, Float, DateTime, Text
from app.database import Base
from datetime import datetime

class AuditLog(Base):
    __tablename__ = "audit_logs"

    audit_id = Column(String, primary_key=True, index=True)
    decision_id = Column(String, index=True)
    event_timestamp = Column(DateTime, default=datetime.utcnow)
    event_type = Column(String, index=True)
    service_name = Column(String)
    payload_snapshot = Column(Text) # Store JSON string of input payload
    result_details = Column(Text)   # Store JSON string of decision/result details
    user_id = Column(String)
    data_hash = Column(String) # For immutability check

class RiskRule(Base):
    __tablename__ = "risk_rules"

    rule_id = Column(String, primary_key=True, index=True)
    rule_name = Column(String, unique=True, index=True)
    description = Column(String)
    threshold = Column(Float)
    rule_type = Column(String) # e.g., "credit_score", "income_ratio"
    severity = Column(String) # e.g., "HIGH", "MEDIUM", "LOW"
    is_active = Column(String) # Using String for boolean to be compatible with SQLite

from pydantic import BaseModel, Field, ConfigDict
from typing import List, Optional
from datetime import datetime

class ClaimBase(BaseModel):
    claim_type: str
    claimant_name: str
    policy_number: str
    claim_amount: float
    incident_description: str
    document_references: Optional[str] = None # Storing as JSON string or comma-separated paths

class ClaimCreate(ClaimBase):
    pass

class ClaimUpdate(ClaimBase):
    status: Optional[str] = None
    approved_by_agent_id: Optional[str] = None
    ai_summary: Optional[str] = None
    complexity_score: Optional[float] = None

class ClaimApprove(BaseModel):
    approved_by_agent_id: str

class Claim(ClaimBase):
    claim_id: str
    status: str
    created_at: datetime
    updated_at: Optional[datetime] = None # Make updated_at optional
    approved_by_agent_id: Optional[str] = None
    ai_summary: Optional[str] = None
    complexity_score: Optional[float] = None

    model_config = ConfigDict(from_attributes=True)

class AgentBase(BaseModel):
    username: str
    email: str
    role: str

class AgentCreate(AgentBase):
    password: str

class Agent(AgentBase):
    agent_id: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class AuditLogBase(BaseModel):
    claim_id: str
    agent_id: Optional[str] = None
    action: str
    details: Optional[str] = None

class AuditLog(AuditLogBase):
    log_id: str
    timestamp: datetime

    model_config = ConfigDict(from_attributes=True)

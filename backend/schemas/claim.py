from typing import List, Optional
from datetime import datetime
from enum import Enum
from pydantic import BaseModel, Field

class ClaimType(str, Enum):
    AUTO = "AUTO"
    HEALTH = "HEALTH"
    PROPERTY = "PROPERTY"

class ClaimStatus(str, Enum):
    PENDING = "PENDING"
    SIMPLE_APPROVED = "SIMPLE_APPROVED"
    COMPLEX_REVIEW = "COMPLEX_REVIEW"
    AI_SUMMARIZED = "AI_SUMMARIZED"
    # Add other statuses as needed

class ClaimBase(BaseModel):
    claim_type: ClaimType
    claimant_name: str
    policy_number: str
    claim_amount: float
    incident_description: str
    document_references: List[str] = Field(default_factory=list) # Keep this here

class ClaimCreate(ClaimBase):
    pass

class ClaimUpdate(ClaimBase):
    status: Optional[ClaimStatus] = None
    approved_by_agent_id: Optional[str] = None
    ai_summary: Optional[str] = None
    complexity_score: Optional[float] = None

class ClaimResponse(ClaimBase):
    claim_id: str
    status: ClaimStatus
    created_at: datetime
    updated_at: datetime
    approved_by_agent_id: Optional[str] = None
    ai_summary: Optional[str] = None
    complexity_score: Optional[float] = None

    class Config:
        from_attributes = True # For Pydantic v2

class ClaimSummaryResponse(BaseModel):
    claim_id: str
    ai_summary: Optional[str] = None
    complexity_score: Optional[float] = None

    class Config:
        from_attributes = True # For Pydantic v2

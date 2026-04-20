from pydantic import BaseModel, ConfigDict
from typing import Optional, List
from datetime import datetime
from .models import MembershipCategory, TransactionType, RequestStatus, DocumentStatus, FinancialTransactionType

class UserBase(BaseModel):
    email: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    role: str
    model_config = ConfigDict(from_attributes=True)

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: Optional[str] = None

class MemberBase(BaseModel):
    name: str
    address: str
    contact_details: str
    email: str
    aadhaar_pan: str
    membership_category: MembershipCategory

class MemberCreate(MemberBase):
    pass

class Member(MemberBase):
    id: int
    status: str
    created_at: datetime
    updated_at: Optional[datetime] = None
    model_config = ConfigDict(from_attributes=True)

class PropertyBase(BaseModel):
    flat_number: str
    tower_unit_code: str
    area: float
    share_certificate_number: str
    legal_status: str
    dues_status: str

class PropertyCreate(PropertyBase):
    current_owner_member_id: int
    previous_owner_member_id: Optional[int] = None

class Property(PropertyBase):
    id: int
    current_owner_member_id: int
    previous_owner_member_id: Optional[int] = None
    created_at: datetime
    updated_at: Optional[datetime] = None
    model_config = ConfigDict(from_attributes=True)

class FlatTransferRequestBase(BaseModel):
    flat_id: int
    transaction_type: TransactionType

class FlatTransferRequestCreate(FlatTransferRequestBase):
    buyer_email: str
    seller_email: str

class FlatTransferRequest(FlatTransferRequestBase):
    id: int
    buyer_id: int
    seller_id: int
    request_status: RequestStatus
    initiated_by: int
    initiated_at: datetime
    approved_by: Optional[int] = None
    approved_at: Optional[datetime] = None
    application_number: str
    model_config = ConfigDict(from_attributes=True)

class DocumentBase(BaseModel):
    document_type: str
    remarks: Optional[str] = None

class DocumentCreate(DocumentBase):
    request_id: int
    file_path_url: str

class Document(DocumentBase):
    id: int
    request_id: int
    file_path_url: str
    uploaded_by: int
    uploaded_at: datetime
    status: DocumentStatus
    model_config = ConfigDict(from_attributes=True)

class FinancialTransactionBase(BaseModel):
    amount: float
    transaction_type: FinancialTransactionType
    payment_mode: str
    due_date: datetime

class FinancialTransactionCreate(FinancialTransactionBase):
    request_id: int

class FinancialTransaction(FinancialTransactionBase):
    id: int
    request_id: int
    payment_date: Optional[datetime] = None
    bank_reference: Optional[str] = None
    received_by: Optional[int] = None
    status: str
    model_config = ConfigDict(from_attributes=True)

class AuditLogBase(BaseModel):
    action: str
    entity_type: str
    entity_id: int
    old_value: Optional[str] = None
    new_value: Optional[str] = None

class AuditLogCreate(AuditLogBase):
    user_id: int

class AuditLog(AuditLogBase):
    id: int
    user_id: int
    timestamp: datetime
    model_config = ConfigDict(from_attributes=True)

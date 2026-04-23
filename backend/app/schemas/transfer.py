
from pydantic import BaseModel
from ..models.transfer import TransferStatus

class CancellationRequest(BaseModel):
    transferReferenceId: str
    accountNumber: str

class CancellationResponse(BaseModel):
    status: str
    reason: str

    class Config:
        orm_mode = True

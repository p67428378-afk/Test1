
from sqlalchemy.orm import Session
from uuid import uuid4
from ..models.transfer import Cancellation, TransferStatus
from ..schemas.transfer import CancellationResponse

class CancellationService:
    def __init__(self, db: Session):
        self.db = db

    def cancel_transfer(self, transfer_reference_id: str, account_number: str) -> CancellationResponse:
        # Mocking external system calls for now
        # In a real scenario, this would involve API calls to the payment system
        
        # 1. Validate Transfer Execution Status
        is_executed = self._check_if_executed(transfer_reference_id)
        
        if is_executed:
            return CancellationResponse(status="TOO LATE", reason="Transfer already executed.")

        # 2. Cancel Instruction in Payment System
        cancellation_successful = self._request_cancellation_from_payment_system(transfer_reference_id)

        if not cancellation_successful:
            return CancellationResponse(status="FAILED", reason="Payment system error.")

        # 3. Reverse Earmarked Balance
        self._reverse_earmarked_balance(account_number)

        # 4. Save cancellation record
        cancellation_record = Cancellation(
            cancellationId=str(uuid4()),
            transferReferenceId=transfer_reference_id,
            accountNumber=account_number,
            status=TransferStatus.CANCELLED,
            reason="Transfer instruction successfully revoked."
        )
        self.db.add(cancellation_record)
        self.db.commit()
        self.db.refresh(cancellation_record)

        return CancellationResponse(status="CANCELLED", reason="Transfer instruction successfully revoked.")

    def _check_if_executed(self, transfer_reference_id: str) -> bool:
        # Mock implementation
        # In a real implementation, this would call the payment system API
        if "EXECUTED" in transfer_reference_id:
            return True
        return False

    def _request_cancellation_from_payment_system(self, transfer_reference_id: str) -> bool:
        # Mock implementation
        # In a real implementation, this would call the payment system API
        if "FAIL" in transfer_reference_id:
            return False
        return True

    def _reverse_earmarked_balance(self, account_number: str):
        # Mock implementation
        # In a real implementation, this would call the account service API
        print(f"Reversing earmarked balance for account {account_number}")

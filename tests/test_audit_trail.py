
import pytest
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session
from app.main import app
from app.models import AuditLog # This will be created next
from app.schemas import LoanApplicationRequest, UnderwritingDecision
from datetime import datetime
import uuid

# Assuming client fixture is defined in conftest.py

def test_audit_log_creation(client: TestClient, session: Session):
    # Mock data for a loan application and decision
    applicant_data = LoanApplicationRequest(
        applicant_id="APP_AUDIT_001",
        income_details={"annual_income": 70000.0, "income_source": "Salary", "proof_of_income_ref": "inc_ref_001"},
        credit_score=720,
        employment_details={"employer_name": "AuditCorp", "employment_status": "Employed", "years_of_employment": 5},
        bank_statement_refs=["bs_ref_001"],
        personal_details={"name": "Audit User", "dob": "1985-01-01", "address": "123 Audit St", "pan": "AUDIT1234A", "aadhaar": "111122223333"}
    )
    
    decision_id = str(uuid.uuid4())
    audit_trail_id = str(uuid.uuid4())
    underwriting_decision = UnderwritingDecision(
        decision_id=decision_id,
        applicant_id=applicant_data.applicant_id,
        final_status="APPROVED",
        decision_timestamp=datetime.now(),
        risk_score=0.1,
        ml_score=85.0,
        rbi_check_result={"is_defaulter": False},
        triggered_rules=[],
        audit_trail_id=audit_trail_id
    )

    # Simulate logging an audit trail entry directly via the model
    audit_entry = AuditLog(
        audit_id=audit_trail_id,
        decision_id=decision_id,
        event_timestamp=datetime.now(),
        event_type="Final Decision",
        service_name="LoanUnderwritingService",
        payload_snapshot=applicant_data.model_dump_json(),
        result_details=underwriting_decision.model_dump_json(),
        user_id="system",
        data_hash="mock_hash"
    )
    session.add(audit_entry)
    session.commit()
    session.refresh(audit_entry)

    # Verify the audit log was created
    retrieved_audit = session.query(AuditLog).filter(AuditLog.audit_id == audit_trail_id).first()
    assert retrieved_audit is not None
    assert retrieved_audit.decision_id == decision_id
    assert retrieved_audit.event_type == "Final Decision"
    assert retrieved_audit.service_name == "LoanUnderwritingService"


def test_audit_log_via_underwrite_endpoint(client: TestClient, session: Session):
    applicant_data = {
        "applicant_id": "APP_AUDIT_002",
        "income_details": {"annual_income": 80000.0, "income_source": "Business", "proof_of_income_ref": "inc_ref_002"},
        "credit_score": 780,
        "employment_details": {"employer_name": "Self", "employment_status": "Self-Employed", "years_of_employment": 10},
        "bank_statement_refs": ["bs_ref_002"],
        "personal_details": {"name": "Another User", "dob": "1978-03-15", "address": "456 Audit Ave", "pan": "AUDIT5678B", "aadhaar": "444455556666"}
    }
    response = client.post("/underwrite", json=applicant_data)
    assert response.status_code == 200
    decision = response.json()
    assert decision["final_status"] == "APPROVED"
    assert "audit_trail_id" in decision

    # Verify the audit log was created in the database
    retrieved_audit = session.query(AuditLog).filter(AuditLog.audit_id == decision["audit_trail_id"]).first()
    assert retrieved_audit is not None
    assert retrieved_audit.decision_id == decision["decision_id"]
    assert retrieved_audit.event_type == "Final Decision" # Assuming the service logs this type for final decision
    assert retrieved_audit.service_name == "LoanUnderwritingService"

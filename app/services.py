
import uuid
from datetime import datetime
from typing import List, Dict, Any
from sqlalchemy.orm import Session
import hashlib

from app.schemas import LoanApplicationRequest, UnderwritingDecision
from app.models import AuditLog

def assess_risk(applicant_data: LoanApplicationRequest) -> Dict[str, Any]:
    """Mocks the risk assessment based on predefined rules."""
    triggered_rules = []
    risk_score = 0.0

    if applicant_data.credit_score < 600:
        triggered_rules.append("Low Credit Score")
        risk_score += 0.4
    elif applicant_data.credit_score < 680:
        triggered_rules.append("Borderline Credit Score")
        risk_score += 0.2

    if applicant_data.income_details.annual_income < 50000:
        triggered_rules.append("Low Annual Income")
        risk_score += 0.3

    if applicant_data.employment_details.years_of_employment < 2:
        triggered_rules.append("Limited Employment History")
        risk_score += 0.1

    # More complex rules would go here

    return {"risk_score": risk_score, "triggered_rules": triggered_rules}

def perform_ml_inference(applicant_data: LoanApplicationRequest) -> Dict[str, Any]:
    """Mocks the ML model inference service."""
    # In a real scenario, this would call an external ML model serving endpoint
    # For now, a simple mock based on credit score and income
    ml_score = (applicant_data.credit_score / 900) * 0.6 + (applicant_data.income_details.annual_income / 100000) * 0.4
    return {"ml_score": round(ml_score * 100, 2)}

def check_rbi_defaulter_list(applicant_data: LoanApplicationRequest) -> Dict[str, Any]:
    """Mocks the RBI defaulter list check."""
    # In a real scenario, this would call an external RBI API (e.g., NCRP-CFCRMS)
    # For testing purposes, we'll simulate a defaulter based on PAN
    is_defaulter = "RBIISDEFUL" in applicant_data.personal_details.pan.upper()
    return {"is_defaulter": is_defaulter, "details": "Mock RBI check result" if is_defaulter else "No record found"}

def log_audit_trail(db: Session, applicant_data: LoanApplicationRequest, decision: UnderwritingDecision) -> str:
    """Logs the audit trail to the database."""
    audit_id = str(uuid.uuid4())
    event_timestamp = datetime.utcnow()

    # Create a hash of the audit record for immutability
    # In a real system, this would be more robust, potentially including a digital signature
    audit_data_string = f"{audit_id}{decision.decision_id}{event_timestamp}{decision.final_status}{applicant_data.model_dump_json()}{decision.model_dump_json()}"
    data_hash = hashlib.sha256(audit_data_string.encode('utf-8')).hexdigest()

    audit_entry = AuditLog(
        audit_id=audit_id,
        decision_id=decision.decision_id,
        event_timestamp=event_timestamp,
        event_type="Final Decision", # This could be more granular, e.g., "Application Received", "Risk Assessed", etc.
        service_name="LoanUnderwritingService",
        payload_snapshot=applicant_data.model_dump_json(),
        result_details=decision.model_dump_json(),
        user_id="system", # In a real system, this would come from authentication context
        data_hash=data_hash
    )
    db.add(audit_entry)
    db.commit()
    db.refresh(audit_entry)
    return audit_id

def make_underwriting_decision(
    applicant_data: LoanApplicationRequest,
    risk_assessment: Dict[str, Any],
    ml_inference_result: Dict[str, Any],
    rbi_check_result: Dict[str, Any]
) -> str:
    """Determines the final underwriting status based on all assessment results."""
    if rbi_check_result["is_defaulter"]:
        return "REJECTED"

    if risk_assessment["risk_score"] > 0.5 or ml_inference_result["ml_score"] < 40:
        return "REJECTED"
    elif risk_assessment["risk_score"] < 0.1 and ml_inference_result["ml_score"] > 70:
        return "APPROVED"
    else:
        return "REVIEW"

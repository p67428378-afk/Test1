import pytest
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session
from backend.models.claim import Claim
from backend.schemas.claim import ClaimCreate, ClaimStatus

def test_create_claim(client: TestClient, session: Session):
    """
    Test that a claim can be successfully created.
    """
    claim_data = {
        "claim_type": "AUTO",
        "claimant_name": "John Doe",
        "policy_number": "POL12345",
        "claim_amount": 500.00,
        "incident_description": "Minor fender bender",
        "document_references": ["gcs://bucket/doc1.pdf"]
    }
    response = client.post("/claims/", json=claim_data)
    assert response.status_code == 200
    data = response.json()
    assert data["claim_type"] == "AUTO"
    assert data["claimant_name"] == "John Doe"
    assert data["status"] == "PENDING"
    assert "claim_id" in data

    # Verify claim is in the database
    db_claim = session.query(Claim).filter(Claim.claim_id == data["claim_id"]).first()
    assert db_claim is not None
    assert db_claim.claimant_name == "John Doe"

def test_approve_simple_claim(client: TestClient, session: Session):
    """
    Test that a simple claim can be approved.
    """
    # First, create a simple claim
    claim_data = {
        "claim_type": "AUTO",
        "claimant_name": "Jane Doe",
        "policy_number": "POL67890",
        "claim_amount": 900.00, # Under $1000 threshold for simplicity
        "incident_description": "Small scratch on bumper",
        "document_references": []
    }
    create_response = client.post("/claims/", json=claim_data)
    assert create_response.status_code == 200
    claim_id = create_response.json()["claim_id"]

    # Now, approve the claim
    approve_response = client.post(f"/claims/{claim_id}/approve")
    assert approve_response.status_code == 200
    data = approve_response.json()
    assert data["claim_id"] == claim_id
    assert data["status"] == "SIMPLE_APPROVED"

    # Verify status in database
    db_claim = session.query(Claim).filter(Claim.claim_id == claim_id).first()
    assert db_claim.status == ClaimStatus.SIMPLE_APPROVED.value

def test_flag_complex_claim_for_review(client: TestClient, session: Session):
    """
    Test that a complex claim is flagged for review (not automatically approved).
    """
    # Create a claim that exceeds the simplicity threshold
    claim_data = {
        "claim_type": "AUTO",
        "claimant_name": "Peter Pan",
        "policy_number": "POL54321",
        "claim_amount": 1500.00, # Above $1000 threshold
        "incident_description": "Major accident with multiple vehicles",
        "document_references": ["gcs://bucket/police_report.pdf"]
    }
    create_response = client.post("/claims/", json=claim_data)
    assert create_response.status_code == 200
    claim_id = create_response.json()["claim_id"]

    # Attempt to approve the claim (should not result in SIMPLE_APPROVED)
    approve_response = client.post(f"/claims/{claim_id}/approve")
    # Assuming the system would classify it as complex and not allow simple approval
    # or set its status to COMPLEX_REVIEW
    assert approve_response.status_code == 200 # Or 400 if approval is explicitly rejected
    data = approve_response.json()
    assert data["claim_id"] == claim_id
    assert data["status"] == "COMPLEX_REVIEW" # Or PENDING if approval logic prevents change

    # Verify status in database
    db_claim = session.query(Claim).filter(Claim.claim_id == claim_id).first()
    assert db_claim.status == ClaimStatus.COMPLEX_REVIEW.value

def test_get_claim_summary(client: TestClient, session: Session):
    """
    Test retrieving an AI-generated summary for a complex claim.
    """
    # First, create a complex claim and simulate AI summarization
    claim_data = {
        "claim_type": "HEALTH",
        "claimant_name": "Alice Wonderland",
        "policy_number": "HEALTH987",
        "claim_amount": 10000.00,
        "incident_description": "Complex medical procedure",
        "document_references": ["gcs://bucket/medical_records.pdf"]
    }
    create_response = client.post("/claims/", json=claim_data)
    assert create_response.status_code == 200
    claim_id = create_response.json()["claim_id"]

    # Simulate AI processing and summary update
    # In a real scenario, this would be done by the AI Integration Service
    # For testing, we'll directly update the DB or mock the AI service
    # For now, let's assume the AI service has already processed it and updated the DB
    # We'll need a way to mock this or trigger it. For this test, let's assume a direct update.
    db_claim = session.query(Claim).filter(Claim.claim_id == claim_id).first()
    db_claim.ai_summary = "AI summary: Patient underwent complex surgery, high cost, requires further review."
    db_claim.complexity_score = 0.85
    db_claim.status = ClaimStatus.AI_SUMMARIZED.value
    session.add(db_claim)
    session.commit()
    session.refresh(db_claim)

    # Request the summary
    summary_response = client.get(f"/claims/{claim_id}/summary")
    assert summary_response.status_code == 200
    data = summary_response.json()
    assert data["claim_id"] == claim_id
    assert "AI summary: Patient underwent complex surgery" in data["ai_summary"]
    assert data["complexity_score"] == 0.85

def test_get_claim_summary_no_ai_data(client: TestClient, session: Session):
    """
    Test retrieving a summary for a claim where AI data is not yet available.
    """
    # Create a claim, but don't simulate AI processing
    claim_data = {
        "claim_type": "PROPERTY",
        "claimant_name": "Bob The Builder",
        "policy_number": "PROP11223",
        "claim_amount": 2000.00,
        "incident_description": "Roof damage from storm",
        "document_references": []
    }
    create_response = client.post("/claims/", json=claim_data)
    assert create_response.status_code == 200
    claim_id = create_response.json()["claim_id"]

    # Request the summary - should indicate no summary available
    summary_response = client.get(f"/claims/{claim_id}/summary")
    assert summary_response.status_code == 200 # Or 404 if summary is not found.
    # For now, let's assume the API returns a ClaimSummary object where ai_summary can be None.
    # So, for this test, I'll check if ai_summary is None.
    data = summary_response.json()
    assert data["claim_id"] == claim_id
    assert data["ai_summary"] is None
    assert data["complexity_score"] is None

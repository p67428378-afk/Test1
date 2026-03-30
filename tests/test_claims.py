from fastapi.testclient import TestClient
from sqlalchemy.orm import Session
from backend.models import Claim
from backend.schemas import ClaimCreate

def test_create_claim(client: TestClient, session: Session):
    claim_data = {
        "claim_type": "AUTO",
        "claimant_name": "John Doe",
        "policy_number": "POL12345",
        "claim_amount": 1500.00,
        "incident_description": "Minor fender bender",
        "document_references": "path/to/doc1.pdf,path/to/doc2.jpg"
    }
    response = client.post("/claims/", json=claim_data)
    assert response.status_code == 200
    data = response.json()
    assert data["claim_type"] == "AUTO"
    assert "claim_id" in data
    assert data["status"] == "PENDING"

    # Verify in database
    claim_in_db = session.query(Claim).filter(Claim.claim_id == data["claim_id"]).first()
    assert claim_in_db is not None
    assert claim_in_db.claimant_name == "John Doe"

def test_approve_simple_claim(client: TestClient, session: Session):
    # First, create a claim
    claim_data = {
        "claim_type": "AUTO",
        "claimant_name": "Jane Doe",
        "policy_number": "POL67890",
        "claim_amount": 500.00, # Simple claim amount
        "incident_description": "Small scratch",
        "document_references": None
    }
    create_response = client.post("/claims/", json=claim_data)
    assert create_response.status_code == 200
    claim_id = create_response.json()["claim_id"]

    # Now, approve the claim
    approve_data = {"approved_by_agent_id": "agent-123"}
    response = client.post(f"/claims/{claim_id}/approve", json=approve_data)
    assert response.status_code == 200
    data = response.json()
    assert data["claim_id"] == claim_id
    assert data["status"] == "SIMPLE_APPROVED"
    assert data["approved_by_agent_id"] == "agent-123"

    # Verify in database
    claim_in_db = session.query(Claim).filter(Claim.claim_id == claim_id).first()
    assert claim_in_db.status == "SIMPLE_APPROVED"
    assert claim_in_db.approved_by_agent_id == "agent-123"

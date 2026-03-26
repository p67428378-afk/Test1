from fastapi.testclient import TestClient
from app.main import app

def test_create_new_policy(client: TestClient):
    policyholder_data = {
        "name": "John Doe",
        "date_of_birth": "1990-01-01",
        "address": "123 Main St",
        "contact_info": "john.doe@example.com",
        "ssn": "***-**-1234",
        "medical_history": "No significant history"
    }
    policy_data = {
        "policy_type": "Health",
        "start_date": "2024-01-01",
        "end_date": "2025-01-01",
        "coverage_details": "Standard",
        "status": "Active"
    }
    response = client.post("/policies/", json={
        "policyholder": policyholder_data,
        "policy": policy_data
    })
    assert response.status_code == 200
    assert response.json()["policyholder"]["name"] == "John Doe"
    assert response.json()["policy"]["policy_type"] == "Health"
    assert "policy_id" in response.json()["policy"]
    assert "policyholder_id" in response.json()["policyholder"]

def test_update_policy(client: TestClient):
    # First, create a policy to update
    policyholder_data = {
        "name": "Jane Doe",
        "date_of_birth": "1985-05-10",
        "address": "456 Oak Ave",
        "contact_info": "jane.doe@example.com",
        "ssn": "***-**-5678",
        "medical_history": "Allergies"
    }
    policy_data = {
        "policy_type": "Dental",
        "start_date": "2023-03-15",
        "end_date": "2024-03-15",
        "coverage_details": "Basic",
        "status": "Active"
    }
    create_response = client.post("/policies/", json={
        "policyholder": policyholder_data,
        "policy": policy_data
    })
    assert create_response.status_code == 200
    policy_id = create_response.json()["policy"]["policy_id"]

    # Now, update the policy
    update_data = {
        "coverage_details": "Premium",
        "status": "Pending Review"
    }
    update_response = client.put(f"/policies/{policy_id}", json=update_data)
    assert update_response.status_code == 200
    assert update_response.json()["policy_id"] == policy_id
    assert update_response.json()["coverage_details"] == "Premium"
    assert update_response.json()["status"] == "Pending Review"

def test_cancel_policy(client: TestClient):
    # First, create a policy to cancel
    policyholder_data = {
        "name": "Peter Pan",
        "date_of_birth": "1992-11-20",
        "address": "789 Neverland Rd",
        "contact_info": "peter.pan@example.com",
        "ssn": "***-**-9012",
        "medical_history": "None"
    }
    policy_data = {
        "policy_type": "Vision",
        "start_date": "2023-01-01",
        "end_date": "2024-01-01",
        "coverage_details": "Standard",
        "status": "Active"
    }
    create_response = client.post("/policies/", json={
        "policyholder": policyholder_data,
        "policy": policy_data
    })
    assert create_response.status_code == 200
    policy_id = create_response.json()["policy"]["policy_id"]

    # Now, cancel the policy
    cancel_response = client.post(f"/policies/{policy_id}/cancel")
    assert cancel_response.status_code == 200
    assert cancel_response.json()["policy_id"] == policy_id
    assert cancel_response.json()["status"] == "Cancelled"

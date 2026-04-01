
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session
from backend.models import Applicant

def test_create_applicant_invalid_email(client: TestClient):
    response = client.post(
        "/applicants",
        json={
            "full_name": "Jane Doe",
            "residential_address": "456 Oak Ave",
            "phone_number": "987-654-3210",
            "email_address": "invalid-email",
            "annual_income": 60000.0,
            "credit_score": 680,
            "employer_name": "XYZ Corp",
            "employer_address": "789 Pine St",
            "job_title": "Marketing Specialist",
            "employment_start_date": "2021-03-15",
        },
    )
    assert response.status_code == 422
    assert "value is not a valid email address" in response.json()["detail"][0]["msg"]

def test_create_applicant_duplicate_email(client: TestClient, session: Session):
    # Create an applicant first
    applicant_data = {
        "full_name": "John Doe",
        "residential_address": "123 Main St",
        "phone_number": "123-456-7890",
        "email_address": "john.doe@example.com",
        "annual_income": 50000.0,
        "credit_score": 700,
        "employer_name": "ABC Corp",
        "employer_address": "456 Elm St",
        "job_title": "Software Engineer",
        "employment_start_date": "2020-01-01",
    }
    response = client.post("/applicants", json=applicant_data)
    assert response.status_code == 201 # Expecting 201 Created

    # Attempt to create another applicant with the same email
    response = client.post("/applicants", json=applicant_data)
    assert response.status_code == 409  # Expecting 409 Conflict
    assert "Applicant with this email address already exists" in response.json()["detail"]

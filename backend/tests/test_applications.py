
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session
from backend.models import Applicant, CreditCardOffering, Application, Document
from backend.schemas import ApplicantCreate, ApplicationCreate, DocumentCreate

def test_create_applicant(client: TestClient, session: Session):
    applicant_data = {
        "full_name": "Jane Doe",
        "residential_address": "456 Oak Ave, Townsville, USA",
        "phone_number": "555-987-6543",
        "email_address": "jane.doe@example.com",
        "annual_income": 80000.00,
        "credit_score": 750,
        "employer_name": "XYZ Corp",
        "employer_address": "789 Pine St, Townsville, USA",
        "job_title": "Data Scientist",
        "employment_start_date": "2019-05-15"
    }
    response = client.post("/applicants", json=applicant_data)
    assert response.status_code == 200
    data = response.json()
    assert data["full_name"] == "Jane Doe"
    assert "applicant_id" in data

def test_create_application(client: TestClient, session: Session):
    # Create a dummy applicant
    applicant = Applicant(
        full_name="John Smith",
        residential_address="123 Main St",
        phone_number="111-222-3333",
        email_address="john.smith@example.com",
        annual_income=70000.00,
        credit_score=720,
        employer_name="ABC Inc",
        employer_address="456 Side Rd",
        job_title="Engineer",
        employment_start_date="2021-01-01"
    )
    session.add(applicant)
    session.commit()
    session.refresh(applicant)

    # Create a dummy credit card offering
    card = CreditCardOffering(
        card_name="Gold Rewards Card",
        features='{"cashback": "2% on groceries"}',
        eligibility_criteria='{"income": 60000, "credit_score": 700}',
        annual_fee=50.00,
        interest_rate=16.50
    )
    session.add(card)
    session.commit()
    session.refresh(card)

    application_data = {
        "applicant_id": applicant.applicant_id,
        "card_id": card.card_id,
        "status": "PENDING",
        "review_flag": True
    }
    response = client.post("/applications", json=application_data)
    assert response.status_code == 200
    data = response.json()
    assert data["applicant_id"] == applicant.applicant_id
    assert data["card_id"] == card.card_id
    assert "application_id" in data

def test_create_application_invalid_applicant_or_card(client: TestClient, session: Session):
    # Create a dummy credit card offering for testing non-existent applicant
    card_for_invalid_applicant = CreditCardOffering(
        card_name="Dummy Card 1",
        features='{"dummy": "feature"}',
        eligibility_criteria='{"dummy": "criteria"}',
        annual_fee=10.00,
        interest_rate=10.00
    )
    session.add(card_for_invalid_applicant)
    session.commit()
    session.refresh(card_for_invalid_applicant)

    # Test with non-existent applicant
    application_data_invalid_applicant = {
        "applicant_id": 99999,
        "card_id": card_for_invalid_applicant.card_id,
        "status": "PENDING",
        "review_flag": True
    }
    response = client.post("/applications", json=application_data_invalid_applicant)
    assert response.status_code == 404
    assert response.json() == {"detail": "Applicant not found"}

    # Create a dummy applicant for testing non-existent card
    applicant_for_invalid_card = Applicant(
        full_name="Test User",
        residential_address="Test Address",
        phone_number="111-111-1111",
        email_address="test.user@example.com",
        annual_income=50000.00,
        credit_score=600,
        employer_name="Test Employer",
        employer_address="Test Employer Address",
        job_title="Tester",
        employment_start_date="2022-01-01"
    )
    session.add(applicant_for_invalid_card)
    session.commit()
    session.refresh(applicant_for_invalid_card)

    # Test with non-existent card
    application_data_invalid_card = {
        "applicant_id": applicant_for_invalid_card.applicant_id,
        "card_id": 99999,
        "status": "PENDING",
        "review_flag": True
    }
    response = client.post("/applications", json=application_data_invalid_card)
    assert response.status_code == 404
    assert response.json() == {"detail": "Credit card offering not found"}

def test_upload_document(client: TestClient, session: Session):
    # Create a dummy applicant
    applicant = Applicant(
        full_name="Alice Wonderland",
        residential_address="1 Wonderland Lane",
        phone_number="123-456-7890",
        email_address="alice@example.com",
        annual_income=90000.00,
        credit_score=780,
        employer_name="Wonderland Corp",
        employer_address="2 Looking Glass Rd",
        job_title="Dreamer",
        employment_start_date="2018-03-01"
    )
    session.add(applicant)
    session.commit()
    session.refresh(applicant)

    # Create a dummy credit card offering
    card = CreditCardOffering(
        card_name="Premium Card",
        features='{"travel_insurance": true}',
        eligibility_criteria='{"income": 80000}',
        annual_fee=150.00,
        interest_rate=13.00
    )
    session.add(card)
    session.commit()
    session.refresh(card)

    # Create a dummy application
    application = Application(
        applicant_id=applicant.applicant_id,
        card_id=card.card_id,
        status="PENDING",
        review_flag=True
    )
    session.add(application)
    session.commit()
    session.refresh(application)

    # Upload a document
    file_content = b"This is a test document content."
    response = client.post(
        f"/applications/{application.application_id}/documents?document_type=ACCOUNT_STATEMENT",
        files={"file": ("test_statement.pdf", file_content, "application/pdf")}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["application_id"] == application.application_id
    assert data["document_type"] == "ACCOUNT_STATEMENT"
    assert data["file_name"] == "test_statement.pdf"
    assert "storage_path" in data

def test_upload_document_invalid_application(client: TestClient, session: Session):
    file_content = b"This is a test document content."
    response = client.post(
        f"/applications/99999/documents?document_type=ID_PROOF",
        files={"file": ("non_existent_app.pdf", file_content, "application/pdf")}
    )
    assert response.status_code == 404
    assert response.json() == {"detail": "Application not found"}

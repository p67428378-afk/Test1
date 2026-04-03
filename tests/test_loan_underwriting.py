
import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}

def test_successful_loan_application():
    applicant_data = {
        "applicant_id": "APP001",
        "income_details": {"annual_income": 75000.0, "income_source": "Salary", "proof_of_income_ref": "income_doc_001"},
        "credit_score": 750,
        "employment_details": {"employer_name": "Tech Solutions Inc.", "employment_status": "Employed", "years_of_employment": 5},
        "bank_statement_refs": ["bank_stmt_001.pdf"],
        "personal_details": {"name": "John Doe", "dob": "1990-01-01", "address": "123 Main St", "pan": "ABCDE1234F", "aadhaar": "123456789012"}
    }
    response = client.post("/underwrite", json=applicant_data)
    assert response.status_code == 200
    assert response.json()["final_status"] == "APPROVED"
    assert "decision_id" in response.json()
    assert "decision_timestamp" in response.json()
    assert "audit_trail_id" in response.json()

def test_rejected_loan_application_low_credit_score():
    applicant_data = {
        "applicant_id": "APP002",
        "income_details": {"annual_income": 40000.0, "income_source": "Salary", "proof_of_income_ref": "income_doc_002"},
        "credit_score": 550,  # Low credit score
        "employment_details": {"employer_name": "Retail Co.", "employment_status": "Employed", "years_of_employment": 2},
        "bank_statement_refs": ["bank_stmt_002.pdf"],
        "personal_details": {"name": "Jane Doe", "dob": "1995-05-10", "address": "456 Oak Ave", "pan": "FGHIJ5678K", "aadhaar": "987654321098"}
    }
    response = client.post("/underwrite", json=applicant_data)
    assert response.status_code == 200
    assert response.json()["final_status"] == "REJECTED"
    assert "decision_id" in response.json()
    assert "decision_timestamp" in response.json()
    assert "audit_trail_id" in response.json()

def test_review_loan_application_borderline_case():
    applicant_data = {
        "applicant_id": "APP003",
        "income_details": {"annual_income": 60000.0, "income_source": "Self-Employed", "proof_of_income_ref": "income_doc_003"},
        "credit_score": 680,  # Borderline credit score
        "employment_details": {"employer_name": "Self", "employment_status": "Self-Employed", "years_of_employment": 3},
        "bank_statement_refs": ["bank_stmt_003.pdf"],
        "personal_details": {"name": "Peter Pan", "dob": "1988-11-20", "address": "789 Pine Ln", "pan": "LMNOP9012Q", "aadhaar": "112233445566"}
    }
    response = client.post("/underwrite", json=applicant_data)
    assert response.status_code == 200
    assert response.json()["final_status"] == "REVIEW"
    assert "decision_id" in response.json()
    assert "decision_timestamp" in response.json()
    assert "audit_trail_id" in response.json()

def test_missing_required_field():
    applicant_data = {
        "applicant_id": "APP004",
        "income_details": {"annual_income": 75000.0, "income_source": "Salary", "proof_of_income_ref": "income_doc_004"},
        "credit_score": 700,
        "employment_details": {"employer_name": "Tech Solutions Inc.", "employment_status": "Employed", "years_of_employment": 5},
        "bank_statement_refs": ["bank_stmt_004.pdf"],
        # "personal_details": {"name": "Missing Field", "dob": "1990-01-01", "address": "123 Main St", "pan": "ABCDE1234F", "aadhaar": "123456789012"} # personal_details is missing
    }
    response = client.post("/underwrite", json=applicant_data)
    assert response.status_code == 422  # Unprocessable Entity for validation errors

def test_invalid_data_type():
    applicant_data = {
        "applicant_id": "APP005",
        "income_details": {"annual_income": "not_a_number", "income_source": "Salary", "proof_of_income_ref": "income_doc_005"}, # annual_income is string
        "credit_score": 700,
        "employment_details": {"employer_name": "Tech Solutions Inc.", "employment_status": "Employed", "years_of_employment": 5},
        "bank_statement_refs": ["bank_stmt_005.pdf"],
        "personal_details": {"name": "Invalid Type", "dob": "1990-01-01", "address": "123 Main St", "pan": "PQRST6789U", "aadhaar": "998877665544"}
    }
    response = client.post("/underwrite", json=applicant_data)
    assert response.status_code == 422  # Unprocessable Entity for validation errors

def test_rbi_defaulter_check_rejection():
    applicant_data = {
        "applicant_id": "APP006",
        "income_details": {"annual_income": 80000.0, "income_source": "Salary", "proof_of_income_ref": "income_doc_006"},
        "credit_score": 780,
        "employment_details": {"employer_name": "Global Corp", "employment_status": "Employed", "years_of_employment": 10},
        "bank_statement_refs": ["bank_stmt_006.pdf"],
        "personal_details": {"name": "Defaulter Test", "dob": "1980-03-15", "address": "100 High St", "pan": "RBIISDEFUL", "aadhaar": "998877665544"} # Valid PAN format, but triggers mock defaulter
    }
    response = client.post("/underwrite", json=applicant_data)
    assert response.status_code == 200
    assert response.json()["final_status"] == "REJECTED"
    assert "decision_id" in response.json()
    assert "decision_timestamp" in response.json()
    assert "audit_trail_id" in response.json()

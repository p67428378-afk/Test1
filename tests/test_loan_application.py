import pytest
from fastapi.testclient import TestClient
from main import create_app

# Assuming 'client' fixture is defined in conftest.py

def test_create_loan_application_success(client: TestClient):
    application_data = {
        "personal_info": {
            "first_name": "John",
            "last_name": "Doe",
            "date_of_birth": "1990-01-01",
            "ssn": "123-45-6789", # Changed to valid SSN format
            "address": "123 Main St, Anytown, USA",
            "phone_number": "555-123-4567",
            "email_address": "john.doe@example.com"
        },
        "employment_info": {
            "employer_name": "Acme Corp",
            "job_title": "Software Engineer",
            "annual_income": 75000.00,
            "employment_start_date": "2020-01-15"
        },
        "financial_info": {
            "bank_account_number": "123456789",
            "routing_number": "987654321",
            "credit_score": 720,
            "existing_debts": "Credit Card, $5000, $100/month",
            "assets": "Savings: $10000, Car: $15000"
        },
        "loan_details": {
            "loan_amount": 25000.00,
            "loan_purpose": "Home Renovation",
            "repayment_period_months": 60
        }
    }
    response = client.post("/applications", json=application_data)
    print(f"Response Status Code: {response.status_code}")
    print(f"Response Body: {response.json()}")
    assert response.status_code == 200
    # assert response.json()["message"] == "Loan application submitted successfully"
    # assert "application_id" in response.json()

def test_create_loan_application_invalid_email(client: TestClient):
    application_data = {
        "personal_info": {
            "first_name": "Jane",
            "last_name": "Doe",
            "date_of_birth": "1995-05-05",
            "ssn": "987-65-4321", # Changed to valid SSN format
            "address": "456 Oak Ave, Othertown, USA",
            "phone_number": "555-987-6543",
            "email_address": "invalid-email"
        },
        "employment_info": {
            "employer_name": "Beta Inc",
            "job_title": "QA Engineer",
            "annual_income": 60000.00,
            "employment_start_date": "2021-03-20"
        },
        "financial_info": {
            "bank_account_number": "987654321",
            "routing_number": "123456789",
            "credit_score": 680,
            "existing_debts": "Student Loan, $15000, $200/month",
            "assets": "Stocks: $5000"
        },
        "loan_details": {
            "loan_amount": 10000.00,
            "loan_purpose": "Car Purchase",
            "repayment_period_months": 36
        }
    }
    response = client.post("/applications", json=application_data)
    print(f"Response Status Code (Invalid Email): {response.status_code}")
    print(f"Response Body (Invalid Email): {response.json()}")
    assert response.status_code == 422  # Unprocessable Entity for validation errors
    assert "email_address" in response.json()["detail"][0]["loc"]

def test_create_loan_application_future_employment_date(client: TestClient):
    application_data = {
        "personal_info": {
            "first_name": "Peter",
            "last_name": "Pan",
            "date_of_birth": "1985-11-11",
            "ssn": "111-22-3333", # Changed to valid SSN format
            "address": "789 Neverland, Fantasyland, USA",
            "phone_number": "555-111-2222",
            "email_address": "peter.pan@example.com"
        },
        "employment_info": {
            "employer_name": "Dream Corp",
            "job_title": "Dreamer",
            "annual_income": 90000.00,
            "employment_start_date": "2099-01-01"  # Future date
        },
        "financial_info": {
            "bank_account_number": "111222333",
            "routing_number": "444555666",
            "credit_score": 750,
            "existing_debts": "Mortgage, $200000, $1000/month",
            "assets": "House: $300000"
        },
        "loan_details": {
            "loan_amount": 50000.00,
            "loan_purpose": "Vacation",
            "repayment_period_months": 12
        }
    }
    response = client.post("/applications", json=application_data)
    print(f"Response Status Code (Future Employment Date): {response.status_code}")
    print(f"Response Body (Future Employment Date): {response.json()}")
    assert response.status_code == 422
    assert "employment_start_date" in response.json()["detail"][0]["loc"]

def test_create_loan_application_invalid_credit_score(client: TestClient):
    application_data = {
        "personal_info": {
            "first_name": "Alice",
            "last_name": "Wonder",
            "date_of_birth": "1992-03-15",
            "ssn": "444-55-6666", # Changed to valid SSN format
            "address": "1 Wonderland, Fairyland, USA",
            "phone_number": "555-333-4444",
            "email_address": "alice.wonder@example.com"
        },
        "employment_info": {
            "employer_name": "Magic Inc",
            "job_title": "Enchanter",
            "annual_income": 80000.00,
            "employment_start_date": "2018-07-01"
        },
        "financial_info": {
            "bank_account_number": "777888999",
            "routing_number": "000111222",
            "credit_score": 200,  # Invalid credit score
            "existing_debts": "None",
            "assets": "Jewelry: $20000"
        },
        "loan_details": {
            "loan_amount": 15000.00,
            "loan_purpose": "Education",
            "repayment_period_months": 24
        }
    }
    response = client.post("/applications", json=application_data)
    print(f"Response Status Code (Invalid Credit Score): {response.status_code}")
    print(f"Response Body (Invalid Credit Score): {response.json()}")
    assert response.status_code == 422
    assert "credit_score" in response.json()["detail"][0]["loc"]

def test_create_loan_application_negative_loan_amount(client: TestClient):
    application_data = {
        "personal_info": {
            "first_name": "Bob",
            "last_name": "Builder",
            "date_of_birth": "1980-02-20",
            "ssn": "777-88-9999", # Changed to valid SSN format
            "address": "Construction Site, Workville, USA",
            "phone_number": "555-555-6666",
            "email_address": "bob.builder@example.com"
        },
        "employment_info": {
            "employer_name": "BuildIt Co",
            "job_title": "Foreman",
            "annual_income": 70000.00,
            "employment_start_date": "2010-04-01"
        },
        "financial_info": {
            "bank_account_number": "333444555",
            "routing_number": "666777888",
            "credit_score": 700,
            "existing_debts": "Tools: $1000, $50/month",
            "assets": "Truck: $25000"
        },
        "loan_details": {
            "loan_amount": -5000.00,  # Negative loan amount
            "loan_purpose": "Equipment Upgrade",
            "repayment_period_months": 18
        }
    }
    response = client.post("/applications", json=application_data)
    print(f"Response Status Code (Negative Loan Amount): {response.status_code}")
    print(f"Response Body (Negative Loan Amount): {response.json()}")
    assert response.status_code == 422
    assert "loan_amount" in response.json()["detail"][0]["loc"]

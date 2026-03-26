
import pytest
from fastapi.testclient import TestClient
from datetime import date

# Assuming 'client' and 'session' fixtures are defined in conftest.py

def test_read_credit_card_offers(client):
    response = client.get("/credit-card-offers/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_submit_personal_info_valid(client):
    personal_info = {
        "first_name": "John",
        "last_name": "Doe",
        "address": "123 Main St, Anytown, USA",
        "phone_number": "555-123-4567",
        "email": "john.doe@example.com",
        "date_of_birth": "1990-01-01"
    }
    response = client.post("/applicants/", json=personal_info)
    assert response.status_code == 200
    assert response.json()["first_name"] == "John"
    assert "id" in response.json()

def test_submit_personal_info_invalid_email(client):
    personal_info = {
        "first_name": "Jane",
        "last_name": "Doe",
        "address": "456 Oak Ave, Cityville, USA",
        "phone_number": "555-987-6543",
        "email": "invalid-email",
        "date_of_birth": "1992-05-10"
    }
    response = client.post("/applicants/", json=personal_info)
    assert response.status_code == 422

def test_submit_personal_info_invalid_phone(client):
    personal_info = {
        "first_name": "Jane",
        "last_name": "Doe",
        "address": "456 Oak Ave, Cityville, USA",
        "phone_number": "invalid-phone",
        "email": "jane.doe@example.com",
        "date_of_birth": "1992-05-10"
    }
    response = client.post("/applicants/", json=personal_info)
    assert response.status_code == 422

def test_submit_financial_info_valid(client, session):
    # First, create an applicant
    personal_info = {
        "first_name": "Financial",
        "last_name": "Applicant",
        "address": "789 Pine Ln, Villagetown, USA",
        "phone_number": "555-111-2222",
        "email": "financial.applicant@example.com",
        "date_of_birth": "1985-03-15"
    }
    applicant_response = client.post("/applicants/", json=personal_info)
    assert applicant_response.status_code == 200
    applicant_id = applicant_response.json()["id"]

    # Then, submit financial info
    financial_info = {
        "annual_income": 70000,
        "credit_score": 750
    }
    response = client.post(f"/applicants/{applicant_id}/financial-info", json=financial_info)
    assert response.status_code == 200
    assert response.json()["annual_income"] == 70000
    assert response.json()["credit_score"] == 750

def test_submit_financial_info_invalid_income(client, session):
    # First, create an applicant
    personal_info = {
        "first_name": "BadIncome",
        "last_name": "Applicant",
        "address": "789 Pine Ln, Villagetown, USA",
        "phone_number": "555-111-3333",
        "email": "badincome.applicant@example.com",
        "date_of_birth": "1985-03-15"
    }
    applicant_response = client.post("/applicants/", json=personal_info)
    assert applicant_response.status_code == 200
    applicant_id = applicant_response.json()["id"]

    # Then, submit financial info with invalid income
    financial_info = {
        "annual_income": -100,
        "credit_score": 700
    }
    response = client.post(f"/applicants/{applicant_id}/financial-info", json=financial_info)
    assert response.status_code == 422

def test_submit_financial_info_invalid_credit_score(client, session):
    # First, create an applicant
    personal_info = {
        "first_name": "BadScore",
        "last_name": "Applicant",
        "address": "789 Pine Ln, Villagetown, USA",
        "phone_number": "555-111-4444",
        "email": "badscore.applicant@example.com",
        "date_of_birth": "1985-03-15"
    }
    applicant_response = client.post("/applicants/", json=personal_info)
    assert applicant_response.status_code == 200
    applicant_id = applicant_response.json()["id"]

    # Then, submit financial info with invalid credit score
    financial_info = {
        "annual_income": 60000,
        "credit_score": 200
    }
    response = client.post(f"/applicants/{applicant_id}/financial-info", json=financial_info)
    assert response.status_code == 422

def test_submit_employment_info_valid(client, session):
    # First, create an applicant
    personal_info = {
        "first_name": "Employment",
        "last_name": "Applicant",
        "address": "101 Corporate Dr, Business City, USA",
        "phone_number": "555-333-4444",
        "email": "employment.applicant@example.com",
        "date_of_birth": "1980-11-20"
    }
    applicant_response = client.post("/applicants/", json=personal_info)
    assert applicant_response.status_code == 200
    applicant_id = applicant_response.json()["id"]

    # Then, submit employment info
    employment_info = {
        "employer_name": "Tech Solutions Inc.",
        "employer_address": "200 Innovation Way, Tech Park, USA",
        "job_title": "Senior Developer",
        "employment_start_date": "2018-06-01"
    }
    response = client.post(f"/applicants/{applicant_id}/employment-info", json=employment_info)
    assert response.status_code == 200
    assert response.json()["employer_name"] == "Tech Solutions Inc."

def test_submit_employment_info_invalid_date_format(client, session):
    # First, create an applicant
    personal_info = {
        "first_name": "BadDate",
        "last_name": "Applicant",
        "address": "101 Corporate Dr, Business City, USA",
        "phone_number": "555-333-5555",
        "email": "baddate.applicant@example.com",
        "date_of_birth": "1980-11-20"
    }
    applicant_response = client.post("/applicants/", json=personal_info)
    assert applicant_response.status_code == 200
    applicant_id = applicant_response.json()["id"]

    # Then, submit employment info with invalid date format
    employment_info = {
        "employer_name": "Tech Solutions Inc.",
        "employer_address": "200 Innovation Way, Tech Park, USA",
        "job_title": "Senior Developer",
        "employment_start_date": "01-06-2018"
    }
    response = client.post(f"/applicants/{applicant_id}/employment-info", json=employment_info)
    assert response.status_code == 422

def test_submit_employment_info_future_date(client, session):
    # First, create an applicant
    personal_info = {
        "first_name": "FutureDate",
        "last_name": "Applicant",
        "address": "101 Corporate Dr, Business City, USA",
        "phone_number": "555-333-6666",
        "email": "futuredate.applicant@example.com",
        "date_of_birth": "1980-11-20"
    }
    applicant_response = client.post("/applicants/", json=personal_info)
    assert applicant_response.status_code == 200
    applicant_id = applicant_response.json()["id"]

    # Then, submit employment info with future date
    future_date = (date.today().replace(year=date.today().year + 1)).isoformat()
    employment_info = {
        "employer_name": "Tech Solutions Inc.",
        "employer_address": "200 Innovation Way, Tech Park, USA",
        "job_title": "Senior Developer",
        "employment_start_date": future_date
    }
    response = client.post(f"/applicants/{applicant_id}/employment-info", json=employment_info)
    assert response.status_code == 422

import pytest
from datetime import date
from pydantic import ValidationError
from app.models import ApplicantCreate, Applicant

def test_applicant_create_valid_data():
    applicant_data = {
        "first_name": "Jane",
        "last_name": "Doe",
        "date_of_birth": "1990-01-01",
        "address": {"street": "123 Main St", "city": "Anytown", "zip": "12345"},
        "phone_number": "555-123-4567",
        "email": "jane.doe@example.com",
        "social_security_number": "XXX-XX-XXXX" # Encrypted representation
    }
    applicant = ApplicantCreate(**applicant_data)
    assert applicant.first_name == "Jane"
    assert applicant.last_name == "Doe"
    assert applicant.date_of_birth == date(1990, 1, 1)
    assert applicant.email == "jane.doe@example.com"
    assert applicant.social_security_number == "XXX-XX-XXXX"

def test_applicant_create_missing_required_field():
    applicant_data = {
        "last_name": "Doe",
        "date_of_birth": "1990-01-01",
        "address": {"street": "123 Main St", "city": "Anytown", "zip": "12345"},
        "phone_number": "555-123-4567",
        "email": "jane.doe@example.com",
        "social_security_number": "XXX-XX-XXXX"
    }
    with pytest.raises(ValidationError):
        ApplicantCreate(**applicant_data)

def test_applicant_create_invalid_date_format():
    applicant_data = {
        "first_name": "Jane",
        "last_name": "Doe",
        "date_of_birth": "01-01-1990", # Invalid format
        "address": {"street": "123 Main St", "city": "Anytown", "zip": "12345"},
        "phone_number": "555-123-4567",
        "email": "jane.doe@example.com",
        "social_security_number": "XXX-XX-XXXX"
    }
    with pytest.raises(ValidationError):
        ApplicantCreate(**applicant_data)

def test_applicant_create_invalid_email_format():
    applicant_data = {
        "first_name": "Jane",
        "last_name": "Doe",
        "date_of_birth": "1990-01-01",
        "address": {"street": "123 Main St", "city": "Anytown", "zip": "12345"},
        "phone_number": "555-123-4567",
        "email": "invalid-email", # Invalid format
        "social_security_number": "XXX-XX-XXXX"
    }
    with pytest.raises(ValidationError):
        ApplicantCreate(**applicant_data)

def test_applicant_model_full_data():
    applicant_data = {
        "applicant_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
        "first_name": "John",
        "last_name": "Doe",
        "date_of_birth": "1985-05-10",
        "address": {"street": "456 Oak Ave", "city": "Otherville", "zip": "67890"},
        "phone_number": "555-987-6543",
        "email": "john.doe@example.com",
        "social_security_number": "YYY-YY-YYYY",
        "created_at": "2023-01-01T10:00:00Z",
        "updated_at": "2023-01-01T10:00:00Z"
    }
    applicant = Applicant(**applicant_data)
    assert str(applicant.applicant_id) == "a1b2c3d4-e5f6-7890-1234-567890abcdef"
    assert applicant.first_name == "John"
    assert applicant.date_of_birth == date(1985, 5, 10)
    assert applicant.email == "john.doe@example.com"
    assert applicant.social_security_number == "YYY-YY-YYYY"

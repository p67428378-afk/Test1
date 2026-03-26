
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine, Column, Integer, String, Boolean, Date, ForeignKey, Text
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import date

# Define a temporary Base for models within the test file to avoid conflicts
# with the actual Base from database.py during initial test setup.
# This will be overridden by the conftest.py's Base.metadata.create_all(bind=engine)
# which uses the Base from database.py
Base = declarative_base()

class Card(Base):
    __tablename__ = "cards"
    card_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    description = Column(Text)
    features = Column(Text)
    apr = Column(String)
    annual_fee = Column(String)
    eligibility_criteria = Column(Text)
    terms_conditions_url = Column(String)

class Applicant(Base):
    __tablename__ = "applicants"
    applicant_id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String, unique=True, index=True)
    phone_number = Column(String)
    date_of_birth = Column(String) # Encrypted in real app, but string for test simplicity
    ssn = Column(String) # Encrypted in real app, but string for test simplicity
    address = Column(Text)

class Application(Base):
    __tablename__ = "applications"
    application_id = Column(Integer, primary_key=True, index=True)
    applicant_id = Column(Integer, ForeignKey("applicants.applicant_id"))
    card_id = Column(Integer, ForeignKey("cards.card_id"))
    submission_date = Column(Date)
    status = Column(String, default="Pending")
    employment_status = Column(String)
    annual_income = Column(String) # Encrypted in real app, but string for test simplicity
    existing_debts = Column(String) # Encrypted in real app, but string for test simplicity
    consent_credit_check = Column(Boolean)

    applicant = relationship("Applicant")
    card = relationship("Card")

class Document(Base):
    __tablename__ = "documents"
    document_id = Column(Integer, primary_key=True, index=True)
    application_id = Column(Integer, ForeignKey("applications.application_id"))
    document_type = Column(String)
    storage_path = Column(String)
    upload_date = Column(Date)
    encrypted = Column(Boolean)

    application = relationship("Application")


def test_get_all_cards(client: TestClient, session):
    # Add some dummy cards to the database
    card1 = Card(name="Card A", description="Desc A", features="Feat A", apr="10%", annual_fee="$0", eligibility_criteria="Good credit", terms_conditions_url="http://example.com/cardA")
    card2 = Card(name="Card B", description="Desc B", features="Feat B", apr="15%", annual_fee="$50", eligibility_criteria="Excellent credit", terms_conditions_url="http://example.com/cardB")
    session.add_all([card1, card2])
    session.commit()
    session.refresh(card1)
    session.refresh(card2)

    response = client.get("/cards/")
    assert response.status_code == 200
    assert len(response.json()) == 2
    assert response.json()[0]["name"] == "Card A"
    assert response.json()[1]["name"] == "Card B"

def test_get_card_by_id(client: TestClient, session):
    card = Card(name="Card C", description="Desc C", features="Feat C", apr="12%", annual_fee="$25", eligibility_criteria="Fair credit", terms_conditions_url="http://example.com/cardC")
    session.add(card)
    session.commit()
    session.refresh(card)

    response = client.get(f"/cards/{card.card_id}")
    assert response.status_code == 200
    assert response.json()["name"] == "Card C"
    assert response.json()["card_id"] == card.card_id

def test_submit_application(client: TestClient, session):
    # Create a card and applicant first
    card = Card(name="Card D", description="Desc D", features="Feat D", apr="18%", annual_fee="$75", eligibility_criteria="Any credit", terms_conditions_url="http://example.com/cardD")
    applicant = Applicant(first_name="John", last_name="Doe", email="john.doe@example.com", phone_number="123-456-7890", date_of_birth="1990-01-01", ssn="XXX-XX-XXXX", address="123 Main St")
    session.add_all([card, applicant])
    session.commit()
    session.refresh(card)
    session.refresh(applicant)

    application_data = {
        "applicant_id": applicant.applicant_id,
        "card_id": card.card_id,
        "employment_status": "Employed",
        "annual_income": "50000",
        "existing_debts": "10000",
        "consent_credit_check": True
    }

    response = client.post("/applications/", json=application_data)
    assert response.status_code == 200
    assert response.json()["status"] == "Pending"
    assert response.json()["applicant_id"] == applicant.applicant_id
    assert response.json()["card_id"] == card.card_id

    # Verify the application is in the database
    app_in_db = session.query(Application).filter(Application.applicant_id == applicant.applicant_id).first()
    assert app_in_db is not None
    assert app_in_db.status == "Pending"


def test_submit_application_invalid_data(client: TestClient):
    invalid_application_data = {
        "applicant_id": 999, # Non-existent applicant
        "card_id": 999,      # Non-existent card
        "employment_status": "Employed",
        "annual_income": "not_a_number", # Invalid income
        "existing_debts": "10000",
        "consent_credit_check": True
    }
    response = client.post("/applications/", json=invalid_application_data)
    # Expect 404 for non-existent applicant/card IDs, or 422 for Pydantic validation errors
    assert response.status_code in [404, 422]



from fastapi.testclient import TestClient
from sqlalchemy.orm import Session
from backend.models import CreditCardOffering

def test_get_credit_card_offerings(client: TestClient, session: Session):
    # Add some dummy data to the database
    card1 = CreditCardOffering(
        card_name="Platinum Rewards Card",
        features='{"points": "2x on travel, 1x on everything else"}',
        eligibility_criteria='{"income": 50000, "credit_score": 700}',
        annual_fee=99.00,
        interest_rate=15.99
    )
    card2 = CreditCardOffering(
        card_name="Travel Miles Card",
        features='{"miles": "3x on travel, 1x on everything else"}',
        eligibility_criteria='{"income": 60000, "credit_score": 720}',
        annual_fee=75.00,
        interest_rate=14.99
    )
    session.add(card1)
    session.add(card2)
    session.commit()
    session.refresh(card1)
    session.refresh(card2)

    response = client.get("/credit-cards")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) == 2

    # Check structure of returned data
    assert "card_name" in data[0]
    assert "features" in data[0]
    assert "eligibility_criteria" in data[0]
    assert "annual_fee" in data[0]
    assert "interest_rate" in data[0]
    assert data[0]["card_name"] == "Platinum Rewards Card"
    assert data[1]["card_name"] == "Travel Miles Card"

def test_get_single_credit_card_offering(client: TestClient, session: Session):
    card = CreditCardOffering(
        card_name="Student Starter Card",
        features='{"cashback": "1% on all purchases"}',
        eligibility_criteria='{"student": true, "credit_score": 650}',
        annual_fee=0.00,
        interest_rate=18.99
    )
    session.add(card)
    session.commit()
    session.refresh(card)

    response = client.get(f"/credit-cards/{card.card_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["card_name"] == "Student Starter Card"
    assert data["annual_fee"] == 0.00

    response = client.get("/credit-cards/999") # Non-existent ID
    assert response.status_code == 404

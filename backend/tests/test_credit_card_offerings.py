
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool
from main import app, get_db
from database import Base
import models
import json

# Setup test database
DATABASE_URL = "sqlite:///:memory:"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@pytest.fixture(name="db_session")
def db_session_fixture():
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()
        Base.metadata.drop_all(bind=engine)

@pytest.fixture(name="client")
def client_fixture(db_session):
    def override_get_db():
        yield db_session
    app.dependency_overrides[get_db] = override_get_db
    with TestClient(app) as client:
        yield client
    app.dependency_overrides.clear()

def test_get_credit_card_offerings_empty(client):
    response = client.get("/credit_card_offerings")
    assert response.status_code == 200
    assert response.json() == []

def test_create_credit_card_offering(client, db_session):
    card_data = {
        "card_name": "Test Card",
        "features": json.dumps(["Feature 1", "Feature 2"]),
        "eligibility_criteria": json.dumps({"age": "18+", "income": "20000+"}),
        "annual_fee": 50,
        "interest_rate": "15.99%"
    }
    response = client.post("/credit_card_offerings/", json=card_data)
    assert response.status_code == 200
    data = response.json()
    assert data["card_name"] == "Test Card"
    assert data["features"] == '["Feature 1", "Feature 2"]'
    assert data["eligibility_criteria"] == '{"age": "18+", "income": "20000+"}'
    assert data["annual_fee"] == 50
    assert data["interest_rate"] == "15.99%"
    assert "card_id" in data

    # Verify it's in the database
    response = client.get("/credit_card_offerings")
    assert response.status_code == 200
    assert len(response.json()) == 1
    assert response.json()[0]["card_name"] == "Test Card"

def test_get_credit_card_offering_by_id(client, db_session):
    card_data = {
        "card_name": "Another Card",
        "features": json.dumps(["Feature A"]),
        "eligibility_criteria": json.dumps({"age": "21+"}),
        "annual_fee": 100,
        "interest_rate": "18.50%"
    }
    post_response = client.post("/credit_card_offerings/", json=card_data)
    card_id = post_response.json()["card_id"]

    get_response = client.get(f"/credit_card_offerings/{card_id}")
    assert get_response.status_code == 200
    data = get_response.json()
    assert data["card_name"] == "Another Card"
    assert data["card_id"] == card_id

def test_get_credit_card_offering_not_found(client):
    response = client.get("/credit_card_offerings/999")
    assert response.status_code == 404
    assert response.json() == {"detail": "CreditCardOffering not found"}

def test_create_credit_card_offering_duplicate_name(client, db_session):
    card_data = {
        "card_name": "Duplicate Card",
        "features": json.dumps(["F1"]),
        "eligibility_criteria": json.dumps({"e": "E"}),
        "annual_fee": 10,
        "interest_rate": "10%"
    }
    client.post("/credit_card_offerings/", json=card_data)
    response = client.post("/credit_card_offerings/", json=card_data)
    assert response.status_code == 400
    assert response.json() == {"detail": "CreditCardOffering with this name already exists"}

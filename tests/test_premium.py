import pytest
from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)

def test_calculate_premium_success():
    response = client.post(
        "/api/v1/insurance/premium",
        json={"ncb_years": 4, "vehicle_make": "Toyota", "vehicle_model": "Camry", "vehicle_year": 2020, "engine_size_cc": 2500},
    )
    assert response.status_code == 200
    assert "premium" in response.json()
    assert response.json()["premium"] == 200.0

def test_calculate_premium_no_ncb():
    response = client.post(
        "/api/v1/insurance/premium",
        json={"ncb_years": 0, "vehicle_make": "Toyota", "vehicle_model": "Camry", "vehicle_year": 2020, "engine_size_cc": 2500},
    )
    assert response.status_code == 200
    assert "premium" in response.json()
    assert response.json()["premium"] == 400.0 # 500 * 0.8

def test_calculate_premium_max_multiplier():
    response = client.post(
        "/api/v1/insurance/premium",
        json={"ncb_years": 4, "vehicle_make": "Ferrari", "vehicle_model": "488", "vehicle_year": 2022, "engine_size_cc": 3902},
    )
    assert response.status_code == 200
    assert "premium" in response.json()
    assert response.json()["premium"] == 400.0 # 500 * 0.5 * 1.6

def test_calculate_premium_1_year_ncb():
    response = client.post(
        "/api/v1/insurance/premium",
        json={"ncb_years": 1, "vehicle_make": "Honda", "vehicle_model": "Civic", "vehicle_year": 2021, "engine_size_cc": 1500},
    )
    assert response.status_code == 200
    assert "premium" in response.json()
    assert response.json()["premium"] == 400.0 # 500 * 0.8 * 1.0

def test_calculate_premium_2_years_ncb():
    response = client.post(
        "/api/v1/insurance/premium",
        json={"ncb_years": 2, "vehicle_make": "Ford", "vehicle_model": "Focus", "vehicle_year": 2019, "engine_size_cc": 1000},
    )
    assert response.status_code == 200
    assert "premium" in response.json()
    assert response.json()["premium"] == 350.0 # 500 * 0.7 * 1.0

def test_calculate_premium_3_years_ncb():
    response = client.post(
        "/api/v1/insurance/premium",
        json={"ncb_years": 3, "vehicle_make": "BMW", "vehicle_model": "X5", "vehicle_year": 2023, "engine_size_cc": 3000},
    )
    assert response.status_code == 200
    assert "premium" in response.json()
    assert response.json()["premium"] == 300.0 # 500 * 0.6 * 1.0

def test_calculate_premium_default_multiplier():
    response = client.post(
        "/api/v1/insurance/premium",
        json={"ncb_years": 2, "vehicle_make": "Audi", "vehicle_model": "A4", "vehicle_year": 2021, "engine_size_cc": 2000},
    )
    assert response.status_code == 200
    assert "premium" in response.json()
    assert response.json()["premium"] == 350.0 # 500 * 0.7 * 1.0

def test_calculate_premium_invalid_ncb():
    response = client.post(
        "/api/v1/insurance/premium",
        json={"ncb_years": -1, "vehicle_make": "Toyota", "vehicle_model": "Camry", "vehicle_year": 2020, "engine_size_cc": 2500},
    )
    assert response.status_code == 422

def test_calculate_premium_missing_fields():
    response = client.post(
        "/api/v1/insurance/premium",
        json={"ncb_years": 4, "vehicle_make": "Toyota"},
    )
    assert response.status_code == 422

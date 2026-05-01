
import pytest
from fastapi.testclient import TestClient
from backend.main import app
from backend.app.services.premium_calculator import PremiumCalculatorService
from backend.schemas import PremiumCalculationRequest

client = TestClient(app)

# Integration Tests

def test_calculate_premium_success(client):
    response = client.post(
        "/api/v1/insurance/premium",
        json={"ncb_years": 4, "vehicle_make": "Toyota", "vehicle_model": "Camry", "vehicle_year": 2020, "engine_size_cc": 2500},
    )
    assert response.status_code == 200
    assert "premium" in response.json()
    assert response.json()["premium"] == 200.0

def test_calculate_premium_no_ncb(client):
    response = client.post(
        "/api/v1/insurance/premium",
        json={"ncb_years": 0, "vehicle_make": "Toyota", "vehicle_model": "Camry", "vehicle_year": 2020, "engine_size_cc": 2500},
    )
    assert response.status_code == 200
    assert "premium" in response.json()
    assert response.json()["premium"] == 400.0 # 500 * 0.8

def test_calculate_premium_max_multiplier(client):
    response = client.post(
        "/api/v1/insurance/premium",
        json={"ncb_years": 4, "vehicle_make": "Ferrari", "vehicle_model": "488", "vehicle_year": 2022, "engine_size_cc": 3902},
    )
    assert response.status_code == 200
    assert "premium" in response.json()
    assert response.json()["premium"] == 400.0 # 250 * 1.6

def test_calculate_premium_invalid_ncb(client):
    response = client.post(
        "/api/v1/insurance/premium",
        json={"ncb_years": -1, "vehicle_make": "Toyota", "vehicle_model": "Camry", "vehicle_year": 2020, "engine_size_cc": 2500},
    )
    assert response.status_code == 422

# Unit Tests for PremiumCalculatorService

@pytest.fixture
def calculator_service():
    return PremiumCalculatorService()

def test_calculate_1_year_ncb(calculator_service):
    request = PremiumCalculationRequest(ncb_years=1, vehicle_make="Honda", vehicle_model="Civic", vehicle_year=2021, engine_size_cc=1500)
    premium = calculator_service.calculate(request)
    assert premium == 400.0 # 500 * 0.8 * 1.0

def test_calculate_2_years_ncb(calculator_service):
    request = PremiumCalculationRequest(ncb_years=2, vehicle_make="Ford", vehicle_model="Focus", vehicle_year=2019, engine_size_cc=1000)
    premium = calculator_service.calculate(request)
    assert premium == 350.0 # 500 * 0.7 * 1.0

def test_calculate_3_years_ncb(calculator_service):
    request = PremiumCalculationRequest(ncb_years=3, vehicle_make="BMW", vehicle_model="X5", vehicle_year=2023, engine_size_cc=3000)
    premium = calculator_service.calculate(request)
    assert premium == 300.0 # 500 * 0.6 * 1.0

def test_calculate_default_multiplier(calculator_service):
    request = PremiumCalculationRequest(ncb_years=2, vehicle_make="Audi", vehicle_model="A4", vehicle_year=2021, engine_size_cc=2000)
    premium = calculator_service.calculate(request)
    assert premium == 350.0 # 500 * 0.7 * 1.0

def test_calculate_negative_ncb_raises_error(calculator_service):
    request = PremiumCalculationRequest(ncb_years=-1, vehicle_make="Toyota", vehicle_model="Camry", vehicle_year=2020, engine_size_cc=2500)
    with pytest.raises(ValueError):
        calculator_service.calculate(request)

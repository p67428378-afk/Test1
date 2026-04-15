from fastapi.testclient import TestClient
from app.main import app
from app.services.premium_calculator import calculate_premium

client = TestClient(app)

def test_calculate_premium_no_ncb():
    premium = calculate_premium(base_rate=500, ncb_years=0, vehicle_multiplier=1.0)
    assert premium == 500.0

def test_calculate_premium_1_year_ncb():
    premium = calculate_premium(base_rate=500, ncb_years=1, vehicle_multiplier=1.0)
    assert premium == 400.0

def test_calculate_premium_2_years_ncb():
    premium = calculate_premium(base_rate=500, ncb_years=2, vehicle_multiplier=1.0)
    assert premium == 350.0

def test_calculate_premium_3_years_ncb():
    premium = calculate_premium(base_rate=500, ncb_years=3, vehicle_multiplier=1.0)
    assert premium == 300.0

def test_calculate_premium_4_years_ncb():
    premium = calculate_premium(base_rate=500, ncb_years=4, vehicle_multiplier=1.0)
    assert premium == 250.0

def test_calculate_premium_5_years_ncb():
    premium = calculate_premium(base_rate=500, ncb_years=5, vehicle_multiplier=1.0)
    assert premium == 250.0

def test_calculate_premium_with_vehicle_multiplier():
    premium = calculate_premium(base_rate=500, ncb_years=0, vehicle_multiplier=1.2)
    assert premium == 600.0

def test_calculate_premium_with_ncb_and_multiplier():
    premium = calculate_premium(base_rate=500, ncb_years=2, vehicle_multiplier=1.2)
    assert premium == 420.0

def test_premium_calculation_endpoint():
    response = client.post("/api/v1/premium/calculate", json={"base_rate": 500, "ncb_years": 2, "vehicle_multiplier": 1.2})
    assert response.status_code == 200
    assert response.json() == {"calculated_premium": 420.0}

def test_premium_calculation_endpoint_invalid_input():
    response = client.post("/api/v1/premium/calculate", json={"base_rate": "invalid", "ncb_years": 2, "vehicle_multiplier": 1.2})
    assert response.status_code == 422

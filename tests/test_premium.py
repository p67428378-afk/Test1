
from fastapi.testclient import TestClient


def test_calculate_premium(client: TestClient):
    response = client.post(
        "/api/v1/insurance/premium/calculate",
        json={"vehicle_details": {"value": 50000}, "ncb_tier": 0.2},
    )
    assert response.status_code == 200
    data = response.json()
    assert data["calculated_premium"] == 400.0
    assert data["base_premium"] == 500.0
    assert data["ncb_applied"] == 0.2
    assert data["vehicle_multiplier_applied"] == 1.0

def test_calculate_premium_with_multiplier(client: TestClient):
    response = client.post(
        "/api/v1/insurance/premium/calculate",
        json={"vehicle_details": {"value": 50000, "multiplier": 1.2}, "ncb_tier": 0.2},
    )
    assert response.status_code == 200
    data = response.json()
    assert data["calculated_premium"] == 480.0
    assert data["base_premium"] == 500.0
    assert data["ncb_applied"] == 0.2
    assert data["vehicle_multiplier_applied"] == 1.2

def test_calculate_premium_ncb_cap(client: TestClient):
    response = client.post(
        "/api/v1/insurance/premium/calculate",
        json={"vehicle_details": {"value": 50000}, "ncb_tier": 0.6},
    )
    assert response.status_code == 200
    data = response.json()
    assert data["calculated_premium"] == 250.0
    assert data["base_premium"] == 500.0
    assert data["ncb_applied"] == 0.5
    assert data["vehicle_multiplier_applied"] == 1.0


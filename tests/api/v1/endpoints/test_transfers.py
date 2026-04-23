
from fastapi.testclient import TestClient
from backend.app.main import app

client = TestClient(app)

def test_cancel_transfer_success():
    response = client.post(
        "/api/v1/transfers/cancel",
        json={"transferReferenceId": "TRF-12345", "accountNumber": "1234567890"},
    )
    assert response.status_code == 200
    assert response.json() == {"status": "CANCELLED", "reason": "Transfer instruction successfully revoked."}

def test_cancel_transfer_too_late():
    response = client.post(
        "/api/v1/transfers/cancel",
        json={"transferReferenceId": "TRF-EXECUTED-12345", "accountNumber": "1234567890"},
    )
    assert response.status_code == 200
    assert response.json() == {"status": "TOO LATE", "reason": "Transfer already executed."}

def test_cancel_transfer_payment_system_error():
    response = client.post(
        "/api/v1/transfers/cancel",
        json={"transferReferenceId": "TRF-FAIL-12345", "accountNumber": "1234567890"},
    )
    assert response.status_code == 200
    assert response.json() == {"status": "FAILED", "reason": "Payment system error."}

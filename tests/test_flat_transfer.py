from fastapi.testclient import TestClient
from sqlalchemy.orm import Session
from backend import models, schemas
from backend.routers.auth import get_current_user
from backend.main import app

def test_initiate_flat_transfer_request(client: TestClient, session: Session):
    # Create users and members for buyer and seller
    seller_user = models.User(email="seller@example.com", hashed_password="password", role="user")
    buyer_user = models.User(email="buyer@example.com", hashed_password="password", role="user")
    admin_user = models.User(email="admin@example.com", hashed_password="password", role="admin")
    session.add_all([seller_user, buyer_user, admin_user])
    session.commit()

    seller_member = models.Member(name="Seller Name", email="seller@example.com", address="123 Main St", contact_details="1234567890", aadhaar_pan="123456789012", membership_category="owner", status="active")
    buyer_member = models.Member(name="Buyer Name", email="buyer@example.com", address="456 Main St", contact_details="0987654321", aadhaar_pan="210987654321", membership_category="owner", status="active")
    session.add_all([seller_member, buyer_member])
    session.commit()

    # Create a property
    property_to_transfer = models.Property(flat_number="A-101", tower_unit_code="T1", area=1000.0, current_owner_member_id=seller_member.id, share_certificate_number="SH-001", legal_status="clear", dues_status="paid")
    session.add(property_to_transfer)
    session.commit()

    # Override dependency to get the admin user
    def get_current_admin_user():
        return admin_user

    app.dependency_overrides[get_current_user] = get_current_admin_user

    response = client.post(
        "/flat-transfer/initiate",
        json={
            "flat_id": property_to_transfer.id,
            "transaction_type": "resale",
            "buyer_email": "buyer@example.com",
            "seller_email": "seller@example.com"
        }
    )

    assert response.status_code == 200
    data = response.json()
    assert data["flat_id"] == property_to_transfer.id
    assert data["buyer_id"] == buyer_member.id
    assert data["seller_id"] == seller_member.id
    assert data["request_status"] == "initiated"
    assert "application_number" in data

    # Clean up dependency override
    del app.dependency_overrides[get_current_user]

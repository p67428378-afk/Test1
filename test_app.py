import pytest
from app import create_app
from database import db, User

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.app_context():
        db.create_all()
    with app.test_client() as client:
        yield client
    with app.app_context():
        db.drop_all()

def test_register_user_success(client):
    response = client.post('/register', json={
        'name': 'Test User',
        'email': 'test@example.com',
        'password': 'password123'
    })
    assert response.status_code == 201
    assert 'User registered successfully' in response.json['message']

    with client.application.app_context():
        user = User.query.filter_by(email='test@example.com').first()
        assert user is not None
        assert user.name == 'Test User'

def test_register_user_missing_fields(client):
    response = client.post('/register', json={
        'name': 'Test User',
        'email': 'test@example.com'
    })
    assert response.status_code == 400
    assert 'Name, email, and password are required' in response.json['error']

def test_register_user_duplicate_email(client):
    # Register first user
    client.post('/register', json={
        'name': 'Test User 1',
        'email': 'duplicate@example.com',
        'password': 'password123'
    })

    # Try to register with the same email
    response = client.post('/register', json={
        'name': 'Test User 2',
        'email': 'duplicate@example.com',
        'password': 'password456'
    })
    assert response.status_code == 409
    assert 'Email already registered' in response.json['error']

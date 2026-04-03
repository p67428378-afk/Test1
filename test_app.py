import pytest
from datetime import datetime, UTC
from database import db, User
from app import bcrypt

@pytest.fixture(scope='function')
def create_user(session):
    def _create_user(name, email, password):
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
        user = User(name=name, email=email, password_hash=hashed_password)
        session.add(user)
        session.commit()
        session.refresh(user)
        return user
    return _create_user

def test_register_user_success(client):
    response = client.post('/register', json={
        'name': 'Test User',
        'email': 'test@example.com',
        'password': 'password123'
    })
    assert response.status_code == 201
    assert 'message' in response.json
    assert response.json['message'] == 'User registered successfully'

def test_register_user_email_already_registered(client, create_user):
    create_user('Duplicate User', 'duplicate@example.com', 'password123')
    response = client.post('/register', json={
        'name': 'Another User',
        'email': 'duplicate@example.com',
        'password': 'anotherpassword'
    })
    assert response.status_code == 409
    assert 'error' in response.json
    assert response.json['error'] == 'Email already registered'

def test_register_user_missing_fields(client):
    response = client.post('/register', json={
        'name': 'Test User',
        'email': 'missing@example.com'
        # password is missing
    })
    assert response.status_code == 400
    assert 'error' in response.json
    assert response.json['error'] == 'Name, email, and password are required'

def test_login_user_success(client, create_user):
    create_user('Login User', 'login@example.com', 'loginpassword')
    response = client.post('/login', json={
        'email': 'login@example.com',
        'password': 'loginpassword'
    })
    assert response.status_code == 200
    assert 'message' in response.json
    assert response.json['message'] == 'Login successful'

def test_login_user_invalid_credentials(client, create_user):
    create_user('Invalid User', 'invalid@example.com', 'invalidpassword')
    response = client.post('/login', json={
        'email': 'invalid@example.com',
        'password': 'wrongpassword'
    })
    assert response.status_code == 401
    assert 'error' in response.json
    assert response.json['error'] == 'Invalid email or password'

def test_get_profile_success(client, create_user):
    user = create_user('Profile User', 'profile@example.com', 'profilepassword')
    response = client.get(f'/profile/{user.id}')
    assert response.status_code == 200
    assert 'user_id' in response.json
    assert response.json['user_id'] == user.id
    assert response.json['name'] == 'Profile User'
    assert response.json['email'] == 'profile@example.com'

def test_get_profile_user_not_found(client):
    response = client.get('/profile/9999') # Assuming user ID 9999 does not exist
    assert response.status_code == 404
    assert 'error' in response.json
    assert response.json['error'] == 'User not found'

def test_datetime_utcnow_deprecation_fix(session, create_user):
    user = create_user('Time Test', 'time@example.com', 'dummy_hash')
    assert user.created_at is not None
    assert isinstance(user.created_at, datetime)
    assert user.updated_at is not None
    assert isinstance(user.updated_at, datetime)

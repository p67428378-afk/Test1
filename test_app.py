import pytest
from datetime import datetime, UTC

def test_register_user_success(client):
    response = client.post('/register', json={
        'name': 'Test User',
        'email': 'test@example.com',
        'password': 'password123'
    })
    assert response.status_code == 201
    assert 'message' in response.json
    assert response.json['message'] == 'User registered successfully'

def test_register_user_email_already_registered(client):
    # Register once
    client.post('/register', json={
        'name': 'Test User',
        'email': 'duplicate@example.com',
        'password': 'password123'
    })
    # Try to register again with the same email
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

def test_login_user_success(client):
    client.post('/register', json={
        'name': 'Login User',
        'email': 'login@example.com',
        'password': 'loginpassword'
    })
    response = client.post('/login', json={
        'email': 'login@example.com',
        'password': 'loginpassword'
    })
    assert response.status_code == 200
    assert 'message' in response.json
    assert response.json['message'] == 'Login successful'

def test_login_user_invalid_credentials(client):
    client.post('/register', json={
        'name': 'Invalid User',
        'email': 'invalid@example.com',
        'password': 'invalidpassword'
    })
    response = client.post('/login', json={
        'email': 'invalid@example.com',
        'password': 'wrongpassword'
    })
    assert response.status_code == 401
    assert 'error' in response.json
    assert response.json['error'] == 'Invalid email or password'

def test_get_profile_success(client, session):
    # Manually add a user to the database for profile retrieval
    from database import User
    from app import bcrypt
    
    hashed_password = bcrypt.generate_password_hash('profilepassword').decode('utf-8')
    user = User(name='Profile User', email='profile@example.com', password_hash=hashed_password)
    session.add(user)
    session.commit()
    session.refresh(user) # Refresh to get the ID

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

def test_datetime_utcnow_deprecation_fix(session):
    from database import User
    # Create a dummy user to trigger the default timestamp
    user = User(name='Time Test', email='time@example.com', password_hash='dummy_hash')
    session.add(user)
    session.commit()
    session.refresh(user)

    assert user.created_at is not None
    assert isinstance(user.created_at, datetime)
    assert user.updated_at is not None
    assert isinstance(user.updated_at, datetime)

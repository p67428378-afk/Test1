import pytest
from database import User

def test_register_duplicate_email(client, session):
    # Register first user
    response = client.post('/register', json={
        'name': 'Test User One',
        'email': 'test@example.com',
        'password': 'password123'
    })
    assert response.status_code == 200
    assert b'User registered successfully' in response.data

    # Attempt to register second user with same email but different name
    response = client.post('/register', json={
        'name': 'Test User Two',
        'email': 'test@example.com',
        'password': 'password456'
    })
    assert response.status_code == 409
    assert b'Email already registered' in response.data

    # Verify only one user exists with that email
    users = session.query(User).filter_by(email='test@example.com').all()
    assert len(users) == 1
    assert users[0].name == 'Test User One'

def test_register_success(client, session):
    response = client.post('/register', json={
        'name': 'New User',
        'email': 'new@example.com',
        'password': 'newpassword'
    })
    assert response.status_code == 200
    assert b'User registered successfully' in response.data
    user = session.query(User).filter_by(email='new@example.com').first()
    assert user is not None
    assert user.name == 'New User'

def test_register_missing_fields(client):
    response = client.post('/register', json={
        'name': 'Missing Email',
        'password': 'password123'
    })
    assert response.status_code == 400
    assert b'Name, email, and password are required' in response.data

    response = client.post('/register', json={
        'email': 'missing@example.com',
        'password': 'password123'
    })
    assert response.status_code == 400
    assert b'Name, email, and password are required' in response.data

    response = client.post('/register', json={
        'name': 'Missing Password',
        'email': 'missing_pass@example.com'
    })
    assert response.status_code == 400
    assert b'Name, email, and password are required' in response.data

def test_login_success(client, session):
    # Register a user first
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
    assert b'Login successful' in response.data

def test_login_invalid_credentials(client, session):
    # Register a user first
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
    assert b'Invalid email or password' in response.data

    response = client.post('/login', json={
        'email': 'nonexistent@example.com',
        'password': 'anypassword'
    })
    assert response.status_code == 401
    assert b'Invalid email or password' in response.data

def test_get_profile_success(client, session):
    # Register a user first
    client.post('/register', json={
        'name': 'Profile User',
        'email': 'profile@example.com',
        'password': 'profilepassword'
    })
    user = session.query(User).filter_by(email='profile@example.com').first()

    response = client.get(f'/profile/{user.id}')
    assert response.status_code == 200
    assert b'Profile User' in response.data
    assert b'profile@example.com' in response.data

def test_get_profile_not_found(client):
    response = client.get('/profile/9999') # Assuming 9999 is a non-existent user ID
    assert response.status_code == 404
    assert b'User not found' in response.data

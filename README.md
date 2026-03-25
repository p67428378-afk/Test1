# User Registration and Login API

This project implements a secure User Registration and Login API using Flask, SQLite, and bcrypt for password hashing.

## Features

- User Registration: Create new user accounts with unique email, name, and securely hashed passwords.
- User Login: Authenticate existing users with their email and password.
- User Profile Retrieval: Fetch user details by their unique user ID.

## Technical Stack

- **Framework:** Flask
- **Database:** SQLite
- **Password Hashing:** bcrypt
- **Dependencies:** Flask, Flask-Bcrypt, Flask-SQLAlchemy, python-dotenv

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/p67428378-afk/Test1.git
cd Test1
```

### 2. Create a virtual environment and activate it

```bash
python -m venv venv
# On Windows
.\venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the root directory of the project based on `.env.example`:

```
SECRET_KEY='your_secret_key_here'
DATABASE_URL='sqlite:///site.db'
```

Replace `'your_secret_key_here'` with a strong, random secret key.

### 5. Initialize the database

Run the following Python script to create the database and tables:

```bash
python -c "from app import create_app, db; app = create_app(); with app.app_context(): db.create_all()"
```

### 6. Run the application

```bash
flask run
```

The API will be accessible at `http://127.0.0.1:5000`.

## API Endpoints

### 1. Register a new user

- **URL:** `/register`
- **Method:** `POST`
- **Request Body (JSON):**
  ```json
  {
    "name": "John Doe",
    "email": "john.doe@example.com",
    "password": "SecureP@ssw0rd"
  }
  ```
- **Response (JSON):**
  - Success: `{"message": "User registered successfully"}`
  - Error (email already exists): `{"error": "Email already registered"}`
  - Error (invalid input): `{"error": "Name, email, and password are required"}`

### 2. Login a user

- **URL:** `/login`
- **Method:** `POST`
- **Request Body (JSON):**
  ```json
  {
    "email": "john.doe@example.com",
    "password": "SecureP@ssw0rd"
  }
  ```
- **Response (JSON):**
  - Success: `{"message": "Login successful"}`
  - Error (invalid credentials): `{"error": "Invalid email or password"}`
  - Error (invalid input): `{"error": "Email and password are required"}`

### 3. Fetch user profile

- **URL:** `/profile/<int:user_id>`
- **Method:** `GET`
- **Response (JSON):**
  - Success: `{"user_id": 1, "name": "John Doe", "email": "john.doe@example.com"}`
  - Error (user not found): `{"error": "User not found"}`
  - Error (invalid user ID): `{"error": "Invalid user ID"}`

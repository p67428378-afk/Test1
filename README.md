# User Registration API

This is a simple FastAPI application that provides an API for user registration.

## Application Architecture

- **Tech stack**: FastAPI, SQLAlchemy, SQLite
- **High-level component diagram**:
  ```
  +-----------------+      +-----------------+      +-----------------+
  |   FastAPI App   | <--> |  Users Router   | <--> |  Users Service  |
  +-----------------+      +-----------------+      +-----------------+
                                                     ^
                                                     |
                                                     v
                                                 +-----------------+
                                                 |   Database      |
                                                 +-----------------+
  ```
- **How frontend and backend communicate**: This is a backend-only application. The API is exposed via HTTP.
- **Database schema overview**: The database contains a single table `users` with the following columns:
  - `id`: Integer, Primary Key
  - `email`: String, Unique
  - `hashed_password`: String

## Project Structure

```
.
├── backend
│   ├── __init__.py
│   ├── database.py
│   ├── main.py
│   ├── models.py
│   ├── routers
│   │   ├── __init__.py
│   │   └── users.py
│   ├── schemas.py
│   └── services.py
├── requirements.txt
└── tests
    ├── __init__.py
    ├── conftest.py
    └── test_users.py
```

## Prerequisites

- Python 3.10+
- pip

## Setup Instructions

1.  **Clone the repo**
2.  **Backend setup**:
    - Create a virtual environment: `python -m venv venv`
    - Activate the virtual environment: `source venv/bin/activate`
    - Install requirements: `pip install -r requirements.txt`
    - Start the server: `uvicorn backend.main:app --reload`

## API Documentation

- **Create User**:
  - **Method**: `POST`
  - **Path**: `/users/`
  - **Request Body**:
    ```json
    {
      "email": "user@example.com",
      "password": "string"
    }
    ```
  - **Response**:
    ```json
    {
      "email": "user@example.com",
      "id": 1
    }
    ```

## Running Tests

- Run backend tests: `pytest`

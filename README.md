# Test1

This project is a simple FastAPI application with a user registration feature.

## Application Architecture

- **Tech stack**: FastAPI, SQLAlchemy, SQLite
- **Backend**: The backend is a FastAPI application with a single endpoint for user creation.
- **Database**: The application uses SQLite for the database.

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
    ├── conftest.py
    └── test_users.py
```

## Setup Instructions

1.  **Clone the repo**
2.  **Backend setup**:
    -   Create a virtual environment: `python -m venv venv`
    -   Activate the virtual environment: `source venv/bin/activate`
    -   Install requirements: `pip install -r requirements.txt`
    -   Run the server: `uvicorn backend.main:app --reload`

## Running Tests

-   Run backend tests: `pytest`

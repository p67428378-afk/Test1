# Cab Management System

This project is a cab management system with a secure login functionality.

## Application Architecture

- **Tech Stack**: FastAPI, MongoDB, React
- **Backend**: FastAPI with a dedicated authentication service.
- **Frontend**: React with Vite.
- **Database**: MongoDB for user data.

## Project Structure

```
.
├── backend
│   ├── app
│   │   ├── api
│   │   │   ├── auth.py
│   │   │   └── users.py
│   │   ├── core
│   │   │   ├── config.py
│   │   │   └── security.py
│   │   ├── database.py
│   │   ├── main.py
│   │   ├── models
│   │   │   └── user.py
│   │   ├── schemas
│   │   │   ├── token.py
│   │   │   └── user.py
│   │   └── services
│   │       └── user_service.py
│   └── tests
│       ├── conftest.py
│       └── test_login.py
├── frontend
│   ├── index.html
│   ├── package.json
│   ├── postcss.config.js
│   ├── src
│   │   ├── App.jsx
│   │   ├── index.css
│   │   ├── main.jsx
│   │   ├── pages
│   │   │   └── Login.jsx
│   │   └── services
│   │       └── api.js
│   ├── tailwind.config.js
│   └── vite.config.js
├── .env.example
├── .gitignore
├── pytest.ini
└── requirements.txt
```

## Prerequisites

- Python 3.10+
- Node.js 18+
- npm
- git

## Setup Instructions

### Backend

1.  Create a virtual environment: `python -m venv venv`
2.  Activate the virtual environment: `source venv/bin/activate`
3.  Install the dependencies: `pip install -r requirements.txt`
4.  Create a `.env` file from the `.env.example` and update the values.
5.  Run the application: `uvicorn app.main:app --reload`

### Frontend

1.  Navigate to the `frontend` directory: `cd frontend`
2.  Install the dependencies: `npm install`
3.  Run the application: `npm run dev`

## API Documentation

- `POST /api/auth/login`: Login to the application.
- `GET /api/users/me`: Get the current user details.

## Running Tests

- **Backend**: `pytest`
- **Frontend**: `npm test`

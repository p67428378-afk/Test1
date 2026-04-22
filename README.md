# Vehicle Insurance Premium Calculator

This project is a Vehicle Insurance Premium Calculator that allows users to calculate their insurance premium based on their vehicle type, no claims bonus (NCB), and a vehicle multiplier.

## Application Architecture

The application is built using a full-stack architecture with a React frontend and a FastAPI backend.

- **Frontend**: React (Vite)
- **Backend**: FastAPI (Python)
- **Database**: PostgreSQL

### High-Level Diagram

```
[Frontend (React)] -> [API (FastAPI)] -> [Database (PostgreSQL)]
```

## Project Structure

```
.
├── backend
│   ├── app
│   │   ├── api
│   │   │   └── premium.py
│   │   ├── core
│   │   │   └── database.py
│   │   ├── models
│   │   │   └── policy.py
│   │   ├── schemas
│   │   │   └── policy.py
│   │   └── main.py
│   ├── requirements.txt
│   └── tests
│       ├── conftest.py
│       └── test_premium.py
└── frontend
    ├── index.html
    ├── package.json
    ├── postcss.config.js
    ├── src
    │   ├── App.jsx
    │   ├── index.css
    │   ├── main.jsx
    │   ├── components
    │   │   └── PremiumCalculator.jsx
    │   └── services
    │       └── api.js
    └── tailwind.config.js
```

## Prerequisites

- Python 3.10+
- Node.js 18+
- npm
- git

## Setup Instructions

### Backend

1.  Navigate to the `backend` directory.
2.  Create a virtual environment: `python -m venv venv`
3.  Activate the virtual environment: `source venv/bin/activate`
4.  Install the dependencies: `pip install -r requirements.txt`
5.  Create a `.env` file with the following content:

    ```
    DATABASE_URL=postgresql://user:password@localhost/db
    ```

6.  Run the application: `uvicorn app.main:app --reload`

### Frontend

1.  Navigate to the `frontend` directory.
2.  Install the dependencies: `npm install`
3.  Run the application: `npm run dev`

## API Documentation

### Calculate Premium

- **Endpoint**: `/api/v1/insurance/premium`
- **Method**: `POST`
- **Request Body**:

  ```json
  {
    "vehicle_type": "SUV",
    "no_claims_bonus_percentage": 0.35,
    "vehicle_multiplier": 1.1
  }
  ```

- **Response Body**:

  ```json
  {
    "calculated_premium": 450.00,
    "policy_details": {
      "vehicle_type": "SUV",
      "no_claims_bonus_percentage": 0.35,
      "vehicle_multiplier": 1.1,
      "base_premium": 500.00
    }
  }
  ```

## Running Tests

### Backend

1.  Navigate to the `backend` directory.
2.  Run the tests: `pytest`

# Vehicle Insurance Premium Calculator

This project is a full-stack application that calculates vehicle insurance premiums based on a base rate, a tiered No-Claim Bonus (NCB), and vehicle-specific multipliers.

## Application Architecture

- **Tech Stack**: FastAPI (Python) for the backend, React (Vite) for the frontend, and PostgreSQL for the database.
- **High-level component diagram**:

```
+--------------------+
|   React Frontend   |
+--------------------+
         |
         | (HTTPS - API Calls)
         v
+--------------------+
|  FastAPI Backend   |
+--------------------+
         |
         | (ORM/SQL Queries)
         v
+--------------------+
| PostgreSQL Database|
+--------------------+
```

- **Communication**: The frontend communicates with the backend via a RESTful API. The backend is configured to run on port 8000 and the frontend on port 5173, with a proxy for API requests.
- **Database Schema**: The database contains a single `policies` table to store policy information, including customer details, vehicle details, NCB history, and the calculated premium.

## Project Structure

```
.
├── backend
│   ├── app
│   │   ├── __init__.py
│   │   ├── config.py
│   │   ├── database.py
│   │   ├── main.py
│   │   ├── models.py
│   │   └── schemas.py
│   ├── requirements.txt
│   └── tests
│       ├── __init__.py
│       ├── conftest.py
│       └── test_main.py
└── frontend
    ├── index.html
    ├── package.json
    ├── postcss.config.js
    ├── tailwind.config.js
    ├── vite.config.js
    └── src
        ├── App.jsx
        ├── index.css
        ├── main.jsx
        ├── components
        │   ├── insurance
        │   │   └── CalculatorCard.jsx
        │   └── layout
        │       ├── Footer.jsx
        │       └── Header.jsx
        ├── pages
        │   └── PremiumCalculatorPage.jsx
        └── services
            └── insuranceApi.js
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
3.  Activate the virtual environment: `source venv/bin/activate` (on Unix/macOS) or `venv\Scripts\activate` (on Windows).
4.  Install the dependencies: `pip install -r requirements.txt`
5.  Create a `.env` file with the `DATABASE_URL` (e.g., `DATABASE_URL=postgresql://user:password@localhost/db`).
6.  Start the server: `uvicorn app.main:app --reload`

### Frontend

1.  Navigate to the `frontend` directory.
2.  Install the dependencies: `npm install`
3.  Start the development server: `npm run dev`

## API Documentation

- **Endpoint**: `POST /api/v1/insurance/premium`
- **Request Body**:

```json
{
  "ncb_years": 3,
  "vehicle_risk_factor": 1.2,
  "policy_holder_name": "John Doe",
  "vehicle_type": "Sedan"
}
```

- **Response Body**:

```json
{
  "calculated_premium": 360.00,
  "policy_id": "some-uuid"
}
```

## Running Tests

### Backend

Navigate to the `backend` directory and run:

```
pytest
```

### Frontend

Navigate to the `frontend` directory and run:

```
npm test
```

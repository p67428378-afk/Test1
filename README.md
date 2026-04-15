# Vehicle Insurance Premium Calculator

This project is a vehicle insurance premium calculator with a tiered No Claims Bonus (NCB) and vehicle multipliers.

## Application Architecture

The application follows a microservices architecture with a React frontend and a FastAPI backend.

- **Frontend**: React (Vite)
- **Backend**: FastAPI (Python)
- **Database**: SQLite (for local development), PostgreSQL (for production)

### High-Level Diagram

```
+----------------+      +------------------+      +--------------------------+
|   React App    |----->|   FastAPI App    |----->|         Database         |
| (Frontend)     |      | (Backend)        |      | (SQLite/PostgreSQL)      |
+----------------+      +------------------+      +--------------------------+
```

## Project Structure

```
.
├── backend
│   ├── app
│   │   ├── api
│   │   │   └── v1
│   │   │       └── endpoints
│   │   │           └── premium.py
│   │   ├── db
│   │   │   └── database.py
│   │   ├── models
│   │   │   └── policy.py
│   │   ├── schemas
│   │   │   └── policy.py
│   │   ├── services
│   │   │   └── premium_calculator.py
│   │   └── main.py
│   ├── requirements.txt
│   └── tests
│       ├── conftest.py
│       └── test_premium.py
└── frontend
    ├── public
    ├── src
    │   ├── components
    │   │   ├── Calculator.jsx
    │   │   ├── Header.jsx
    │   │   ├── SideNav.jsx
    │   │   └── Summary.jsx
    │   ├── services
    │   │   └── api.js
    │   ├── App.jsx
    │   ├── index.css
    │   └── main.jsx
    ├── index.html
    ├── package.json
    ├── postcss.config.js
    ├── tailwind.config.js
    └── vite.config.js
```

## Prerequisites

- Python 3.10+
- Node.js 18+
- npm
- git

## Setup Instructions

### Backend

1.  Navigate to the `backend` directory:
    ```bash
    cd backend
    ```
2.  Create a virtual environment:
    ```bash
    python -m venv venv
    ```
3.  Activate the virtual environment:
    -   **Windows**:
        ```bash
        venv\Scripts\activate
        ```
    -   **macOS/Linux**:
        ```bash
        source venv/bin/activate
        ```
4.  Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```
5.  Start the backend server:
    ```bash
    uvicorn app.main:app --reload
    ```

### Frontend

1.  Navigate to the `frontend` directory:
    ```bash
    cd frontend
    ```
2.  Install the required packages:
    ```bash
    npm install
    ```
3.  Start the frontend development server:
    ```bash
    npm run dev
    ```

## API Documentation

### POST /api/v1/premium/calculate

Calculates the insurance premium.

**Request Body:**

```json
{
  "base_rate": 500,
  "ncb_years": 2,
  "vehicle_multiplier": 1.2
}
```

**Response Body:**

```json
{
  "calculated_premium": 420.0
}
```

## Running Tests

### Backend

1.  Navigate to the `backend` directory.
2.  Run the tests:
    ```bash
    pytest
    ```


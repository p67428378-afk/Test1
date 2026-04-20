# Society Management System

This project is a Society Management System that allows society owners to manage flat purchases and membership transfers.

## Application Architecture

- **Tech Stack**: FastAPI, React, PostgreSQL
- **Backend**: FastAPI with routers, services, models, and schemas.
- **Frontend**: React (Vite) with components, pages, and an API service layer.
- **Database**: PostgreSQL for production, SQLite for testing.

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
│   │   ├── auth.py
│   │   └── flat_transfer.py
│   ├── schemas.py
│   └── security.py
├── frontend
│   ├── index.html
│   ├── package.json
│   ├── postcss.config.js
│   ├── src
│   │   ├── App.jsx
│   │   ├── components
│   │   │   ├── AuditActivity.jsx
│   │   │   ├── Header.jsx
│   │   │   ├── MetricCard.jsx
│   │   │   ├── Sidebar.jsx
│   │   │   └── TransferRequestsTable.jsx
│   │   ├── index.css
│   │   ├── main.jsx
│   │   ├── pages
│   │   │   └── Dashboard.jsx
│   │   └── services
│   │       └── api.js
│   └── tailwind.config.js
├── requirements.txt
└── tests
    ├── __init__.py
    ├── conftest.py
    ├── test_auth.py
    └── test_flat_transfer.py
```

## Setup Instructions

### Backend

1.  Create a virtual environment: `python -m venv venv`
2.  Activate the virtual environment: `source venv/bin/activate` (on Unix) or `venv\Scripts\activate` (on Windows)
3.  Install dependencies: `pip install -r requirements.txt`
4.  Run the application: `uvicorn backend.main:app --reload`

### Frontend

1.  Navigate to the `frontend` directory: `cd frontend`
2.  Install dependencies: `npm install`
3.  Run the application: `npm run dev`

## Running Tests

- **Backend**: `pytest`
- **Frontend**: `npm test`

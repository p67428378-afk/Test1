# Retail Banking Application

This project is a retail banking application that allows users to check their balance, apply for loans, and deposit funds.

## Application Architecture

- **Tech Stack**: FastAPI + React + PostgreSQL
- **High-level component diagram**:

```graphviz:dot
digraph G {
    rankdir=LR;
    node [shape=box, style="filled", fillcolor="#e0e0e0"];

    subgraph cluster_client {
        label="Client Layer";
        color=blue;
        "Web Application" [shape=cylinder];
        "Mobile Application" [shape=cylinder];
    }

    subgraph cluster_backend {
        label="Application Layer";
        color=green;
        "API Gateway" [shape=octagon];
        "Authentication Service" [shape=box];
        "Account Service" [shape=box];
        "Loan Service" [shape=box];
        "Deposit Service" [shape=box];
        "Notification Service" [shape=box];
        "Audit & Logging Service" [shape=box];
    }

    subgraph cluster_data {
        label="Data Layer";
        color=red;
        "Relational Database" [shape=database];
        "NoSQL Database" [shape=database];
        "Document Storage" [shape=folder];
    }

    subgraph cluster_external {
        label="External Integrations";
        color=purple;
        "Core Banking System" [shape=component];
        "Credit Check Service" [shape=component];
        "Identity Verification Service" [shape=component];
        "Payment Network" [shape=component];
        "RDC Provider" [shape=component];
    }

    "Web Application" -> "API Gateway" [label="HTTPS/REST"];
    "Mobile Application" -> "API Gateway" [label="HTTPS/REST"];

    "API Gateway" -> "Authentication Service";
    "API Gateway" -> "Account Service";
    "API Gateway" -> "Loan Service";
    "API Gateway" -> "Deposit Service";

    "Authentication Service" -> "Relational Database" [label="User Data"];
    "Account Service" -> "Core Banking System" [label="Balance/Transactions"];
    "Loan Service" -> "Relational Database" [label="Loan Data"];
    "Loan Service" -> "Credit Check Service";
    "Loan Service" -> "Identity Verification Service";
    "Deposit Service" -> "RDC Provider";
    "Deposit Service" -> "Core Banking System" [label="Fund Transfer"];
    "Deposit Service" -> "Payment Network" [label="EFT"];

    "Account Service" -> "Notification Service";
    "Loan Service" -> "Notification Service";
    "Deposit Service" -> "Notification Service";

    "API Gateway" -> "Audit & Logging Service";
    "Authentication Service" -> "Audit & Logging Service";
    "Account Service" -> "Audit & Logging Service";
    "Loan Service" -> "Audit & Logging Service";
    "Deposit Service" -> "Audit & Logging Service";
    "Notification Service" -> "Audit & Logging Service";

    "Audit & Logging Service" -> "NoSQL Database" [label="Logs/Audit Trails"];
    "RDC Provider" -> "Document Storage" [label="Check Images"];
}
```

- **How frontend and backend communicate**: The frontend and backend communicate via a RESTful API. The backend is served at `http://localhost:8000`.
- **Database schema overview**: The database schema consists of users, accounts, loans, and deposits.

## Project Structure

```
.
├── backend
│   ├── app
│   │   ├── api
│   │   │   ├── __init__.py
│   │   │   ├── accounts.py
│   │   │   ├── deposits.py
│   │   │   ├── loans.py
│   │   │   └── users.py
│   │   ├── core
│   │   │   ├── __init__.py
│   │   │   └── security.py
│   │   ├── db
│   │   │   ├── __init__.py
│   │   │   └── database.py
│   │   ├── models
│   │   │   ├── __init__.py
│   │   │   ├── account.py
│   │   │   ├── deposit.py
│   │   │   ├── loan.py
│   │   │   └── user.py
│   │   ├── schemas
│   │   │   ├── __init__.py
│   │   │   ├── account.py
│   │   │   ├── deposit.py
│   │   │   ├── loan.py
│   │   │   └── user.py
│   │   ├── __init__.py
│   │   └── main.py
│   └── tests
│       ├── __init__.py
│       ├── conftest.py
│       ├── test_accounts.py
│       ├── test_deposits.py
│       ├── test_loans.py
│       └── test_users.py
├── frontend
│   ├── index.html
│   ├── package.json
│   ├── postcss.config.js
│   ├── src
│   │   ├── App.jsx
│   │   ├── App.test.jsx
│   │   ├── components
│   │   │   ├── AccountSummary.jsx
│   │   │   ├── Balance.jsx
│   │   │   ├── Deposit.jsx
│   │   │   ├── Header.jsx
│   │   │   ├── LoanCenter.jsx
│   │   │   └── TransactionLedger.jsx
│   │   ├── index.css
│   │   ├── main.jsx
│   │   └── services
│   │       └── api.js
│   ├── tailwind.config.js
│   └── vite.config.js
├── .gitignore
└── requirements.txt
```

## Prerequisites

- Python 3.10+
- Node.js 18+
- npm
- git

## Setup Instructions

### Backend

1.  Clone the repo
2.  Create a virtual environment: `python -m venv venv`
3.  Activate the virtual environment: `source venv/bin/activate`
4.  Install the requirements: `pip install -r requirements.txt`
5.  Run the server: `uvicorn backend.app.main:app --reload`

### Frontend

1.  Navigate to the `frontend` directory: `cd frontend`
2.  Install the dependencies: `npm install`
3.  Run the development server: `npm run dev`

## API Documentation

- `POST /users/`: Create a new user.
- `POST /accounts/?user_id={user_id}`: Create a new account for a user.
- `GET /accounts/{account_id}`: Get account details.
- `POST /loans/?user_id={user_id}`: Create a new loan for a user.
- `GET /loans/{loan_id}`: Get loan details.
- `POST /deposits/?account_id={account_id}`: Create a new deposit for an account.
- `GET /deposits/{deposit_id}`: Get deposit details.

## Running Tests

### Backend

`pytest`

### Frontend

`npm test`

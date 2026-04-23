
# Scheduled Transfer Cancellation Microservice

This project is a full-stack application that provides a microservice to cancel scheduled fund transfers. It is built with a FastAPI backend and a React frontend.

## Architecture

- **Backend**: FastAPI, SQLAlchemy, PostgreSQL
- **Frontend**: React, Vite, Tailwind CSS

### Project Structure

```
.
├── backend
│   ├── app
│   │   ├── api
│   │   │   └── v1
│   │   │       └── endpoints
│   │   │           └── transfers.py
│   │   ├── core
│   │   │   └── config.py
│   │   ├── db
│   │   │   └── database.py
│   │   ├── models
│   │   │   └── transfer.py
│   │   ├── schemas
│   │   │   └── transfer.py
│   │   ├── services
│   │   │   └── cancellation_service.py
│   │   ├── __init__.py
│   │   └── main.py
│   └── requirements.txt
├── frontend
│   ├── public
│   ├── src
│   │   ├── components
│   │   │   └── CancellationForm.jsx
│   │   ├── services
│   │   │   └── api.js
│   │   ├── App.jsx
│   │   ├── index.css
│   │   └── main.jsx
│   ├── index.html
│   ├── package.json
│   ├── postcss.config.js
│   ├── tailwind.config.js
│   └── vite.config.js
└── tests
    ├── api
    │   └── v1
    │       └── endpoints
    │           └── test_transfers.py
    ├── conftest.py
    └── test_main.py
```

## Setup and Installation

### Prerequisites

- Python 3.9+
- Node.js 16+
- npm

### Backend

1.  Navigate to the `backend` directory:
    ```sh
    cd backend
    ```
2.  Create a virtual environment:
    ```sh
    python -m venv venv
    ```
3.  Activate the virtual environment:
    -   **Windows**:
        ```sh
        venv\Scripts\activate
        ```
    -   **macOS/Linux**:
        ```sh
        source venv/bin/activate
        ```
4.  Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```
5.  Run the application:
    ```sh
    uvicorn app.main:app --reload
    ```

### Frontend

1.  Navigate to the `frontend` directory:
    ```sh
    cd frontend
    ```
2.  Install the dependencies:
    ```sh
    npm install
    ```
3.  Run the application:
    ```sh
    npm run dev
    ```

## Running Tests

### Backend

Navigate to the `backend` directory and run:

```sh
pytest
```

## API Endpoints

- **POST** `/api/v1/transfers/cancel`

  Cancels a scheduled transfer.

  **Request Body:**

  ```json
  {
    "transferReferenceId": "string",
    "accountNumber": "string"
  }
  ```

  **Response:**

  ```json
  {
    "status": "string",
    "reason": "string"
  }
  ```

# Personal Loan Application

This project implements a digital personal loan application system, allowing users to apply for loans without physical paperwork or bank visits. It consists of a React frontend and a FastAPI backend with a PostgreSQL database.

## Table of Contents

- [Features](#features)
- [Architecture](#architecture)
- [Prerequisites](#prerequisites)
- [Setup Instructions](#setup-instructions)
  - [Backend Setup](#backend-setup)
  - [Frontend Setup](#frontend-setup)
- [Running the Application](#running-the-application)
- [API Endpoints](#api-endpoints)
- [Database Schema](#database-schema)
- [Security Considerations](#security-considerations)

## Features

- Digital capture of personal, employment, bank, loan, and legal information.
- Client-side and server-side validation for all input fields.
- Secure transmission and storage of sensitive data (SSN, bank account numbers).
- Responsive web interface.
- RESTful API for application submission.

## Architecture

The application follows a layered architecture:

- **Frontend:** Built with React, providing a responsive user interface.
- **Backend:** Developed using FastAPI (Python), exposing RESTful API endpoints.
- **Database:** PostgreSQL for persistent storage of application data.
- **Containerization:** Docker for packaging both frontend and backend applications.

## Prerequisites

Before you begin, ensure you have the following installed:

- Docker and Docker Compose (recommended for local development)
- Node.js and npm (for frontend development, if not using Docker)
- Python 3.9+ and pip (for backend development, if not using Docker)

## Setup Instructions

### Clone the Repository

```bash
git clone https://github.com/p67428378-afk/Test1.git
cd Test1
```

### Backend Setup

1.  **Navigate to the backend directory:**
    ```bash
    cd backend
    ```

2.  **Create a `.env` file:**
    Copy the `.env.example` file to `.env` and update the values. **Ensure you generate a strong, 32-byte URL-safe base64 encoded key for `SECRET_KEY` in a production environment.** For local development, you can use `openssl rand -base64 32` to generate one.
    ```bash
    cp .env.example .env
    ```
    Example `.env` content:
    ```
    DATABASE_URL="postgresql://user:password@db:5432/loan_app_db"
    SECRET_KEY="your_32_byte_secret_key_for_encryption_here"
    ```

3.  **Database Setup (using Docker Compose):**
    A `docker-compose.yml` file (not provided in this commit, but assumed for full setup) would typically define the PostgreSQL service. For a quick local setup without Docker Compose, you would need a running PostgreSQL instance.

    To create the database tables, you can run the FastAPI application once. The `models.Base.metadata.create_all(bind=engine)` line in `main.py` will create the tables if they don't exist.

### Frontend Setup

1.  **Navigate to the frontend directory:**
    ```bash
    cd ../frontend
    ```

2.  **Create a `.env` file:**
    Copy the `.env.example` file to `.env` and update the `REACT_APP_API_URL` if your backend is running on a different host or port.
    ```bash
    cp .env.example .env
    ```
    Example `.env` content:
    ```
    REACT_APP_API_URL=http://localhost:8000
    ```

3.  **Install dependencies:**
    ```bash
    npm install
    ```

## Running the Application

### Using Docker Compose (Recommended)

(Assuming a `docker-compose.yml` file exists at the root of the project, defining both frontend and backend services, and a PostgreSQL database.)

1.  **From the project root directory, build and run the services:**
    ```bash
    docker-compose up --build
    ```

    The frontend will be accessible at `http://localhost:3000` (or as configured in docker-compose) and the backend API at `http://localhost:8000`.

### Running Backend Separately

1.  **Ensure PostgreSQL is running and accessible.**
2.  **From the `backend` directory:**
    ```bash
    uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
    ```
    The API will be available at `http://localhost:8000`.

### Running Frontend Separately

1.  **From the `frontend` directory:**
    ```bash
    npm start
    ```
    The React app will be available at `http://localhost:3000`.

## API Endpoints

-   **POST `/applications/`**
    -   **Description:** Submits a new loan application.
    -   **Request Body:** `LoanApplicationForm` schema (JSON).
    -   **Response:** `LoanApplicationResponse` schema (JSON) on success.

## Database Schema

The database consists of the following tables:

-   `applicants`
    -   `applicant_id` (PK)
    -   `first_name`
    -   `last_name`
    -   `date_of_birth`
    -   `ssn` (Encrypted)
    -   `email`
    -   `phone_number`
    -   `address`
-   `employment`
    -   `employment_id` (PK)
    -   `applicant_id` (FK)
    -   `company_name`
    -   `company_address`
    -   `job_title`
    -   `income`
-   `bank_accounts`
    -   `bank_account_id` (PK)
    -   `applicant_id` (FK)
    -   `account_number` (Encrypted)
    -   `aba_routing_number` (Encrypted)
-   `loan_applications`
    -   `application_id` (PK)
    -   `applicant_id` (FK)
    -   `loan_purpose`
    -   `loan_amount`
    -   `loan_period_months`
    -   `submission_date`
    -   `status`
-   `legal_declarations`
    -   `legal_id` (PK)
    -   `applicant_id` (FK)
    -   `citizenship_status`
    -   `has_pending_cases`
    -   `declaration_date`

## Security Considerations

-   **Data Encryption:** Sensitive fields like SSN, bank account number, and ABA routing number are encrypted at rest in the database using `cryptography.fernet`.
-   **HTTPS:** All communication between frontend and backend should be over HTTPS in production.
-   **Input Validation:** Both client-side and server-side validation are implemented to prevent common vulnerabilities.
-   **Environment Variables:** Sensitive configurations are managed via environment variables.
-   **CORS:** Configured to allow requests from the frontend origin.

**Note:** For a production environment, a more robust key management system (KMS) should be used for the encryption key, and proper authentication/authorization mechanisms should be implemented for API access.

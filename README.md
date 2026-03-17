# Online Loan Application Platform

This project implements an online loan application platform with a React frontend and a Flask backend, as described in Jira issue [SCRUM-59](https://bfsi-na-ai-engineering.atlassian.net/browse/SCRUM-59) and its associated High-Level Design (HLD) document.

## Table of Contents

- [Project Overview](#project-overview)
- [Architecture](#architecture)
- [Features](#features)
- [Setup Instructions](#setup-instructions)
- [Running the Application](#running-the-application)
- [API Endpoints](#api-endpoints)
- [Database Schema](#database-schema)
- [Security Considerations](#security-considerations)

## Project Overview

The Online Loan Application Platform allows users to submit personal loan applications digitally, eliminating the need for physical bank visits. It features a user-friendly frontend for applicants and a dedicated portal for loan officers to review and manage applications.

## Architecture

The system follows a microservices architectural style, consisting of:

- **Frontend (Applicant Portal):** A React application for loan applicants to input their details.
- **Frontend (Loan Officer Portal):** A React application for loan officers to review and manage applications.
- **Backend Services:** A Flask API that handles application submission, data validation, loan management, user management, and loan officer actions.
- **Database:** PostgreSQL for secure storage of all application data.

## Features

### Applicant Features
- Input personal information (name, contact, DOB, address).
- Input financial information (income, employment, liabilities).
- Input bank details (bank name, account number, IFSC/SWIFT code).
- Specify desired loan amount and tenure.
- Agree to legal terms and conditions.
- Submit loan application.

### Loan Officer Features
- Review submitted loan applications.
- Approve or reject applications.

## Setup Instructions

### Prerequisites
- Docker and Docker Compose
- Node.js (for frontend development, if not using Docker)
- Python 3.9+ (for backend development, if not using Docker)

### Local Development Setup

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/p67428378-afk/Test1.git
    cd Test1
    ```

2.  **Build and run with Docker Compose:**
    ```bash
    docker-compose up --build
    ```
    This will:
    - Build the frontend and backend Docker images.
    - Start the PostgreSQL database.
    - Start the backend Flask application.
    - Start the frontend React application.

3.  **Access the application:**
    - Frontend (Applicant Portal): `http://localhost:3000`
    - Backend API: `http://localhost:5000`

### Manual Setup (without Docker)

#### Backend

1.  **Navigate to the backend directory:**
    ```bash
    cd backend
    ```
2.  **Create a virtual environment and activate it:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: `venv\Scripts\activate`
    ```
3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
4.  **Set up environment variables:**
    Create a `.env` file in the `backend/` directory with your database configuration:
    ```
    DATABASE_URL=postgresql://user:password@localhost:5432/loan_app_db
    SECRET_KEY=your_secret_key_for_flask_sessions
    ```
5.  **Run database migrations (if any):**
    *(To be implemented later with Alembic or similar)*

6.  **Run the Flask application:**
    ```bash
    flask run
    ```

#### Frontend

1.  **Navigate to the frontend directory:**
    ```bash
    cd frontend
    ```
2.  **Install dependencies:**
    ```bash
    npm install
    ```
3.  **Set up environment variables:**
    Create a `.env` file in the `frontend/` directory:
    ```
    REACT_APP_API_BASE_URL=http://localhost:5000
    ```
4.  **Run the React application:**
    ```bash
    npm start
    ```

## Running the Application

Once both frontend and backend services are running (either via Docker Compose or manually):

- Open your browser to `http://localhost:3000` to access the Loan Applicant Portal.
- (Future) Access the Loan Officer Portal at a designated route (e.g., `http://localhost:3000/officer`).

## API Endpoints

*(To be documented as they are implemented)*

## Database Schema

*(To be documented as models are defined)*

## Security Considerations

- All sensitive data is encrypted at rest and in transit.
- Authentication and authorization mechanisms are in place for both applicants and loan officers.
- Input validation is performed to prevent common web vulnerabilities.

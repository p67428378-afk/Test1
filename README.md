# Online Loan Application Platform

This project implements an online platform for personal loan applications, as described in Jira issue [SCRUM-60](https://bfsi-na-ai-engineering.atlassian.net/browse/SCRUM-60) and its associated High-Level Design (HLD) document.

## Architecture

The system follows a microservices architecture with separate frontend applications for loan applicants and loan officers, and a backend API. PostgreSQL is used as the primary database.

## Components

*   **Frontend (Applicant):** A React-based web application for loan applicants to submit their personal, financial, bank, loan, and legal information.
*   **Frontend (Loan Officer):** A React-based web application for loan officers to review and manage loan applications.
*   **Backend:** A Python (Flask/FastAPI) application providing RESTful APIs for application submission, data validation, loan management, and loan officer actions.
*   **Database:** PostgreSQL for secure storage of all application data.

## Setup and Installation

### Prerequisites

*   Docker and Docker Compose (recommended for local development)
*   Node.js (for frontend development)
*   Python 3.9+ (for backend development)

### Local Development with Docker Compose (Recommended)

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/p67428378-afk/Test1.git
    cd Test1
    git checkout ISSUE-SCRUM-60
    ```

2.  **Configure Environment Variables:**

    Create `.env` files based on the provided `.env.example` files in `backend/` and `frontend/` directories.

    **`backend/.env`:**
    ```
    DATABASE_URL=postgresql://user:password@db:5432/loan_app_db
    SECRET_KEY=your_secret_key
    ```

    **`frontend/.env`:**
    ```
    REACT_APP_API_BASE_URL=http://localhost:5000/api
    ```

3.  **Build and Run with Docker Compose:**

    ```bash
    docker-compose up --build
    ```

    This will:
    *   Build Docker images for the backend and frontend.
    *   Start a PostgreSQL database container.
    *   Run the backend API server.
    *   Run the frontend development server.

4.  **Access the Applications:**

    *   **Applicant Frontend:** `http://localhost:3000`
    *   **Loan Officer Frontend:** `http://localhost:3001` (or similar, depending on configuration)
    *   **Backend API:** `http://localhost:5000/api`

### Manual Setup (Without Docker Compose)

#### Backend Setup

1.  **Navigate to the backend directory:**

    ```bash
    cd backend
    ```

2.  **Create and activate a virtual environment:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: `venv\Scripts\activate`
    ```

3.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Set up PostgreSQL database:**

    Ensure you have a PostgreSQL server running and create a database (e.g., `loan_app_db`). Update `backend/.env` with your database connection string.

5.  **Run database migrations (if applicable):**

    ```bash
    # Example using Flask-Migrate or Alembic
    flask db upgrade
    ```

6.  **Run the backend server:**

    ```bash
    flask run
    ```

#### Frontend Setup

1.  **Navigate to the frontend directory:**

    ```bash
    cd frontend
    ```

2.  **Install dependencies:**

    ```bash
    npm install
    ```

3.  **Run the frontend development server:**

    ```bash
    npm start
    ```

## API Endpoints (Backend)

(To be detailed as API is implemented)

## Database Schema

(To be detailed as models are implemented)

## Contributing

(Standard contribution guidelines)

## License

(Standard license information)

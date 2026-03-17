# Online Loan Application Platform

This project implements a basic online loan application platform, allowing users to submit loan applications and loan officers to review and manage them.

## Architecture

The system follows a microservices architecture with a React frontend and a Flask (Python) backend. PostgreSQL is used as the database.

## Features

### Applicant Module
- Submit personal information (name, contact, DOB, address)
- Submit financial information (income, employment, liabilities)
- Submit bank details (bank name, account number, IFSC/SWIFT)
- Specify desired loan amount and tenure
- Agree to terms and conditions
- Submit the complete application

### Loan Officer Module
- View submitted loan applications
- Manually approve or reject applications

## Technologies

**Frontend:**
- React
- HTML/CSS/JavaScript

**Backend:**
- Python 3.9+
- Flask
- SQLAlchemy (ORM for database interaction)
- Psycopg2 (PostgreSQL adapter)

**Database:**
- PostgreSQL

**Deployment (HLD Recommendation):**
- AWS (EC2, RDS, VPC, ELB, S3, IAM, WAF, CloudWatch, X-Ray)
- Docker for containerization
- Kubernetes (Amazon EKS) for orchestration

## Setup and Installation

### Prerequisites

- Git
- Node.js and npm (for frontend)
- Python 3.9+ and pip (for backend)
- PostgreSQL database instance

### Backend Setup

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/p67428378-afk/Test1.git
    cd Test1
    ```

2.  **Navigate to the backend directory:**
    ```bash
    cd backend
    ```

3.  **Create a virtual environment and activate it:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: `venv\Scripts\activate`
    ```

4.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

5.  **Configure environment variables:**
    Create a `.env` file in the `backend/` directory based on `.env.example`:
    ```
    # .env
    DATABASE_URL="postgresql://user:password@host:port/database_name"
    ```
    Replace `user`, `password`, `host`, `port`, and `database_name` with your PostgreSQL database credentials.

6.  **Initialize the database:**
    (This step assumes you have a PostgreSQL database running and accessible with the provided credentials. The `database.py` script will create the necessary tables.)
    ```bash
    python database.py
    ```

7.  **Run the Flask application:**
    ```bash
    flask run
    ```
    The backend server will typically run on `http://127.0.0.1:5000`.

### Frontend Setup

1.  **Navigate to the frontend directory:**
    ```bash
    cd frontend
    ```

2.  **Install dependencies:**
    ```bash
    npm install
    ```

3.  **Configure environment variables:**
    Create a `.env` file in the `frontend/` directory based on `.env.example`:
    ```
    # .env
    REACT_APP_API_URL="http://127.0.0.1:5000"
    ```
    Ensure `REACT_APP_API_URL` points to your running backend server.

4.  **Run the React application:**
    ```bash
    npm start
    ```
    The frontend application will typically open in your browser at `http://localhost:3000`.

## Usage

1.  Open your browser to the frontend application (e.g., `http://localhost:3000`).
2.  Fill out the loan application form with personal, financial, bank, loan, and legal details.
3.  Submit the application.
4.  (For Loan Officers) Access the Loan Officer Portal (e.g., `http://localhost:3000/officer-dashboard`) to view and manage submitted applications.

## API Endpoints (Backend)

-   `POST /applications`: Submit a new loan application.
-   `GET /applications`: Retrieve all loan applications (for loan officers).
-   `GET /applications/<id>`: Retrieve a specific loan application.
-   `PUT /applications/<id>/status`: Update the status of a loan application (approve/reject).

## Project Structure

```
.
├── README.md
├── backend/
│   ├── .env.example
│   ├── app.py
│   ├── database.py
│   └── requirements.txt
├── frontend/
│   ├── .env.example
│   ├── package.json
│   ├── public/
│   │   └── index.html
│   └── src/
│       ├── App.js
│       ├── index.js
│       ├── components/
│       │   ├── LoanApplicationForm.js
│       │   └── LoanOfficerDashboard.js
└── .gitignore
```

import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from dotenv import load_dotenv

from database import Base, engine, SessionLocal, Applicant, LoanApplication, LoanOfficer, ApplicationReview, ApplicationStatus

load_dotenv()

app = Flask(__name__)
CORS(app) # Enable CORS for all routes

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Helper function to convert SQLAlchemy objects to dicts
def serialize_applicant(applicant):
    return {
        "id": applicant.id,
        "first_name": applicant.first_name,
        "last_name": applicant.last_name,
        "email": applicant.email,
        "phone_number": applicant.phone_number,
        "date_of_birth": applicant.date_of_birth.isoformat() if applicant.date_of_birth else None,
        "address": applicant.address,
    }

def serialize_loan_application(app_obj):
    return {
        "id": app_obj.id,
        "applicant_id": app_obj.applicant_id,
        "loan_amount": app_obj.loan_amount,
        "loan_tenure": app_obj.loan_tenure,
        "application_date": app_obj.application_date.isoformat(),
        "status": app_obj.status.value,
        "financial_details": app_obj.financial_details,
        "bank_details": app_obj.bank_details,
        "legal_consent": app_obj.legal_consent,
        "legal_consent_timestamp": app_obj.legal_consent_timestamp.isoformat() if app_obj.legal_consent_timestamp else None,
        "applicant": serialize_applicant(app_obj.applicant) if app_obj.applicant else None,
    }

def serialize_loan_officer(officer):
    return {
        "id": officer.id,
        "first_name": officer.first_name,
        "last_name": officer.last_name,
        "email": officer.email,
        "role": officer.role,
    }

def serialize_application_review(review):
    return {
        "id": review.id,
        "application_id": review.application_id,
        "officer_id": review.officer_id,
        "review_date": review.review_date.isoformat(),
        "decision": review.decision.value,
        "comments": review.comments,
    }

@app.route("/", methods=["GET"])
def health_check():
    return jsonify({"status": "ok", "message": "Loan Application Backend is running!"}), 200

# Endpoint for submitting a new loan application
@app.route("/applications", methods=["POST"])
def submit_application():
    db = next(get_db())
    data = request.get_json()

    # Basic validation
    required_fields = ["first_name", "last_name", "email", "loan_amount", "loan_tenure", "legal_consent"]
    if not all(field in data for field in required_fields):
        return jsonify({"error": "Missing required fields"}), 400

    # Check if applicant already exists or create new
    applicant = db.query(Applicant).filter_by(email=data["email"]).first()
    if not applicant:
        applicant = Applicant(
            first_name=data["first_name"],
            last_name=data["last_name"],
            email=data["email"],
            phone_number=data.get("phone_number"),
            date_of_birth=datetime.fromisoformat(data["date_of_birth"]) if data.get("date_of_birth") else None,
            address=data.get("address"),
        )
        db.add(applicant)
        db.commit()
        db.refresh(applicant)

    new_application = LoanApplication(
        applicant_id=applicant.id,
        loan_amount=data["loan_amount"],
        loan_tenure=data["loan_tenure"],
        financial_details=data.get("financial_details"),
        bank_details=data.get("bank_details"),
        legal_consent=data["legal_consent"],
        legal_consent_timestamp=datetime.utcnow() if data["legal_consent"] else None,
        status=ApplicationStatus.PENDING
    )
    db.add(new_application)
    db.commit()
    db.refresh(new_application)

    return jsonify({"message": "Application submitted successfully", "application_id": new_application.id}), 201

# Endpoint for retrieving all loan applications (for loan officers)
@app.route("/applications", methods=["GET"])
def get_applications():
    db = next(get_db())
    applications = db.query(LoanApplication).all()
    return jsonify([serialize_loan_application(app_obj) for app_obj in applications]), 200

# Endpoint for retrieving a specific loan application
@app.route("/applications/<int:application_id>", methods=["GET"])
def get_application(application_id):
    db = next(get_db())
    application = db.query(LoanApplication).filter_by(id=application_id).first()
    if not application:
        return jsonify({"error": "Application not found"}), 404
    return jsonify(serialize_loan_application(application)), 200

# Endpoint for updating the status of a loan application (for loan officers)
@app.route("/applications/<int:application_id>/status", methods=["PUT"])
def update_application_status(application_id):
    db = next(get_db())
    data = request.get_json()
    officer_id = data.get("officer_id") # In a real app, this would come from authentication
    decision_str = data.get("decision")
    comments = data.get("comments")

    if not officer_id or not decision_str:
        return jsonify({"error": "Missing officer_id or decision"}), 400

    try:
        decision = ApplicationStatus[decision_str.upper()]
    except KeyError:
        return jsonify({"error": "Invalid decision status"}), 400

    application = db.query(LoanApplication).filter_by(id=application_id).first()
    if not application:
        return jsonify({"error": "Application not found"}), 404

    officer = db.query(LoanOfficer).filter_by(id=officer_id).first()
    if not officer:
        # For demonstration, create a dummy officer if not found
        officer = LoanOfficer(first_name="Dummy", last_name="Officer", email=f"dummy.officer{officer_id}@example.com")
        db.add(officer)
        db.commit()
        db.refresh(officer)
        # return jsonify({"error": "Loan Officer not found"}), 404

    application.status = decision
    db.add(application)

    review = ApplicationReview(
        application_id=application.id,
        officer_id=officer.id,
        decision=decision,
        comments=comments,
        review_date=datetime.utcnow()
    )
    db.add(review)
    db.commit()
    db.refresh(application)
    db.refresh(review)

    return jsonify({"message": f"Application {application_id} {decision.value}", "review_id": review.id}), 200

if __name__ == "__main__":
    # Initialize database tables if they don't exist
    engine = engine # Accessing engine from database.py to ensure init_db is called
    # Add a dummy loan officer if not exists for testing purposes
    db = next(get_db())
    if not db.query(LoanOfficer).filter_by(email="loan.officer@example.com").first():
        officer = LoanOfficer(first_name="Loan", last_name="Officer", email="loan.officer@example.com")
        db.add(officer)
        db.commit()
        db.refresh(officer)
        print("Dummy loan officer added.")
    db.close()

    app.run(debug=True)

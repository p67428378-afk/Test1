from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Applicant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(100), nullable=False)
    contact_info = db.Column(db.String(100), nullable=False)
    date_of_birth = db.Column(db.Date, nullable=False)
    address = db.Column(db.String(200), nullable=False)
    applications = db.relationship('LoanApplication', backref='applicant', lazy=True)

class LoanApplication(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    applicant_id = db.Column(db.Integer, db.ForeignKey('applicant.id'), nullable=False)
    status = db.Column(db.String(50), default='Pending Review') # e.g., Pending Review, Approved, Rejected
    submission_date = db.Column(db.DateTime, default=datetime.utcnow)
    loan_amount = db.Column(db.Float, nullable=False)
    tenure_months = db.Column(db.Integer, nullable=False)
    financial_details = db.relationship('FinancialDetails', backref='loan_application', uselist=False, lazy=True)
    bank_details = db.relationship('BankDetails', backref='loan_application', uselist=False, lazy=True)
    legal_agreements = db.relationship('LegalAgreements', backref='loan_application', uselist=False, lazy=True)
    review_history = db.relationship('ReviewHistory', backref='loan_application', lazy=True)

class FinancialDetails(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    loan_application_id = db.Column(db.Integer, db.ForeignKey('loan_application.id'), nullable=False, unique=True)
    income = db.Column(db.Float, nullable=False)
    employment_status = db.Column(db.String(100), nullable=False)
    existing_liabilities = db.Column(db.Float, nullable=True)

class BankDetails(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    loan_application_id = db.Column(db.Integer, db.ForeignKey('loan_application.id'), nullable=False, unique=True)
    bank_name = db.Column(db.String(100), nullable=False)
    account_number = db.Column(db.String(100), nullable=False)
    ifsc_swift_code = db.Column(db.String(100), nullable=False)

class LegalAgreements(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    loan_application_id = db.Column(db.Integer, db.ForeignKey('loan_application.id'), nullable=False, unique=True)
    terms_agreed = db.Column(db.Boolean, default=False, nullable=False)
    credit_check_consent = db.Column(db.Boolean, default=False, nullable=False)

class LoanOfficer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    # In a real app, this would be hashed
    password = db.Column(db.String(200), nullable=False)
    reviews = db.relationship('ReviewHistory', backref='loan_officer', lazy=True)

class ReviewHistory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    loan_application_id = db.Column(db.Integer, db.ForeignKey('loan_application.id'), nullable=False)
    loan_officer_id = db.Column(db.Integer, db.ForeignKey('loan_officer.id'), nullable=False)
    decision = db.Column(db.String(50), nullable=False) # e.g., Approved, Rejected
    comments = db.Column(db.Text, nullable=True)
    review_date = db.Column(db.DateTime, default=datetime.utcnow)

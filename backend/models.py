from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Applicant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone_number = db.Column(db.String(20), nullable=False)
    date_of_birth = db.Column(db.Date, nullable=False)
    address = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    loan_applications = db.relationship('LoanApplication', backref='applicant', lazy=True)

    def __repr__(self):
        return f'<Applicant {self.full_name}>'

class LoanApplication(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    applicant_id = db.Column(db.Integer, db.ForeignKey('applicant.id'), nullable=False)
    status = db.Column(db.String(50), default='Pending Review', nullable=False)
    submission_date = db.Column(db.DateTime, default=datetime.utcnow)
    loan_amount = db.Column(db.Float, nullable=False)
    tenure_months = db.Column(db.Integer, nullable=False)

    financial_details = db.relationship('FinancialDetails', backref='loan_application', uselist=False, lazy=True)
    bank_details = db.relationship('BankDetails', backref='loan_application', uselist=False, lazy=True)
    legal_agreements = db.relationship('LegalAgreements', backref='loan_application', uselist=False, lazy=True)
    review_history = db.relationship('ReviewHistory', backref='loan_application', lazy=True)

    def __repr__(self):
        return f'<LoanApplication {self.id} - {self.status}>'

class FinancialDetails(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    loan_application_id = db.Column(db.Integer, db.ForeignKey('loan_application.id'), nullable=False, unique=True)
    income = db.Column(db.Float, nullable=False)
    employment_status = db.Column(db.String(100), nullable=False)
    existing_liabilities = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<FinancialDetails for Application {self.loan_application_id}>'

class BankDetails(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    loan_application_id = db.Column(db.Integer, db.ForeignKey('loan_application.id'), nullable=False, unique=True)
    bank_name = db.Column(db.String(100), nullable=False)
    account_number = db.Column(db.String(50), nullable=False)
    ifsc_swift_code = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f'<BankDetails for Application {self.loan_application_id}>'

class LegalAgreements(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    loan_application_id = db.Column(db.Integer, db.ForeignKey('loan_application.id'), nullable=False, unique=True)
    agreed_terms = db.Column(db.Boolean, default=False, nullable=False)
    credit_check_consent = db.Column(db.Boolean, default=False, nullable=False)
    agreed_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<LegalAgreements for Application {self.loan_application_id}>'

class LoanOfficer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False) # In a real app, use proper hashing
    full_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    review_actions = db.relationship('ReviewHistory', backref='loan_officer', lazy=True)

    def __repr__(self):
        return f'<LoanOfficer {self.username}>'

class ReviewHistory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    loan_application_id = db.Column(db.Integer, db.ForeignKey('loan_application.id'), nullable=False)
    loan_officer_id = db.Column(db.Integer, db.ForeignKey('loan_officer.id'), nullable=False)
    action = db.Column(db.String(50), nullable=False) # e.g., 'Approved', 'Rejected', 'Requested More Info'
    comments = db.Column(db.Text, nullable=True)
    reviewed_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Review {self.id} for Application {self.loan_application_id} by {self.loan_officer_id}>'

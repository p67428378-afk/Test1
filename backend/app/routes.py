from flask import Blueprint, request, jsonify
from .models import db, Applicant, LoanApplication, FinancialDetails, BankDetails, LegalAgreements, LoanOfficer, ReviewHistory
from datetime import datetime

api_bp = Blueprint('api', __name__)

@api_bp.route('/applications', methods=['POST'])
def submit_application():
    data = request.get_json()

    # Basic validation
    required_fields = [
        'full_name', 'contact_info', 'date_of_birth', 'address',
        'income', 'employment_status', 'loan_amount', 'tenure_months',
        'bank_name', 'account_number', 'ifsc_swift_code',
        'terms_agreed', 'credit_check_consent'
    ]
    for field in required_fields:
        if field not in data:
            return jsonify({'error': f'Missing field: {field}'}), 400

    try:
        # Create Applicant
        applicant = Applicant(
            full_name=data['full_name'],
            contact_info=data['contact_info'],
            date_of_birth=datetime.strptime(data['date_of_birth'], '%Y-%m-%d').date(),
            address=data['address']
        )
        db.session.add(applicant)
        db.session.flush() # To get applicant.id before commit

        # Create LoanApplication
        loan_application = LoanApplication(
            applicant_id=applicant.id,
            loan_amount=data['loan_amount'],
            tenure_months=data['tenure_months']
        )
        db.session.add(loan_application)
        db.session.flush() # To get loan_application.id before commit

        # Create FinancialDetails
        financial_details = FinancialDetails(
            loan_application_id=loan_application.id,
            income=data['income'],
            employment_status=data['employment_status'],
            existing_liabilities=data.get('existing_liabilities')
        )
        db.session.add(financial_details)

        # Create BankDetails
        bank_details = BankDetails(
            loan_application_id=loan_application.id,
            bank_name=data['bank_name'],
            account_number=data['account_number'],
            ifsc_swift_code=data['ifsc_swift_code']
        )
        db.session.add(bank_details)

        # Create LegalAgreements
        legal_agreements = LegalAgreements(
            loan_application_id=loan_application.id,
            terms_agreed=data['terms_agreed'],
            credit_check_consent=data['credit_check_consent']
        )
        db.session.add(legal_agreements)

        db.session.commit()

        return jsonify({'message': 'Loan application submitted successfully', 'application_id': loan_application.id}), 201

    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@api_bp.route('/applications', methods=['GET'])
def get_applications():
    applications = LoanApplication.query.all()
    result = []
    for app in applications:
        applicant = Applicant.query.get(app.applicant_id)
        financial = FinancialDetails.query.filter_by(loan_application_id=app.id).first()
        bank = BankDetails.query.filter_by(loan_application_id=app.id).first()
        legal = LegalAgreements.query.filter_by(loan_application_id=app.id).first()

        result.append({
            'id': app.id,
            'status': app.status,
            'submission_date': app.submission_date.isoformat(),
            'loan_amount': app.loan_amount,
            'tenure_months': app.tenure_months,
            'applicant': {
                'full_name': applicant.full_name,
                'contact_info': applicant.contact_info,
                'date_of_birth': applicant.date_of_birth.isoformat(),
                'address': applicant.address
            },
            'financial_details': {
                'income': financial.income,
                'employment_status': financial.employment_status,
                'existing_liabilities': financial.existing_liabilities
            },
            'bank_details': {
                'bank_name': bank.bank_name,
                'account_number': bank.account_number,
                'ifsc_swift_code': bank.ifsc_swift_code
            },
            'legal_agreements': {
                'terms_agreed': legal.terms_agreed,
                'credit_check_consent': legal.credit_check_consent
            }
        })
    return jsonify(result), 200

@api_bp.route('/applications/<int:application_id>', methods=['GET'])
def get_application_details(application_id):
    app = LoanApplication.query.get_or_404(application_id)
    applicant = Applicant.query.get(app.applicant_id)
    financial = FinancialDetails.query.filter_by(loan_application_id=app.id).first()
    bank = BankDetails.query.filter_by(loan_application_id=app.id).first()
    legal = LegalAgreements.query.filter_by(loan_application_id=app.id).first()
    review_history = ReviewHistory.query.filter_by(loan_application_id=app.id).all()

    review_data = []
    for review in review_history:
        officer = LoanOfficer.query.get(review.loan_officer_id)
        review_data.append({
            'officer_name': officer.full_name if officer else 'N/A',
            'decision': review.decision,
            'comments': review.comments,
            'review_date': review.review_date.isoformat()
        })

    result = {
        'id': app.id,
        'status': app.status,
        'submission_date': app.submission_date.isoformat(),
        'loan_amount': app.loan_amount,
        'tenure_months': app.tenure_months,
        'applicant': {
            'full_name': applicant.full_name,
            'contact_info': applicant.contact_info,
            'date_of_birth': applicant.date_of_birth.isoformat(),
            'address': applicant.address
        },
        'financial_details': {
            'income': financial.income,
            'employment_status': financial.employment_status,
            'existing_liabilities': financial.existing_liabilities
        },
        'bank_details': {
            'bank_name': bank.bank_name,
            'account_number': bank.account_number,
            'ifsc_swift_code': bank.ifsc_swift_code
        },
        'legal_agreements': {
            'terms_agreed': legal.terms_agreed,
            'credit_check_consent': legal.credit_check_consent
        },
        'review_history': review_data
    }
    return jsonify(result), 200

@api_bp.route('/applications/<int:application_id>/status', methods=['PUT'])
def update_application_status(application_id):
    data = request.get_json()
    new_status = data.get('status')
    loan_officer_id = data.get('loan_officer_id') # This would come from authenticated user in real app
    comments = data.get('comments')

    if not new_status or not loan_officer_id:
        return jsonify({'error': 'Status and loan_officer_id are required'}), 400

    loan_application = LoanApplication.query.get_or_404(application_id)
    loan_officer = LoanOfficer.query.get(loan_officer_id)

    if not loan_officer:
        return jsonify({'error': 'Loan Officer not found'}), 404

    try:
        loan_application.status = new_status
        review = ReviewHistory(
            loan_application_id=application_id,
            loan_officer_id=loan_officer_id,
            decision=new_status, # Decision is the new status
            comments=comments
        )
        db.session.add(review)
        db.session.commit()
        return jsonify({'message': f'Application {application_id} status updated to {new_status}'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

# Placeholder for Loan Officer Login/Auth (not fully implemented in this HLD scope)
@api_bp.route('/loan_officers/login', methods=['POST'])
def loan_officer_login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    loan_officer = LoanOfficer.query.filter_by(email=email).first()

    # In a real application, password would be hashed and securely compared
    if loan_officer and loan_officer.password == password:
        return jsonify({'message': 'Login successful', 'loan_officer_id': loan_officer.id}), 200
    else:
        return jsonify({'message': 'Invalid credentials'}), 401

# Placeholder for Loan Officer Registration (for initial setup/testing)
@api_bp.route('/loan_officers/register', methods=['POST'])
def loan_officer_register():
    data = request.get_json()
    full_name = data.get('full_name')
    email = data.get('email')
    password = data.get('password')

    if not all([full_name, email, password]):
        return jsonify({'error': 'Missing full_name, email, or password'}), 400

    if LoanOfficer.query.filter_by(email=email).first():
        return jsonify({'error': 'Loan Officer with this email already exists'}), 409

    try:
        new_officer = LoanOfficer(
            full_name=full_name,
            email=email,
            password=password # In real app, hash this password!
        )
        db.session.add(new_officer)
        db.session.commit()
        return jsonify({'message': 'Loan Officer registered successfully', 'loan_officer_id': new_officer.id}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

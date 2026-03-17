from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from datetime import datetime

from config import Config
from models import db, Applicant, LoanApplication, FinancialDetails, BankDetails, LegalAgreements, LoanOfficer, ReviewHistory

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate = Migrate(app, db)
    CORS(app) # Enable CORS for frontend interaction

    @app.route('/')
    def hello_world():
        return 'Hello, World! This is the Loan Application Backend.'

    @app.route('/api/apply', methods=['POST'])
    def apply_loan():
        data = request.get_json()

        # Basic validation
        required_fields = [
            'full_name', 'email', 'phone_number', 'date_of_birth', 'address',
            'income', 'employment_status', 'existing_liabilities',
            'bank_name', 'account_number', 'ifsc_swift_code',
            'loan_amount', 'tenure_months',
            'agreed_terms', 'credit_check_consent'
        ]
        for field in required_fields:
            if field not in data:
                return jsonify({'error': f'Missing field: {field}'}), 400

        try:
            # Create Applicant (or find existing by email)
            applicant = Applicant.query.filter_by(email=data['email']).first()
            if not applicant:
                applicant = Applicant(
                    full_name=data['full_name'],
                    email=data['email'],
                    phone_number=data['phone_number'],
                    date_of_birth=datetime.strptime(data['date_of_birth'], '%Y-%m-%d').date(),
                    address=data['address']
                )
                db.session.add(applicant)
                db.session.commit()

            # Create LoanApplication
            loan_application = LoanApplication(
                applicant_id=applicant.id,
                loan_amount=data['loan_amount'],
                tenure_months=data['tenure_months']
            )
            db.session.add(loan_application)
            db.session.commit()

            # Create FinancialDetails
            financial_details = FinancialDetails(
                loan_application_id=loan_application.id,
                income=data['income'],
                employment_status=data['employment_status'],
                existing_liabilities=data['existing_liabilities']
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
                agreed_terms=data['agreed_terms'],
                credit_check_consent=data['credit_check_consent']
            )
            db.session.add(legal_agreements)

            db.session.commit()

            return jsonify({'message': 'Loan application submitted successfully', 'application_id': loan_application.id}), 201

        except Exception as e:
            db.session.rollback()
            return jsonify({'error': str(e)}), 500

    # Loan Officer Endpoints (simplified for initial implementation)
    @app.route('/api/applications', methods=['GET'])
    def get_applications():
        applications = LoanApplication.query.all()
        result = []
        for app in applications:
            applicant = Applicant.query.get(app.applicant_id)
            result.append({
                'id': app.id,
                'applicant_name': applicant.full_name if applicant else 'N/A',
                'loan_amount': app.loan_amount,
                'tenure_months': app.tenure_months,
                'status': app.status,
                'submission_date': app.submission_date.isoformat()
            })
        return jsonify(result), 200

    @app.route('/api/applications/<int:app_id>/status', methods=['PUT'])
    def update_application_status(app_id):
        data = request.get_json()
        new_status = data.get('status')
        officer_id = data.get('officer_id') # In a real app, get this from authenticated user
        comments = data.get('comments')

        if not new_status or not officer_id:
            return jsonify({'error': 'Missing status or officer_id'}), 400

        loan_application = LoanApplication.query.get(app_id)
        if not loan_application:
            return jsonify({'error': 'Application not found'}), 404

        loan_application.status = new_status

        review = ReviewHistory(
            loan_application_id=app_id,
            loan_officer_id=officer_id,
            action=new_status,
            comments=comments
        )
        db.session.add(review)
        db.session.commit()

        return jsonify({'message': f'Application {app_id} status updated to {new_status}'}), 200

    return app

if __name__ == '__main__':
    app = create_app()
    with app.app_context():
        db.create_all() # This will create tables based on models.py
    app.run(debug=True, host='0.0.0.0', port=5000)

from sqlalchemy.orm import Session
from models import Applicant, Employment, Financial, LoanApplication
from schemas import LoanApplicationCreate
from datetime import date

def create_loan_application(db: Session, application: LoanApplicationCreate):
    print("--- Inside create_loan_application ---")
    # Create Applicant
    db_applicant = Applicant(
        first_name=application.personal_info.first_name,
        last_name=application.personal_info.last_name,
        date_of_birth=application.personal_info.date_of_birth,
        ssn=application.personal_info.ssn,
        address=application.personal_info.address,
        phone_number=application.personal_info.phone_number,
        email_address=application.personal_info.email_address,
    )
    db.add(db_applicant)
    db.flush() # Flush to get applicant_id
    print(f"Applicant created with ID: {db_applicant.applicant_id}")

    # Create Employment Info
    db_employment = Employment(
        applicant_id=db_applicant.applicant_id,
        employer_name=application.employment_info.employer_name,
        job_title=application.employment_info.job_title,
        annual_income=application.employment_info.annual_income,
        employment_start_date=application.employment_info.employment_start_date,
    )
    db.add(db_employment)

    # Create Financial Info
    db_financial = Financial(
        applicant_id=db_applicant.applicant_id,
        bank_account_number=application.financial_info.bank_account_number,
        routing_number=application.financial_info.routing_number,
        credit_score=application.financial_info.credit_score,
        existing_debts=application.financial_info.existing_debts,
        assets=application.financial_info.assets,
    )
    db.add(db_financial)

    # Create Loan Application
    db_loan_application = LoanApplication(
        applicant_id=db_applicant.applicant_id,
        loan_amount=application.loan_details.loan_amount,
        loan_purpose=application.loan_details.loan_purpose,
        repayment_period_months=application.loan_details.repayment_period_months,
        submission_date=date.today(),
        status="Submitted",
        kyc_status="Pending",
        credit_check_status="Pending",
    )
    db.add(db_loan_application)

    print("--- Before commit ---")
    db.commit()
    db.refresh(db_loan_application)
    print(f"Loan application committed with ID: {db_loan_application.application_id}")
    return db_loan_application

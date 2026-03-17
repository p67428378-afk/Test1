from sqlalchemy.orm import Session
from . import models, schemas
from datetime import date

def create_loan_application(db: Session, application_data: schemas.LoanApplicationForm):
    # Create Applicant
    db_applicant = models.Applicant(
        first_name=application_data.applicant.first_name,
        last_name=application_data.applicant.last_name,
        date_of_birth=application_data.applicant.date_of_birth,
        email=application_data.applicant.email,
        phone_number=application_data.applicant.phone_number,
        address=application_data.applicant.address
    )
    db_applicant.ssn = application_data.applicant.ssn # Encrypted via setter
    db.add(db_applicant)
    db.flush() # Flush to get applicant_id

    # Create Employment
    db_employment = models.Employment(
        applicant_id=db_applicant.applicant_id,
        company_name=application_data.employment.company_name,
        company_address=application_data.employment.company_address,
        job_title=application_data.employment.job_title,
        income=application_data.employment.income
    )
    db.add(db_employment)

    # Create BankAccount
    db_bank_account = models.BankAccount(
        applicant_id=db_applicant.applicant_id
    )
    db_bank_account.account_number = application_data.bank_account.account_number # Encrypted via setter
    db_bank_account.aba_routing_number = application_data.bank_account.aba_routing_number # Encrypted via setter
    db.add(db_bank_account)

    # Create LoanApplication
    db_loan_application = models.LoanApplication(
        applicant_id=db_applicant.applicant_id,
        loan_purpose=application_data.loan_details.loan_purpose,
        loan_amount=application_data.loan_details.loan_amount,
        loan_period_months=application_data.loan_details.loan_period_months,
        submission_date=date.today(),
        status="Submitted"
    )
    db.add(db_loan_application)

    # Create LegalDeclaration
    db_legal_declaration = models.LegalDeclaration(
        applicant_id=db_applicant.applicant_id,
        citizenship_status=application_data.legal_declaration.citizenship_status,
        has_pending_cases=application_data.legal_declaration.has_pending_cases,
        declaration_date=date.today()
    )
    db.add(db_legal_declaration)

    db.commit()
    db.refresh(db_applicant)
    db.refresh(db_employment)
    db.refresh(db_bank_account)
    db.refresh(db_loan_application)
    db.refresh(db_legal_declaration)

    return schemas.LoanApplicationResponse(
        applicant=schemas.Applicant.from_orm(db_applicant),
        employment=schemas.Employment.from_orm(db_employment),
        bank_account=schemas.BankAccount.from_orm(db_bank_account),
        loan_application=schemas.LoanApplication.from_orm(db_loan_application),
        legal_declaration=schemas.LegalDeclaration.from_orm(db_legal_declaration)
    )

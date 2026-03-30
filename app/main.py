
from fastapi import FastAPI, HTTPException, status, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from datetime import datetime
import uuid

from app.schemas import LoanApplicationRequest, UnderwritingDecision, HealthCheckResponse
from app.services import (
    assess_risk,
    perform_ml_inference,
    check_rbi_defaulter_list,
    log_audit_trail,
    make_underwriting_decision
)

app = FastAPI(
    title="Loan Underwriting Microservice",
    description="Real-time microservice for assessing loan applicant creditworthiness.",
    version="1.0.0",
)

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    print(f"Validation error: {exc.errors()} for request: {exc.body}")
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_CONTENT, # Changed from HTTP_422_UNPROCESSABLE_ENTITY
        content={"detail": exc.errors(), "body": exc.body},
    )

@app.get("/health", response_model=HealthCheckResponse, summary="Health Check")
async def health_check():
    """Checks the health of the microservice."""
    return {"status": "healthy"}

@app.post("/underwrite", response_model=UnderwritingDecision, status_code=status.HTTP_200_OK, summary="Underwrite Loan Application")
async def underwrite_loan_application(request: LoanApplicationRequest):
    """Processes a loan application to assess creditworthiness and return a decision."""
    try:
        # 1. Assess Risk based on predefined rules
        risk_assessment = assess_risk(request)

        # 2. Perform ML Inference
        ml_inference_result = perform_ml_inference(request)

        # 3. Check RBI Defaulter List
        rbi_check_result = check_rbi_defaulter_list(request)

        # 4. Make Final Underwriting Decision
        final_status = make_underwriting_decision(
            request, risk_assessment, ml_inference_result, rbi_check_result
        )

        decision_id = str(uuid.uuid4())
        decision_timestamp = datetime.now()

        # 5. Log Comprehensive Audit Trail
        # The audit trail service is mocked for now, but in a real scenario,
        # it would persist all inputs, intermediate results, and the final decision.
        underwriting_decision = UnderwritingDecision(
            decision_id=decision_id,
            applicant_id=request.applicant_id,
            final_status=final_status,
            decision_timestamp=decision_timestamp,
            risk_score=risk_assessment["risk_score"],
            ml_score=ml_inference_result["ml_score"],
            rbi_check_result=rbi_check_result,
            triggered_rules=risk_assessment["triggered_rules"],
            audit_trail_id=""
        )
        audit_trail_id = log_audit_trail(request, underwriting_decision)
        underwriting_decision.audit_trail_id = audit_trail_id

        return underwriting_decision

    except Exception as e:
        # Log the exception for debugging purposes
        print(f"An error occurred during loan underwriting: {e}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal server error")

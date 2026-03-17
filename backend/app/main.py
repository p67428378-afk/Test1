from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from . import models, schemas, crud
from .database import SessionLocal, engine, get_db
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    # Create database tables on startup
    models.Base.metadata.create_all(bind=engine)

# CORS middleware to allow requests from the frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"], # Allow frontend origin
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.post("/applications/", response_model=schemas.LoanApplicationResponse, status_code=status.HTTP_201_CREATED)
def create_loan_application(application: schemas.LoanApplicationForm, db: Session = Depends(get_db)):
    try:
        return crud.create_loan_application(db=db, application_data=application)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

@app.get("/health")
def health_check():
    return {"status": "ok"}

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.core.database import get_db, Base, engine
from backend.models import claim as claim_model
from backend.schemas import claim as claim_schema
from backend.services import claim_service
from backend.routers import claims

app = FastAPI()

# Create database tables
Base.metadata.create_all(bind=engine)

app.include_router(claims.router, prefix="/claims", tags=["claims"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the Insurance Claim Processing API"}

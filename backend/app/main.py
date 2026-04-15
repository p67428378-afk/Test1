from fastapi import FastAPI
from app.db.database import engine
from app.models import policy
from app.api.v1.endpoints import premium

policy.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Vehicle Insurance Premium Calculator",
    description="An API to calculate vehicle insurance premiums with tiered NCB and vehicle multipliers.",
    version="1.0.0"
)

app.include_router(premium.router, prefix="/api/v1", tags=["Premium Calculation"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the Vehicle Insurance Premium Calculator API"}

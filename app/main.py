from fastapi import FastAPI
from app.routers import policy
from app.database import engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(policy.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Health Insurance Portal API"}

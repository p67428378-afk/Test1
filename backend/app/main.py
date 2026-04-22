from fastapi import FastAPI
from app.api import premium

app = FastAPI()

app.include_router(premium.router, prefix="/api/v1/insurance", tags=["insurance"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the Insurance Premium Calculator"}

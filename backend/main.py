from fastapi import FastAPI
from backend.routers import premium_calculator

app = FastAPI()

app.include_router(premium_calculator.router)

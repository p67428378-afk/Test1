
from fastapi import FastAPI
from backend.api.v1.endpoints import premium

app = FastAPI()

app.include_router(premium.router, prefix="/api/v1")

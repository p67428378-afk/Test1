
from fastapi import FastAPI
from .api.v1.endpoints import transfers
from .db.database import engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(transfers.router, prefix="/api/v1", tags=["transfers"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the Scheduled Transfer Cancellation Microservice"}

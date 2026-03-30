from fastapi import FastAPI
from backend.database import engine, Base
from backend.routers import claims

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(claims.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Insurance Claim API"}

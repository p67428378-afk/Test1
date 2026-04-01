
from fastapi import FastAPI
from backend.database import engine, Base
from backend.routers import credit_cards, applications

app = FastAPI()

@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)

app.include_router(credit_cards.router)
app.include_router(applications.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Credit Card Application API"}

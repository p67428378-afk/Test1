from fastapi import FastAPI
from .database import engine
from . import models
from .routers import auth, flat_transfer

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(auth.router)
app.include_router(flat_transfer.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Society Management System"}

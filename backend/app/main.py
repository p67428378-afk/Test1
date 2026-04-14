from fastapi import FastAPI

from .db.database import Base, engine
from .api import users, accounts, loans, deposits

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(accounts.router, prefix="/accounts", tags=["accounts"])
app.include_router(loans.router, prefix="/loans", tags=["loans"])
app.include_router(deposits.router, prefix="/deposits", tags=["deposits"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the Banking API"}

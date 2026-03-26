
from fastapi import FastAPI
from routers import cards, applications

app = FastAPI()

app.include_router(cards.router)
app.include_router(applications.router)

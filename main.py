from fastapi import FastAPI
from database import Base, engine
from routers import loan_applications

def create_app():
    app = FastAPI()

    @app.on_event("startup")
    def on_startup():
        Base.metadata.create_all(bind=engine)

    app.include_router(loan_applications.router)
    print("Router included in FastAPI app (from create_app).")
    return app

app = create_app()

from fastapi import FastAPI

from .routers import heroes, auth
from .database import create_db_and_tables

app = FastAPI(title="Heroes API", description="An API to manage heroes", version="1.0.0"   )

# Create tables on startup
@app.on_event("startup")
def on_startup():
    create_db_and_tables()

app.include_router(auth.router)
app.include_router(heroes.router)

@app.get("/")
def root():
    return {"message":"hello world!"}


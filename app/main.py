from contextlib import asynccontextmanager

from fastapi import FastAPI, Path, HTTPException

from app.config.admin import setup_admin
from app.config.database import init_db
from router.v1.product import crud as product_crud
import app.model.product_model as product_model
from app.config.database import  engine, SessionLocal

app = FastAPI()
product_model.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def root():
    return "Hello from the homepage!"

app.include_router(product_crud.product_router)
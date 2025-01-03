from fastapi import FastAPI

from router.v1.product import crud as product_crud
from app.config.database import SessionLocal

app = FastAPI()

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
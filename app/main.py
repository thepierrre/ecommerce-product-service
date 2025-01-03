from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.config.database import init_db
from router.v1.product import crud as product_crud

@asynccontextmanager
async def on_startup(app: FastAPI):
    init_db()
    yield

app = FastAPI(lifespan=on_startup)

@app.get("/")
def root():
    return "Hello from the homepage!"

app.include_router(product_crud.product_router)
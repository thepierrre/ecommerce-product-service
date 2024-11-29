from fastapi import FastAPI, Path, HTTPException
from router.v1.product import crud as product_crud

app = FastAPI()

@app.get("/")
def root():
    return "Hello from the homepage!"

app.include_router(product_crud.product_router)
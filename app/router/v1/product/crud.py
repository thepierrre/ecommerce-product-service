from fastapi import APIRouter, status
from app.service.product_service import ProductService
from app.model.product_model import ProductCreate
from app.config.database import db_dependency

router = APIRouter()
service = ProductService()

product_router = APIRouter(
  prefix="/v1/products"
)

@product_router.get("/{product_id}")
def fetch_product_by_id(product_id: str, db: db_dependency):
    return service.find_product_by_id(product_id, db)

@product_router.post("", status_code=status.HTTP_201_CREATED)
def create_product(product: ProductCreate, db: db_dependency):
    return service.create_product(product, db)

@product_router.delete("/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_product(product_id: str, db: db_dependency):
    return service.remove_product(product_id, db)

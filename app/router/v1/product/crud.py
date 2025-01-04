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
async def fetch_product_by_id(product_id: str, db: db_dependency):
    return await service.find_product_by_id(product_id, db)

@product_router.post("", status_code=status.HTTP_201_CREATED)
async def create_product(product: ProductCreate, db: db_dependency):
    return await service.create_product(product, db)

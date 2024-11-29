from fastapi import APIRouter
from service.product_service import ProductService

router = APIRouter()
service = ProductService()

product_router = APIRouter(
  prefix="/v1/products"
)

@product_router.get("/{product_id}")
async def get_product_by_id(product_id: str):
    return await service.find_product_by_id(product_id)
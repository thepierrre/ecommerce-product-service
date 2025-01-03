from fastapi import APIRouter, status
from app.service.product_service import ProductService
from app.model.product_model import ProductCreate

router = APIRouter()
service = ProductService()

product_router = APIRouter(
  prefix="/v1/products"
)

@product_router.get("/{product_id}")
async def fetch_product_by_id(product_id: str):
    return await service.find_product_by_id(product_id)

@product_router.post("", status_code=status.HTTP_201_CREATED)
async def create_product(product: ProductCreate):
    return await service.create_product(product)

# generate uuid
# build a url string with the location of the resource using the id
# only return 201 and location header to the client
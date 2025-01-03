from app.model.product_model import Product, ProductCreate
from sqlalchemy.orm import Session

class ProductService:
    async def find_product_by_id(self, id: str):
        return "product"
    
    async def create_product(self, product: ProductCreate, session: Session):
        db_product = Product(**product.model_dump())
        session.add(db_product)
        session.commit()
        session.refresh(db_product)
        return db_product
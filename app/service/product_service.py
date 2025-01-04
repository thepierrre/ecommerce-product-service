from fastapi import HTTPException
from uuid import UUID

from app.model.product_model import Product, ProductCreate
from sqlalchemy.orm import Session

class ProductService:

    @staticmethod
    def find_product_by_id(product_id: str, session: Session):
        uuid = UUID(product_id)
        product = session.get(Product, uuid)
        if not product:
            raise HTTPException(status_code=404, detail=f'Product with the id {product_id} not found.')
        return product

    @staticmethod
    def create_product(product: ProductCreate, session: Session):
        db_product = Product(**product.model_dump())
        session.add(db_product)
        session.commit()
        session.refresh(db_product)
        return db_product

    @staticmethod
    def remove_product(product_id: str, session: Session):
        uuid = UUID(product_id)
        product = session.get(Product, uuid)
        if not product:
            raise HTTPException(status_code=404, detail=f'Product with the id {product_id} not found.')
        session.delete(product)
        session.commit()


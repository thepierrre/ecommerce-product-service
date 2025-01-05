from fastapi import HTTPException
from uuid import UUID

from app.model.product_model import Product, ProductCreate, ProductRead, ProductEdit
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
    def create_product(product: ProductCreate, session: Session) -> Product:
        db_product = Product(**product.model_dump())
        session.add(db_product)
        session.commit()
        session.refresh(db_product)
        return db_product

    @staticmethod
    def update_product(product_id: str, product: ProductEdit, session: Session) -> Product:
        uuid = UUID(product_id)
        product_db = session.get(Product, uuid)
        if product_db is None:
            raise HTTPException(status_code=404, detail=f'Product with the id {product_id} not found.')

        product_data = product.model_dump(exclude_unset=True)
        product_db.sqlmodel_update(product_data)
        session.add(product_db)
        session.commit()
        session.refresh(product_db)
        return product_db

    @staticmethod
    def remove_product(product_id: str, session: Session):
        uuid = UUID(product_id)
        product = session.get(Product, uuid)
        if product is None:
            raise HTTPException(status_code=404, detail=f'Product with the id {product_id} not found.')
        session.delete(product)
        session.commit()


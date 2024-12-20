from __future__ import annotations
from sqlalchemy import Column, String, Float, UUID, DateTime
from app.config.database import Base

class ProductBase(Base):
    name: String
    description: String | None = None
    price: Float
    discount_price: Float | None = None
    currency: String | None = "EUR"
    rating: Float | None = None
    category: String


class ProductCreate(ProductBase):
    pass


class Product(ProductBase):
    __tablename__ = 'products'
    id = Column(UUID, primary_key=True, index=True)
    name = Column(String(100), index=True)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

from __future__ import annotations

from uuid import UUID

from app.config.database import Base
from pydantic import BaseModel
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, DateTime


class ProductBase(Base):
    __abstract__ = True

    name: Mapped[str] = mapped_column(String(100), index=True)
    description: Mapped[str | None] = mapped_column(String, nullable=True)
    price: Mapped[float]
    discount_price: Mapped[float | None] = mapped_column(nullable=True)
    currency: Mapped[str] = mapped_column(String(3), default="EUR")
    rating: Mapped[float | None] = mapped_column(nullable=True)
    category: Mapped[str]


class ProductCreate(BaseModel):
    name: str
    description: str | None = None
    price: float
    discount_price: float | None = None
    currency: str = "EUR"
    rating: float | None = None
    category: str


class Product(ProductBase):
    __tablename__ = 'products'
    __table_args__ = {'extend_existing': True}
    id: Mapped[UUID] = mapped_column(primary_key=True, index=True)
    created_at = Mapped[DateTime]
    updated_at = Mapped[DateTime]

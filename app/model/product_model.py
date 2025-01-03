from __future__ import annotations

from uuid import UUID, uuid4

from app.config.database import Base
from pydantic import BaseModel, Field
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, DateTime


class Product(Base):
    __tablename__ = 'products'

    id: Mapped[UUID] = mapped_column(primary_key=True, index=True)
    created_at = Mapped[DateTime]
    updated_at = Mapped[DateTime]
    name: Mapped[str] = mapped_column(String(100), index=True)
    description: Mapped[str | None] = mapped_column(String(1000), nullable=True)
    price: Mapped[float]
    discount_price: Mapped[float | None] = mapped_column(nullable=True)
    currency: Mapped[str] = mapped_column(String(3), default="EUR")
    rating: Mapped[float | None] = mapped_column(nullable=True)
    category: Mapped[str] = mapped_column(String(100))

class ProductCreate(BaseModel):
    id: UUID = Field(default_factory=uuid4, unique=True)
    name: str
    description: str | None = None
    price: float
    discount_price: float | None = None
    currency: str = "EUR"
    rating: float | None = None
    category: str
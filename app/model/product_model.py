import datetime
from uuid import UUID, uuid4
from sqlmodel import SQLModel, Field
from sqlalchemy import Column, DateTime, func
from pydantic import confloat, constr


class Product(SQLModel, table=True):
    __tablename__ = 'products'

    id: UUID = Field(default_factory=uuid4, primary_key=True)
    created_at: datetime.datetime = Field(default=func.now())
    updated_at: datetime.datetime | None = Field(
        sa_column=Column(
            DateTime(timezone=True), onupdate=func.now(), nullable=True
        )
    )
    name: str = Field(index=True, min_length=2, max_length=50)
    description: str | None = Field(default=None, min_length=2, max_length=200)
    price: float
    discount_price: float | None = Field(default=None)
    currency: str = Field(default='EUR', min_length=3, max_length=3)
    rating: float | None = Field(default=None)
    category: str = Field(index=True, min_length=2, max_length=30)

class ProductCreate(SQLModel):
    name: constr(min_length=2, max_length=50)
    description: constr(min_length=2, max_length=200) | None = None
    price: confloat(ge=0.01)
    discount_price: confloat(ge=0.01) | None = None
    currency: constr(min_length=3, max_length=3) = "EUR"
    rating: confloat(ge=0, le=5) | None = None
    category: constr(min_length=2, max_length=30)

class ProductEdit(SQLModel):
    name: constr(min_length=2, max_length=50) | None = None
    description: constr(min_length=2, max_length=200) | None = None
    price: confloat(ge=0.01) | None = None
    discount_price: confloat(ge=0.01) | None = None
    currency: constr(min_length=3, max_length=3) | None = None
    rating: confloat(ge=0, le=5) | None = None
    category: constr(min_length=2, max_length=30) | None = None

class ProductRead(SQLModel):
    id: UUID
    created_at: datetime.datetime
    updated_at: datetime.datetime | None
    name: str
    description: str | None
    price: float
    discount_price: float | None
    currency: str = "EUR"
    rating: float | None
    category: str
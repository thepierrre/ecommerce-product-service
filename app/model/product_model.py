import datetime
from uuid import UUID, uuid4
from sqlmodel import SQLModel, Field
from sqlalchemy import Column, DateTime, func


class Product(SQLModel, table=True):
    __tablename__ = 'products'

    id: UUID = Field(default_factory=uuid4, primary_key=True)
    created_at: datetime.datetime = Field(default=func.now())
    updated_at: datetime.datetime | None = Field(
        sa_column=Column(
            DateTime(timezone=True), onupdate=func.now(), nullable=True
        )
    )
    name: str = Field(index=True)
    description: str | None = Field(default=None)
    price: float
    discount_price: float | None = Field(default=None)
    currency: str = Field(default='EUR')
    rating: float | None = Field(default=None)
    category: str

class ProductCreate(SQLModel):
    name: str
    description: str | None = None
    price: float
    discount_price: float | None = None
    currency: str = "EUR"
    rating: float | None = None
    category: str

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
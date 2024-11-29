from decimal import Decimal
from datetime import datetime
import uuid
from sqlmodel import Field, SQLModel


class ProductBase(SQLModel):
    name: str
    description: str | None = None
    price: Decimal
    discount_price: Decimal | None = None
    currency: str | None = "EUR"
    rating: Decimal | None = None
    category: str

class ProductCreate(ProductBase):
    pass

class Product(ProductBase, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)
    name: str = Field(index=True)

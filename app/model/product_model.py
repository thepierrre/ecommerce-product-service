from decimal import Decimal
from datetime import datetime
import uuid
from sqlmodel import Field, SQLModel


class Product(SQLModel, table=True):
    id: uuid.UUID = Field(default_factory = uuid.uuid4, primary_key=True)
    name: str = Field(index=True)
    description: str | None
    price: Decimal
    discount_price: Decimal | None
    currency: str | None = Field(default = "EUR")
    rating: Decimal | None
    created_at: datetime
    updated_at: datetime | None
    category: str

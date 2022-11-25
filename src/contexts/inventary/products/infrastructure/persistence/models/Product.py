from typing import Literal
from uuid import UUID, uuid4

from beanie import Document
from pydantic import Field


class ProductMongo(Document):
    ProductId: UUID = Field(default_factory=uuid4)
    name: str
    status: Literal[1, 0]
    stock: float
    description: str
    price: float

    class Collection:
        name = "products"

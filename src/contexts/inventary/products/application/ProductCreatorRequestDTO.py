from dataclasses import dataclass


@dataclass
class ProductCreatorRequestDTO:
    product_id: str
    name: str
    status: int
    stock: int
    description: str
    price: float

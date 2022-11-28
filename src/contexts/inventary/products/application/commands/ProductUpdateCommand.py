from dataclasses import dataclass


@dataclass
class ProductUpdateCommand:
    name: str
    status: int
    stock: int
    description: str
    price: float

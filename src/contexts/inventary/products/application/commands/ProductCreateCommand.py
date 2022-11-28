from dataclasses import dataclass


@dataclass
class ProductCreateCommand:
    product_id: str
    name: str
    status: int
    stock: int
    description: str
    price: float

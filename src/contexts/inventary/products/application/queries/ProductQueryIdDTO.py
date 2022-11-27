from dataclasses import dataclass


@dataclass
class ProductQueryIdDTO:
    product_id: str
    name: str
    status: int
    stock: int
    description: str
    price: float
    discount: float
    final_price: float

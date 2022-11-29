from dataclasses import dataclass
from typing import Literal


@dataclass
class ProductQueryIdDTO:
    product_id: str
    name: str
    status: int | Literal["Active", "Inactive"]
    stock: int
    description: str
    price: float
    discount: float
    final_price: float

    def __post_init__(self):
        self.status = {1: "Active", 0: "Inactive"}.get(self.status)

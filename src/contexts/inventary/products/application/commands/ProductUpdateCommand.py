from dataclasses import asdict, dataclass


@dataclass
class ProductUpdateCommand:
    name: str
    status: int
    stock: int
    description: str
    price: float

    def to_dict(self):
        return {k: v for k, v in asdict(self).items()}

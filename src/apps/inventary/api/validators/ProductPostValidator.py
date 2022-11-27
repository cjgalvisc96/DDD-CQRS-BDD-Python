from uuid import UUID

from pydantic import BaseModel, validator

from src.contexts.shared.domain import DomainConstants


class ProductPostValidator(BaseModel):
    product_id: str
    name: str
    status: int
    stock: int
    description: str
    price: float

    @validator("product_id")
    def validate_product_id(cls, product_id):
        try:
            UUID(hex=product_id, version=DomainConstants["uuid_version"])
        except ValueError:
            raise ValueError("product_id need to be a valid uuid")
        return product_id

    @validator("status")
    def validate_status(cls, status):
        if status not in [1, 0]:
            raise ValueError("status needs to be 1 or 0")
        return status

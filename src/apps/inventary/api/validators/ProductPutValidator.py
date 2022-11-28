from pydantic import BaseModel, validator


class ProductPutValidator(BaseModel):
    name: str
    status: int
    stock: int
    description: str
    price: float

    @validator("status")
    def validate_status(cls, status):
        if status not in [1, 0]:
            raise ValueError("status needs to be 1 or 0")
        return status

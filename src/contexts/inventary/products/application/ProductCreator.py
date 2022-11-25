from src.contexts.inventary.products.application import (
    ProductCreatorRequestDTO,
)
from src.contexts.inventary.products.domain import Product, ProductRepository


class ProductCreator:
    def __init__(self, repository: ProductRepository):
        self._repository = repository

    async def run(self, *, request: ProductCreatorRequestDTO):
        product = Product.create(
            id=request.id, name=request.name, duration=request.duration
        )
        return await self._repository.save(product=product)

from src.contexts.inventary.products.application import (
    ProductCreatorRequestDTO,
)
from src.contexts.inventary.products.domain import Product, ProductRepository


class ProductCreator:
    def __init__(self, repository: ProductRepository):
        self._repository = repository

    async def run(self, *, request: ProductCreatorRequestDTO):
        product = Product.create(
            product_id=request.product_id,
            name=request.name,
            status=request.status,
            stock=request.stock,
            description=request.description,
            price=request.price,
        )
        return await self._repository.save(product=product)

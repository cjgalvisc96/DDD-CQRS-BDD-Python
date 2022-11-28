from src.contexts.inventary.products.domain import ProductWriteRepository
from src.contexts.inventary.products.domain.Product import Product

from .ProductCommandService import ProductCommandService
from .ProductCreateCommand import ProductCreateCommand
from .ProductUpdateCommand import ProductUpdateCommand


class ProductCommandServiceImp(ProductCommandService):
    def __init__(
        self,
        repository: ProductWriteRepository,
    ):
        self._repository = repository

    async def save(self, *, product_create_command: ProductCreateCommand):
        product = Product.create(
            product_id=product_create_command.product_id,
            name=product_create_command.name,
            status=product_create_command.status,
            stock=product_create_command.stock,
            description=product_create_command.description,
            price=product_create_command.price,
        )
        return await self._repository.save(product=product)

    async def update(
        self, *, product_id: str, product_update_command: ProductUpdateCommand
    ):
        ...

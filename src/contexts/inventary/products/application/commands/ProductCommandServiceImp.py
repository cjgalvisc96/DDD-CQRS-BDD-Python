from src.contexts.inventary.products.domain import ProductWriteRepository
from src.contexts.inventary.products.domain.Product import Product
from src.contexts.shared.domain import DomainException

from .ProductCommandService import ProductCommandService
from .ProductCreateCommand import ProductCreateCommand
from .ProductUpdateCommand import ProductUpdateCommand


class ProductCommandServiceImp(ProductCommandService):
    def __init__(self, *, repository: ProductWriteRepository):
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
        result = await self._repository.save(product=product)
        if not result:
            raise DomainException("Product already exists")

    async def update(
        self, *, product_id: str, product_update_command: ProductUpdateCommand
    ):
        result = await self._repository.update(
            product_id=product_id, data=product_update_command.to_dict()
        )
        if not result:
            raise DomainException("Product don't exists")

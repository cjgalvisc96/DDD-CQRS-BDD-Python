from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends, status

from src.apps.inventary.api.dependecy_injection import InventaryContainer
from src.apps.inventary.api.validators import ProductPostValidator
from src.contexts.inventary.products.application import (
    ProductCommandService,
    ProductCreateCommand,
)
from src.contexts.shared.domain import DomainException

router = APIRouter(prefix="", tags=["WriteProduct"])


class ProductCommandController:
    @router.post("/", status_code=status.HTTP_201_CREATED)
    @inject
    async def run(
        product: ProductPostValidator,
        product_write_service: ProductCommandService = Depends(
            Provide[InventaryContainer.products_package.product_write_service]
        ),
    ):
        product_create_command = ProductCreateCommand(
            product_id=product.product_id,
            name=product.name,
            status=product.status,
            stock=product.stock,
            description=product.description,
            price=product.price,
        )

        result = await product_write_service.save(
            product_create_command=product_create_command
        )
        if not result:
            raise DomainException("Product already exists")

from uuid import UUID

from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends, status

from src.apps.inventary.api.dependecy_injection import ApplicationContainer
from src.apps.inventary.api.validators import (
    ProductPostValidator,
    ProductPutValidator,
)
from src.contexts.inventary.products.application import (
    ProductCommandService,
    ProductCreateCommand,
    ProductUpdateCommand,
)

router = APIRouter(prefix="", tags=["WriteProduct"])


class ProductCommandController:
    @router.post("/", status_code=status.HTTP_201_CREATED)
    @inject
    async def create_product(
        product: ProductPostValidator,
        product_write_service: ProductCommandService = Depends(
            Provide[
                ApplicationContainer.products_package.product_write_service
            ]
        ),
    ):
        await product_write_service.save(
            product_create_command=ProductCreateCommand(
                product_id=product.product_id,
                name=product.name,
                status=product.status,
                stock=product.stock,
                description=product.description,
                price=product.price,
            )
        )

    @router.put(
        path="/{product_id}",
        status_code=status.HTTP_200_OK,
    )
    @inject
    async def update_product(
        product_id: UUID,
        product: ProductPutValidator,
        product_write_service: ProductCommandService = Depends(
            Provide[
                ApplicationContainer.products_package.product_write_service
            ]
        ),
    ):
        await product_write_service.update(
            product_id=str(product_id),
            product_update_command=ProductUpdateCommand(
                name=product.name,
                status=product.status,
                stock=product.stock,
                description=product.description,
                price=product.price,
            ),
        )

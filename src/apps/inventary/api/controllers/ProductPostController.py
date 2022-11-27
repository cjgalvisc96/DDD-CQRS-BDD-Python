from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends, status

from src.apps.inventary.api.dependecy_injection import InventaryContainer
from src.apps.inventary.api.validators import ProductPostValidator
from src.contexts.inventary.products.application import (
    ProductCreator,
    ProductCreatorRequestDTO,
)
from src.contexts.shared.domain import DomainException

router = APIRouter(prefix="", tags=["WriteProduct"])


class ProductPostController:
    @router.post("/", status_code=status.HTTP_201_CREATED)
    @inject
    async def run(
        product: ProductPostValidator,
        product_creator: ProductCreator = Depends(
            Provide[InventaryContainer.products_package.product_creator]
        ),
    ):
        product_creator_request_dto = ProductCreatorRequestDTO(
            product_id=product.product_id,
            name=product.name,
            status=product.status,
            stock=product.stock,
            description=product.description,
            price=product.price,
        )

        creator_result = await product_creator.run(
            request=product_creator_request_dto
        )
        if not creator_result:
            raise DomainException("Product already exists")

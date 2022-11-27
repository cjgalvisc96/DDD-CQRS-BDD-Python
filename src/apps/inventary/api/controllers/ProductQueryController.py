from uuid import UUID

from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends, HTTPException, status

from src.apps.inventary.api.dependecy_injection import InventaryContainer
from src.contexts.inventary.products.application import (
    ProductQueryIdDTO,
    ProductQueryService,
)

router = APIRouter(prefix="", tags=["ReadProducts"])


class ProductQueryController:
    @router.get(
        path="/{product_id}",
        response_model=ProductQueryIdDTO,
        status_code=status.HTTP_200_OK,
    )
    @inject
    async def get_product_by_id(
        product_id: UUID,
        product_query_service: ProductQueryService = Depends(
            Provide[InventaryContainer.products_package.product_query_service]
        ),
    ):
        product = await product_query_service.find_product_by_id(
            product_id=str(product_id)
        )
        if not product:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

        return product

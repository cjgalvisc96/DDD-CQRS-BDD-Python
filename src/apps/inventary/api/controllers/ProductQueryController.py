from typing import Any
from uuid import UUID

from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends, HTTPException, status

from src.apps.inventary.api.dependecy_injection import InventaryContainer
from src.contexts.inventary.products.application import (
    ProductQueryIdDTO,
    ProductQueryService,
)
from src.contexts.inventary.products.infrastructure import MemoryCacheService
from src.contexts.shared.infrastucture import CacheService

router = APIRouter(prefix="", tags=["ReadProducts"])


async def apply_cache_to_product(
    *, product: ProductQueryIdDTO, cache: Any
) -> ProductQueryIdDTO:
    in_cache = await cache.get("Status")
    if not in_cache:
        await cache.set(
            key="Status",
            value=product.status,
        )
        return product

    product.status = await cache.get("Status")
    return product


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
        cache_service: CacheService = Depends(MemoryCacheService),
    ):
        product = await product_query_service.find_product_by_id(
            product_id=str(product_id)
        )
        if not product:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

        product_with_cache_applied = await apply_cache_to_product(
            product=product,
            cache=cache_service.get_cache(),
        )

        return product_with_cache_applied

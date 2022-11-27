from fastapi import APIRouter

from src.apps.inventary.api.controllers import (
    product_post_controller_router,
    product_query_controller_router,
)

products_router = APIRouter(prefix="/products")


products_router.include_router(router=product_post_controller_router)
products_router.include_router(router=product_query_controller_router)

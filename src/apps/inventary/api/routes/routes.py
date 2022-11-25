from fastapi import APIRouter

from src.apps.inventary.api.controllers import product_post_controller_router

router = APIRouter()

router.include_router(product_post_controller_router)

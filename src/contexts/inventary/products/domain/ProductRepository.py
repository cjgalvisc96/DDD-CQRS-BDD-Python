from abc import ABC, abstractstaticmethod

from src.contexts.inventary.products.domain.Product import Product


class ProductRepository(ABC):
    @abstractstaticmethod
    async def save(*, product: Product) -> Product | bool:
        ...

    @abstractstaticmethod
    async def update(*, product_id: str) -> Product | bool:
        ...

    @abstractstaticmethod
    async def search_by_product_id(*, product_id: str) -> Product:
        ...

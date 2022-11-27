from abc import ABC, abstractstaticmethod

from src.contexts.inventary.products.domain.Product import Product


class ProductReadRepository(ABC):
    @abstractstaticmethod
    async def find_product_by_id(*, product_id: str) -> Product:
        ...

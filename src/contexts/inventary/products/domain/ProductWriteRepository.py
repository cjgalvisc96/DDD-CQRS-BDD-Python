from abc import ABC, abstractstaticmethod

from src.contexts.inventary.products.domain.Product import Product


class ProductWriteRepository(ABC):
    @abstractstaticmethod
    async def save(*, product: Product) -> bool:
        ...

    @abstractstaticmethod
    async def update(*, product_id: str, data) -> bool:
        ...

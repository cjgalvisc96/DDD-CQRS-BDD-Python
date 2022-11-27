from abc import ABC, abstractmethod

from .ProductQueryIdDTO import ProductQueryIdDTO


class ProductQueryService(ABC):
    @abstractmethod
    async def find_product_by_id(*, product_id: str) -> ProductQueryIdDTO:
        ...

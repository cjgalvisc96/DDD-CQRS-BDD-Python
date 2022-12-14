from abc import ABC, abstractmethod


class ExternalDiscountService(ABC):
    @abstractmethod
    async def get_discount_percentage(self, *, product_id: str) -> int:
        ...

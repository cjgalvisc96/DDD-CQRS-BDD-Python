from abc import ABC, abstractmethod

from .ProductCreateCommand import ProductCreateCommand
from .ProductUpdateCommand import ProductUpdateCommand


class ProductCommandService(ABC):
    @abstractmethod
    async def save(self, *, product_create_command: ProductCreateCommand):
        ...

    @abstractmethod
    async def update(
        self, *, product_id: str, product_update_command: ProductUpdateCommand
    ):
        ...

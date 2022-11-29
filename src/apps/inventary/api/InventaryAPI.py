from abc import ABC, abstractmethod


class InventaryAPI(ABC):
    @abstractmethod
    async def start(self) -> None:
        ...

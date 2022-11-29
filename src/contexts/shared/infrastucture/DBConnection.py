from abc import ABC, abstractmethod


class DBConnection(ABC):
    @abstractmethod
    async def init_db(self):
        ...

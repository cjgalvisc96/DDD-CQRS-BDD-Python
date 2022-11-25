from abc import ABC, abstractstaticmethod


class DBConnection(ABC):
    @abstractstaticmethod
    async def init_db(self):
        ...

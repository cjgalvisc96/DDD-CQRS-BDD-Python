from abc import ABC, abstractstaticmethod


class CacheService(ABC):
    @abstractstaticmethod
    async def init():
        ...

    @abstractstaticmethod
    async def close():
        ...

    @abstractstaticmethod
    def get_cache():
        ...

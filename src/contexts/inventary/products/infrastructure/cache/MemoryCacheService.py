from fastapi_cache import CacheRegistry, caches, close_caches
from fastapi_cache.backends.memory import CACHE_KEY, InMemoryCacheBackend

from src.contexts.shared.infrastucture import CacheService


class MemoryCacheService(CacheService):
    def __init__(self, *, cache_ttl: int) -> None:
        self.cache_ttl = cache_ttl

    @staticmethod
    async def init():
        caches.flush()
        memory_cache_backend = InMemoryCacheBackend()
        caches.set(name=CACHE_KEY, cache=memory_cache_backend)

    @staticmethod
    async def close():
        await close_caches()

    @staticmethod
    def get_cache() -> CacheRegistry:
        return caches.get(CACHE_KEY)

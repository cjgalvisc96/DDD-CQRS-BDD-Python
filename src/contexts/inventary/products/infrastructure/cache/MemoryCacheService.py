from fastapi_cache import CacheRegistry, caches, close_caches
from fastapi_cache.backends.memory import CACHE_KEY, InMemoryCacheBackend

from src.contexts.shared.infrastucture import CacheService, Singlenton


class MemoryCacheService(Singlenton, CacheService):
    async def init(self):
        memory_cache_backend = InMemoryCacheBackend()
        caches.flush()
        # TODO: expiration time in VARS
        # await redis_cache_backend.expire(key=CACHE_KEY, ttl=60)
        caches.set(name=CACHE_KEY, cache=memory_cache_backend)

    @staticmethod
    async def close():
        await close_caches()

    @staticmethod
    def get_cache() -> CacheRegistry:
        return caches.get(CACHE_KEY)

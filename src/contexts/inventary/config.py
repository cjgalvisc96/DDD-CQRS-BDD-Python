from functools import lru_cache

from pydantic import BaseSettings


class Settings(BaseSettings):
    API_PORT: int = 5000
    MONGO_URL: str = "mongodb://localhost:27017/inventary_dev"
    EXTERNAL_PARTY_SERVICE: str = "https://mockapi.io"
    # TESTS
    TEST_MONGO_URL: str = "mongodb://localhost:27017/inventary_test"

    class Config:
        case_sensitive = True
        env_file = ".env"  # TODO: Fix file read


@lru_cache()
def get_inventary_settings() -> Settings:
    return Settings()


inventary_settings = get_inventary_settings()

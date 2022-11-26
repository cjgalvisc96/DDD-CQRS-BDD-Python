from functools import lru_cache

from dotenv import load_dotenv
from pydantic import BaseSettings

load_dotenv()


class Settings(BaseSettings):
    API_PORT: int
    MONGO_URL: str
    EXTERNAL_PARTY_SERVICE: str
    # TESTS
    TEST_MONGO_URL: str

    class Config:
        case_sensitive = True
        env_file = ".env"


@lru_cache()
def get_inventary_settings() -> Settings:
    return Settings()


inventary_settings = get_inventary_settings()

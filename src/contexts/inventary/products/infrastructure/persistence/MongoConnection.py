from typing import Any, List

from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase

from src.contexts.shared.infrastucture import DBConnection


class MongoConnection(DBConnection):
    def __init__(self, *, db_url: str, models: List[Any]) -> None:
        self.db_url = db_url
        self.models = models
        self.client = None | AsyncIOMotorClient
        self.db = None | AsyncIOMotorDatabase

    async def init_db(self):
        self.client = AsyncIOMotorClient(self.db_url)
        self.db = self.client.get_database()
        await init_beanie(database=self.db, document_models=self.models)

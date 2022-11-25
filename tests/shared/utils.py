from dataclasses import dataclass

from faker import Faker
from motor.motor_asyncio import AsyncIOMotorDatabase

from src.contexts.inventary import inventary_settings
from src.contexts.inventary.products.infrastructure import (
    MongoConnection,
    __beanie_models__,
)


def mongo_connection():
    return MongoConnection(
        db_url=inventary_settings.TEST_MONGO_URL, models=__beanie_models__
    )


async def clear_mongo_database(*, mongo_db: AsyncIOMotorDatabase):
    for collection in await mongo_db.list_collections():
        await mongo_db[collection["name"]].delete_many({})


@dataclass
class FakerData:
    faker_data = Faker(locale="en_us")

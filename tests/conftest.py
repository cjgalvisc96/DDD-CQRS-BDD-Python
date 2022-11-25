import pytest_asyncio

from tests.shared.utils import clear_mongo_database, mongo_connection


@pytest_asyncio.fixture
async def mongo_db():
    client = mongo_connection()
    await client.init_db()
    await clear_mongo_database(mongo_db=client.db)

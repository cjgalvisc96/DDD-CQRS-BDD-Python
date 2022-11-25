import pytest

from src.contexts.inventary.products.infrastructure import (
    MongoProductRepository,
)
from tests.contexts.inventary.products.domain import ProductMother


@pytest.mark.unit
@pytest.mark.asyncio
async def test_save_product(mongo_db):
    repository = MongoProductRepository()
    product = ProductMother().create_random_valid()
    await repository.save(product=product)
    # TODO: USE native DB for get product saved
    product_founded = await repository.search(product_id=product.id.value)

    assert product_founded.id.value == product.id.value
    assert product_founded.name.value == product.name.value
    assert product_founded.status.value == product.status.value
    assert product_founded.stock.value == product.stock.value
    assert product_founded.description.value == product.description.value
    assert product_founded.price.value == product.price.value


@pytest.mark.unit
@pytest.mark.asyncio
async def test_search_existent_product(mongo_db):
    ...


@pytest.mark.unit
@pytest.mark.asyncio
async def test_search_inexistent_product(mongo_db):
    ...


@pytest.mark.unit
@pytest.mark.asyncio
async def test_update_existent_product(mongo_db):
    ...


@pytest.mark.unit
@pytest.mark.asyncio
async def test_update_inexistent_product(mongo_db):
    ...

import pytest

from src.contexts.inventary.products.infrastructure import (
    MongoProductRepository,
    ProductMongo,
)
from tests.contexts.inventary.products.domain import ProductMother


@pytest.mark.unit
@pytest.mark.asyncio
async def test_save_product(mongo_db):
    product = ProductMother().create_random_valid()
    repository = MongoProductRepository()
    await repository.save(product=product)
    products = await ProductMongo.find_all().to_list()

    assert len(products) == 1
    product_founded = products[0]
    assert isinstance(product_founded, ProductMongo)

    assert str(product_founded.ProductId) == product.product_id.value
    assert product_founded.name == product.name.value
    assert product_founded.status == product.status.value
    assert product_founded.stock == product.stock.value
    assert product_founded.description == product.description.value
    assert product_founded.price == product.price.value


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

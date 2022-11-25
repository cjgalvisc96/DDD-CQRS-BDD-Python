import pytest

from src.contexts.inventary.products.domain import Product
from src.contexts.inventary.products.infrastructure import (
    MongoProductRepository,
    ProductMongo,
)
from tests.contexts.inventary.products.domain import ProductMother


@pytest.mark.unit
@pytest.mark.asyncio
async def test_save_valid_product(mongo_db):
    product_to_save = ProductMother().create_random_valid()
    mongo_repository = MongoProductRepository()
    await mongo_repository.save(product=product_to_save)
    products_founded = await ProductMongo.find_all().to_list()

    assert len(products_founded) == 1
    product_founded = products_founded[0]
    assert isinstance(product_founded, ProductMongo)

    assert str(product_founded.ProductId) == product_to_save.product_id.value
    assert product_founded.name == product_to_save.name.value
    assert product_founded.status == product_to_save.status.value
    assert product_founded.stock == product_to_save.stock.value
    assert product_founded.description == product_to_save.description.value
    assert product_founded.price == product_to_save.price.value


@pytest.mark.unit
@pytest.mark.asyncio
async def test_search_existent_product(mongo_db):
    product_to_save = ProductMother().create_random_valid()
    product_saved = ProductMongo(
        ProductId=product_to_save.product_id.value,
        name=product_to_save.name.value,
        status=product_to_save.status.value,
        stock=product_to_save.stock.value,
        description=product_to_save.description.value,
        price=product_to_save.price.value,
    )
    await product_saved.create()

    mongo_repository = MongoProductRepository()
    product_founded = await mongo_repository.search_by_product_id(
        product_id=product_to_save.product_id.value
    )
    assert isinstance(product_founded, Product)

    assert product_founded.product_id.value == product_to_save.product_id.value
    assert product_founded.name.value == product_to_save.name.value
    assert product_founded.status.value == product_to_save.status.value
    assert product_founded.stock.value == product_to_save.stock.value
    assert (
        product_founded.description.value == product_to_save.description.value
    )
    assert product_founded.price.value == product_to_save.price.value


@pytest.mark.unit
@pytest.mark.asyncio
async def test_search_inexistent_product(mongo_db):
    inexistent_product_id = ProductMother().get_random_valid_uuid4()
    mongo_repository = MongoProductRepository()
    product_founded = await mongo_repository.search_by_product_id(
        product_id=inexistent_product_id
    )
    assert isinstance(product_founded, bool)
    assert product_founded == False


@pytest.mark.unit
@pytest.mark.asyncio
async def test_update_existent_product(mongo_db):
    ...


@pytest.mark.unit
@pytest.mark.asyncio
async def test_update_inexistent_product(mongo_db):
    ...

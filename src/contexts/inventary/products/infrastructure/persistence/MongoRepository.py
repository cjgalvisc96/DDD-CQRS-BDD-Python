from uuid import UUID

from beanie.operators import Set
from pymongo.results import UpdateResult

from src.contexts.inventary.products.domain import (
    Product,
    ProductDescription,
    ProductName,
    ProductPrice,
    ProductRepository,
    ProductStatus,
    ProductStock,
)
from src.contexts.inventary.products.infrastructure import ProductMongo
from src.contexts.inventary.shared.domain import ProductId
from src.contexts.shared.domain import DomainConstants


class MongoProductRepository(ProductRepository):
    @staticmethod
    async def save(*, product: Product) -> Product | bool:
        update_result = await ProductMongo.find_one(
            ProductMongo.ProductId
            == UUID(
                product.product_id.value,
                version=DomainConstants["uuid_version"],
            )
        ).upsert(
            Set({}),
            on_insert=ProductMongo(
                ProductId=product.product_id.value,
                name=product.name.value,
                status=product.status.value,
                stock=product.stock.value,
                description=product.description.value,
                price=product.price.value,
            ),
        )
        if isinstance(update_result, UpdateResult):
            return False

        return product

    @staticmethod
    async def update(*, product_id: str) -> Product:
        ...

    @staticmethod
    async def search_by_product_id(*, product_id: str) -> Product | bool:
        product = await ProductMongo.find_one(
            ProductMongo.ProductId
            == UUID(hex=product_id, version=DomainConstants["uuid_version"])
        )
        if not product:
            return False

        return Product(
            product_id=ProductId(str(product.ProductId)),
            name=ProductName(product.name),
            status=ProductStatus(product.status),
            stock=ProductStock(product.stock),
            description=ProductDescription(product.description),
            price=ProductPrice(product.price),
        )

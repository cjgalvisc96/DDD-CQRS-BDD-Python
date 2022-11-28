from typing import Any, Dict
from uuid import UUID

from beanie.operators import Set
from pymongo.results import UpdateResult

from src.contexts.inventary.products.domain import ProductWriteRepository
from src.contexts.inventary.products.domain.Product import Product
from src.contexts.inventary.products.infrastructure import ProductMongo
from src.contexts.shared.domain import DomainConstants


class MongoProductWriteRepository(ProductWriteRepository):
    @staticmethod
    async def save(*, product: Product) -> bool:
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
        return False if isinstance(update_result, UpdateResult) else True

    @staticmethod
    async def update(*, product_id: str, data: Dict[str, Any]) -> bool:
        update_result = await ProductMongo.find_one(
            ProductMongo.ProductId
            == UUID(
                product_id,
                version=DomainConstants["uuid_version"],
            )
        ).update(
            Set(
                {
                    ProductMongo.name: data["name"],
                    ProductMongo.status: data["status"],
                    ProductMongo.stock: data["stock"],
                    ProductMongo.description: data["description"],
                    ProductMongo.price: data["price"],
                }
            ),
        )
        return True if update_result.modified_count == 1 else False

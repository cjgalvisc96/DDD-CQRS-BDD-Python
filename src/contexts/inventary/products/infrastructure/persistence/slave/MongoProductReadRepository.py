from uuid import UUID

from src.contexts.inventary.products.domain import (
    ProductDescription,
    ProductName,
    ProductPrice,
    ProductReadRepository,
    ProductStatus,
    ProductStock,
)
from src.contexts.inventary.products.domain.Product import Product
from src.contexts.inventary.products.infrastructure import ProductMongo
from src.contexts.inventary.shared.domain import ProductId
from src.contexts.shared.domain import DomainConstants


class MongoProductReadRepository(ProductReadRepository):
    @staticmethod
    async def find_product_by_id(*, product_id: str) -> Product | bool:
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

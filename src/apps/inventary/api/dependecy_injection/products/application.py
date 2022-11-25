from dependency_injector import containers, providers

from src.contexts.inventary.products.application import ProductCreator
from src.contexts.inventary.products.infrastructure import (
    MongoProductRepository,
)


class ProductsContainer(containers.DeclarativeContainer):
    product_repository = providers.Factory(MongoProductRepository)
    product_creator = providers.Factory(ProductCreator, product_repository)

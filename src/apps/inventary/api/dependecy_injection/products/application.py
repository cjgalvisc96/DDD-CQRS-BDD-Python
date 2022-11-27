from dependency_injector import containers, providers

from src.contexts.inventary.products.application import (
    ProductCreator,
    ProductQueryServiceImp,
)
from src.contexts.inventary.products.infrastructure import (
    MongoProductReadRepository,
    MongoProductRepository,
)
from src.contexts.inventary.products.infrastructure.external_services import (
    MockAPIIOExternalDiscountService,
)


class ProductsContainer(containers.DeclarativeContainer):
    product_repository = providers.Factory(MongoProductRepository)
    product_creator = providers.Factory(ProductCreator, product_repository)

    product_read_repository = providers.Factory(MongoProductReadRepository)
    external_discount_service = providers.Factory(
        MockAPIIOExternalDiscountService
    )
    product_query_service = providers.Factory(
        ProductQueryServiceImp,
        product_read_repository,
        external_discount_service,
    )

from dependency_injector import containers, providers

from src.contexts.inventary.products.application import (
    ProductCommandServiceImp,
    ProductQueryServiceImp,
)
from src.contexts.inventary.products.infrastructure import (
    MongoProductReadRepository,
    MongoProductWriteRepository,
)
from src.contexts.inventary.products.infrastructure.external_services import (
    MockAPIIOExternalDiscountService,
)


class ProductsContainer(containers.DeclarativeContainer):
    product_write_repository = providers.Factory(MongoProductWriteRepository)
    product_write_service = providers.Factory(
        ProductCommandServiceImp,
        product_write_repository,
    )

    product_read_repository = providers.Factory(MongoProductReadRepository)
    external_discount_service = providers.Factory(
        MockAPIIOExternalDiscountService
    )
    product_query_service = providers.Factory(
        ProductQueryServiceImp,
        product_read_repository,
        external_discount_service,
    )

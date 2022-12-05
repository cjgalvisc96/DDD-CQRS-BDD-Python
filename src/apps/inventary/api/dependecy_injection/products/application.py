from dependency_injector import containers, providers

from src.contexts.inventary import inventary_settings
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
    product_write_repository = providers.Singleton(MongoProductWriteRepository)
    product_write_service = providers.Factory(
        ProductCommandServiceImp,
        repository=product_write_repository,
    )

    product_read_repository = providers.Singleton(MongoProductReadRepository)
    external_discount_service = providers.Singleton(
        MockAPIIOExternalDiscountService,
        url=inventary_settings.EXTERNAL_PARTY_SERVICE,
    )
    product_query_service = providers.Factory(
        ProductQueryServiceImp,
        repository=product_read_repository,
        external_discount_service=external_discount_service,
    )

from dependency_injector import containers, providers

from src.apps.inventary.api.dependecy_injection import ProductsContainer
from src.contexts.inventary import inventary_settings
from src.contexts.inventary.products.infrastructure import (
    MemoryCacheService,
    MongoConnection,
    __beanie_models__,
)
from src.contexts.shared.domain import DomainConstants
from src.contexts.shared.infrastucture import LoggingLogger


class ApplicationContainer(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(
        modules=[
            "src.apps.inventary.api.controllers.ProductCommandController",
            "src.apps.inventary.api.controllers.ProductQueryController",
        ],
    )
    products_package = providers.Container(ProductsContainer)
    logger_service = providers.Singleton(
        LoggingLogger,
        filename=DomainConstants["logger_filename"],
        name=DomainConstants["logger_name"],
        level=DomainConstants["logger_level"],
        format_=DomainConstants["logger_format"],
        date_format=DomainConstants["logger_date_format"],
    )
    db_service = providers.Singleton(
        MongoConnection,
        db_url=inventary_settings.MONGO_URL,
        models=__beanie_models__,
    )
    cache_service = providers.Singleton(
        MemoryCacheService, cache_ttl=inventary_settings.CACHE_TTL
    )

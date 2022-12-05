from dependency_injector.wiring import Provide, inject

from src.apps.inventary.api import InventaryAPI, InventaryFastAPI
from src.apps.inventary.api.dependecy_injection import ApplicationContainer
from src.contexts.inventary import inventary_settings
from src.contexts.shared.domain import Logger
from src.contexts.shared.infrastucture import CacheService, DBConnection


@inject
def get_api(
    logger_service: Logger = Provide[ApplicationContainer.logger_service],
    db_service: DBConnection = Provide[ApplicationContainer.db_service],
    cache_service: CacheService = Provide[ApplicationContainer.cache_service],
) -> InventaryAPI:
    inventary_api = InventaryFastAPI(
        host=inventary_settings.API_HOST,
        port=inventary_settings.API_PORT,
        logger=logger_service,
        db=db_service,
        cache_service=cache_service,
    )
    return inventary_api


if __name__ == "__main__":
    container = ApplicationContainer()
    container.wire(modules=[__name__])

    inventary_api = get_api()
    try:
        inventary_api.start()
    except Exception as error:
        inventary_api.logger.error(message=f"Start() => {error}")

from src.apps.inventary.api import InventaryAPI
from src.contexts.inventary import inventary_settings
from src.contexts.inventary.products.infrastructure import (
    MongoConnection,
    __beanie_models__,
)
from src.contexts.shared.domain import DomainConstants
from src.contexts.shared.infrastucture import LoggingLogger

# TODO: try to  implement DependencyInjection
inventary_api = InventaryAPI(
    port=inventary_settings.API_PORT,
    logger=LoggingLogger(
        filename=DomainConstants["logger_filename"],
        name=DomainConstants["logger_name"],
        level=DomainConstants["logger_level"],
        format_=DomainConstants["logger_format"],
        date_format=DomainConstants["logger_date_format"],
    ),
    db=MongoConnection(
        db_url=inventary_settings.MONGO_URL, models=__beanie_models__
    ),
)
if __name__ == "__main__":
    try:
        inventary_api.start()
    except Exception as error:
        inventary_api.logger.error(message=f"Start() => {error}")

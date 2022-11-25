from src.apps.inventary.api import InventaryAPI
from src.contexts.inventary import inventary_settings
from src.contexts.inventary.products.infrastructure import (
    MongoConnection,
    __beanie_models__,
)
from src.contexts.shared.infrastucture import LoggingLogger

if __name__ == "__main__":
    try:
        InventaryAPI(
            port=inventary_settings.API_PORT,
            logger=LoggingLogger(),
            db=MongoConnection(
                db_url=inventary_settings.MONGO_URL, models=__beanie_models__
            ),
        ).start()
    except Exception as error:
        # TODO: use logger
        print(f"[ERROR]Start() => {error}")

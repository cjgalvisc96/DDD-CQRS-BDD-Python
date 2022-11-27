from typing import Any, List

from .persistence.models.Product import ProductMongo
from .persistence.MongoConnection import MongoConnection
from .persistence.master.MongoRepository import MongoProductRepository
from .persistence.slave.MongoProductReadRepository import (
    MongoProductReadRepository,
)

__beanie_models__: List[Any] = [ProductMongo]

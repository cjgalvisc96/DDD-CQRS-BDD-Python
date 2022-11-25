from typing import Any, List

from .persistence.models.Product import ProductMongo
from .persistence.MongoConnection import MongoConnection
from .persistence.MongoRepository import MongoProductRepository

__beanie_models__: List[Any] = [ProductMongo]

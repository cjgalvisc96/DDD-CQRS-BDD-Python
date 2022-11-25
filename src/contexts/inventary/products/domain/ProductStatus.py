from src.contexts.inventary.products.domain import ProductInvalidStatusValue
from src.contexts.shared.domain import IntegerValueObject


class ProductStatus(IntegerValueObject):
    def __init__(self, value: int) -> None:
        super().__init__(value=value)
        self._ensure_value_is_1_or_0(value=value)

    def _ensure_value_is_1_or_0(self, *, value: int):
        if value not in [1, 0]:
            raise ProductInvalidStatusValue(
                f"The Product Status {value} has to be 1 0r 0"
            )

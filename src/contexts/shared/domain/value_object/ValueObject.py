from abc import ABC
from typing import Any

from src.contexts.shared.domain import InvalidArgumentError


class ValueObject(ABC):
    def __init__(self, value: Any) -> None:
        self._ensure_value_is_defined(value=value)
        self.value = value

    @staticmethod
    def _ensure_value_is_defined(*, value: Any) -> None | InvalidArgumentError:
        if value is None:
            raise InvalidArgumentError("Value must be defined")

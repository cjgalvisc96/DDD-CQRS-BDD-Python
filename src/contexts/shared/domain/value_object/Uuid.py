from uuid import UUID

from src.contexts.shared.domain import (
    DomainConstants,
    InvalidArgumentError,
    ValueObject,
)


class Uuid(ValueObject):
    def __init__(self, value: str) -> None:
        super().__init__(value=value)
        self._ensure_is_valid_uuid(id=value)

    def _ensure_is_valid_uuid(self, *, id: str) -> None:
        try:
            UUID(hex=id, version=DomainConstants["uuid_version"])
        except ValueError:
            raise InvalidArgumentError(
                f"<{Uuid.__name__}> does not allow the value <{id}>"
            )

from unittest.mock import MagicMock

from src.contexts.shared.infrastucture import LoggingLogger


class LoggingLoggerMock(LoggingLogger):
    def __init__(
        self,
        *,
        filename: str,
        name: str,
        level: str,
        format_: str,
        date_format: str,
    ) -> None:
        super().__init__(
            filename=filename,
            name=name,
            level=level,
            format_=format_,
            date_format=date_format,
        )
        self.debug_mock = MagicMock()
        self.error_mock = MagicMock()
        self.info_mock = MagicMock()

    def debug(self, *, message: str):
        self.debug_mock(message=message)

    def error(self, *, message: str):
        self.error_mock(message=message)

    def info(self, *, message: str):
        self.info_mock(message=message)

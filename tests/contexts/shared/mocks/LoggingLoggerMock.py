from unittest.mock import MagicMock

from src.contexts.shared.infrastucture import LoggingLogger


class LoggingLoggerMock(LoggingLogger):
    def __init__(self) -> None:
        super().__init__()
        self.__debug_mock = MagicMock()
        self.__error_mock = MagicMock()
        self.__info_mock = MagicMock()

    def debug(self, *, message: str):
        self.__debug_mock(message=message)

    def error(self, *, message: str):
        self.__error_mock(message=message)

    def info(self, *, message: str):
        self.__info_mock(message=message)

    def debug_has_been_called_with(self, *, expected_message: str):
        self.__debug_mock.assert_called_once()
        message_displayed = self.__debug_mock.call_args.kwargs["message"]
        assert message_displayed == expected_message

    def error_has_been_called_with(self, *, expected_message: str):
        self.__error_mock.assert_called_once()
        message_displayed = self.__error_mock.call_args.kwargs["message"]
        assert message_displayed == expected_message

    def info_has_been_called_with(self, *, expected_message: str):
        self.__info_mock.assert_called_once()
        message_displayed = self.__info_mock.call_args.kwargs["message"]
        assert message_displayed == expected_message

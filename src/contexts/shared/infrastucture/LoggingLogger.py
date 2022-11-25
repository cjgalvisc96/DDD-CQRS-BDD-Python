import logging

from src.contexts.shared.domain import Logger


class LoggingLogger(Logger):
    def __init__(self) -> None:
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)
        logger_handler = logging.StreamHandler()
        logger_format = logging.Formatter(
            fmt="%(asctime)s - %(message)s", datefmt="%d-%b-%y %H:%M:%S"
        )
        logger_handler.setFormatter(logger_format)
        self.logger.addHandler(logger_handler)

    def debug(self, *, message: str):
        self.logger.debug(message)

    def error(self, *, message: str):
        self.logger.error(message)

    def info(self, *, message: str):
        self.logger.info(message)

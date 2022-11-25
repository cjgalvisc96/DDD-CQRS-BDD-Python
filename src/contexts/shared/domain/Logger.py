from abc import ABC


class Logger(ABC):
    def debug(self, *, message: str):
        ...

    def error(self, *, message: str):
        ...

    def info(self, *, message: str):
        ...

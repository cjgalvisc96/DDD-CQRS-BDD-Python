from abc import ABC, abstractmethod


class Logger(ABC):
    @abstractmethod
    def debug(self, *, message: str):
        ...

    @abstractmethod
    def error(self, *, message: str):
        ...

    @abstractmethod
    def info(self, *, message: str):
        ...

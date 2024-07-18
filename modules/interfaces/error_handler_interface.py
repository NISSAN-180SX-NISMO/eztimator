from abc import ABC, abstractmethod
from enum import Enum, auto


class LEVEL(Enum):
    WARNING = auto()
    ERROR = auto()


class ErrorHandlerInterface(ABC):
    @abstractmethod
    def handle(self, lvl: LEVEL, info: str) -> None:
        pass

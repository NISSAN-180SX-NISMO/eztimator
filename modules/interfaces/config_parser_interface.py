from abc import ABC, abstractmethod
from typing import Dict


class ConfigParserInterface(ABC):
    @abstractmethod
    def parse(self) -> Dict:
        pass

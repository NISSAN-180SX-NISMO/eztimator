from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Dict

from modules.aliases.aliases import CppStruct


class BytesParserInterface(ABC):
    @abstractmethod
    def parse(self, bytes_str: str) -> CppStruct:
        pass

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Dict


@dataclass
class CppStruct:
    struct: Dict[str, ...]


class BytesParserInterface(ABC):
    @abstractmethod
    def parse(self, bytes_str: str) -> CppStruct:
        pass

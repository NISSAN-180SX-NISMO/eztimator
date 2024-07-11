from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Iterable, List, Optional, Tuple


class SourceDataIterableParserInterface(ABC):
    @abstractmethod
    def iterable_line(self, file_path: str) \
            -> Iterable[Tuple[Optional[str], List[str]]]:
        pass

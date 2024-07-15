from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Iterable, List, Optional, Tuple

from settings import Settings


class SourceDataIterableParserInterface(ABC):
    @abstractmethod
    def iterable_line(self, cfg: Settings.data_source) \
            -> Iterable[Tuple[Optional[str], List[str]]]:
        pass

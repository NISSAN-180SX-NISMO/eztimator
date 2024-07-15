from __future__ import annotations

from typing import Iterable, List, Optional, Tuple

from modules.interfaces.source_data_iterable_parser_interface import SourceDataIterableParserInterface
from settings import Settings


class SourceDataIterableParser(SourceDataIterableParserInterface):
    def iterable_line(self, cfg: Settings.SourceData) \
            -> Iterable[Tuple[Optional[str], List[str]]]:
        with open(cfg.file_path, 'r', newline=cfg.line_delimiter) as file:
            for line in file:
                line = line.strip()
                if line:
                    values = [v.strip() for v in line.split(cfg.value_delimiter)]
                    if len(values) > 0:
                        key = values.pop(0)
                        yield key, values
                    else:
                        raise ValueError('Empty line')
                else:
                    yield None, []

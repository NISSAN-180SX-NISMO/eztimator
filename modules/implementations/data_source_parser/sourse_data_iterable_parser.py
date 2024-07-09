from __future__ import annotations

from typing import Iterable, List, Optional, Tuple

from modules.interfaces.data_source_parser_interface import DataSourceParserInterface


class SourceDataIterableParser(DataSourceParserInterface):
    def __init__(self, value_delimiter: str = ',', line_delimiter: str = '\n'):
        self._value_delimiter = value_delimiter
        self._line_delimiter = line_delimiter

    def iterable_line(self, file_path: str) \
            -> Iterable[Tuple[Optional[str], List[str]]]:
        with open(file_path, 'r', newline=self._line_delimiter) as file:
            for line in file:
                line = line.strip()
                if line:
                    values = [v.strip() for v in line.split(self._value_delimiter)]
                    if len(values) > 0:
                        key = values.pop(0)
                        yield key, values
                    else:
                        raise ValueError('Empty line')
                else:
                    yield None, []

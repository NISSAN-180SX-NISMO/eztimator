from __future__ import annotations

from typing import Dict, List, Tuple, Generator, Iterator
from DataSourceHandlers.AbstractDataSourceHandler import AbstractDataSourceHandler
from zparser_lib_cpp.TempParser import TempParser


class FileDataSourceHandler(AbstractDataSourceHandler):
    _file_path: str
    _value_delimiter: str
    _line_delimiter: str  # now only None, '', '\n', '\r' и '\r\n'

    def get_split_line_iterator(self) -> Iterator[Tuple[str, List[str]]]:
        with open(self._file_path, 'r', newline=self._line_delimiter) as file:
            line: str = file.readline().strip()
            while line:
                values: List[str] = line.split(self._value_delimiter)
                if len(values) > 1:  # хз че с ключом без значения делать
                    key = values.pop(0).strip()  # Оставшиеся элементы как значения
                    yield key, values
                line: str = file.readline().strip()

    def __init__(self, file_path: str, _value_delimiter: str, _line_delimiter: str):
        super().__init__()
        self._file_path = file_path
        self._value_delimiter = _value_delimiter
        self._line_delimiter = _line_delimiter
        self._cpp_parser = TempParser()

    def get_info(self, key: str) -> Dict[str, str] | None:
        return self._source_data.get(key)

    def read_source_data(self):
        split_line_iter = self.get_split_line_iterator()
        for key, values in split_line_iter:
            self._source_data[key] = values

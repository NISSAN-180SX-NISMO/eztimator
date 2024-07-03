from typing import Dict
from DataSourceHandlers.DataSourceHandlerInterface import DataSourceHandlerInterface
from zparser_lib_cpp.TempParser import TempParser


class FileDataSourceHandler(DataSourceHandlerInterface):
    _file_path: str
    _value_delimiter: str
    _line_delimiter: str  # now only None, '', '\n', '\r', и '\r\n'

    _cpp_parser: TempParser

    # test
    _map: Dict[str, Dict[str, Dict[str, bool]]]

    # test

    def _do_parse_file(self):
        with open(self._file_path, 'r', newline=self._line_delimiter) as file:
            line: str = file.readline().strip()
            while line:
                values = line.split(self._value_delimiter)
                if len(values) > 1:  # хз че с ключом без значения делать
                    key = values.pop(0).strip()  # Оставшиеся элементы как значения
                    # TODO: Вызов парсера со стороны плюсов \.
                    structs: Dict[str, Dict[str, bool]] = dict()
                    for value in values:
                        struct_key, struct = self._cpp_parser.parse_bytes(value)
                        structs[struct_key] = struct
                    self._cpp_parser.reset_counter()
                    self._map[key] = structs
                    # TODO: Вызов парсера со стороны плюсов /.
                line: str = file.readline().strip()

    def __init__(self, file_path: str, _value_delimiter: str, _line_delimiter: str):
        self._file_path = file_path
        self._value_delimiter = _value_delimiter
        self._line_delimiter = _line_delimiter

        self._map = dict()
        self._cpp_parser = TempParser()

    def get_info(self) -> Dict[str, Dict[str, Dict[str, bool]]]:
        self._do_parse_file()
        return self._map
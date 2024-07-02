from abc import ABCMeta, abstractmethod
from typing import Dict, List
from collections import defaultdict



class DataSourceHandlerInterface(metaclass=ABCMeta):
    @abstractmethod
    def get_info(self) -> Dict[str, Dict[str, str]]:
        pass


# Класс который получает данные из файла
class FileDataSourceHandler(DataSourceHandlerInterface):
    _file_path: str
    _value_delimiter: str
    _line_delimiter: str

    _cpp_parser: ...

    # test
    _map: Dict[str, List[str]]
    # test

    def _get_line(self) -> str:
        with open(self._file_path, 'r') as file:
            buffer = ''
            while True:
                char = file.read(1)  # Чтение одного символа
                if not char:  # Конец файла
                    if buffer:
                        yield buffer  # Возвращаем оставшийся буфер, если он не пуст
                    break
                if char == self._line_delimiter:
                    yield buffer
                    buffer = ''
                else:
                    buffer += char

    def _parse_line(self, line: str) -> str:
        buffer = ''
        for char in line:
            if char == self._value_delimiter:
                yield buffer
                buffer = ''
            else:
                buffer += char

        # Вернуть оставшийся буфер, если он не пуст
        if buffer:
            yield buffer

    def _do_parse_file(self):
        key: str
        values: List[str] = []
        is_key = True

        line_generator = self._get_line();
        for line in line_generator:
            value_generator = self._parse_line(line)
            for value in value_generator:
                if is_key:
                    key = value
                    is_key = False;
                else:
                    values.append(value)
            self._map[key] = values.copy();
            is_key = True
            values.clear()


    def __init__(self, file_path: str, _value_delimiter: str, _line_delimiter: str):
        self._file_path = file_path
        self._value_delimiter = _value_delimiter
        self._line_delimiter = _line_delimiter

        self._map = {}

    def get_info(self) -> Dict[str, Dict[str, str]]:
        self._do_parse_file()
        print(self._map)
        return ...


# Класс который получает данные из бд
class DataBaseDataSourceHandler(DataSourceHandlerInterface):
    _server: str
    _username: str
    _password: str

    def _some_private_method(self) -> int:
        return 0

    def __init__(self, server: str, username: str, password: str):
        self._server = server
        self._username = username
        self._password = password

    def get_info(self) -> Dict[str, Dict[str, str]]:
        # TODO
        return ...


# Класс который получает данные по http
class HttpDataSourceHandler(DataSourceHandlerInterface):
    _url_list: List[str]
    _request: ...

    def _some_private_method(self) -> int:
        return 0

    def __init__(self, url_list: List[str], request: ...):
        self._url_list = url_list
        self._request = request

    def get_info(self) -> Dict[str, Dict[str, str]]:
        # TODO
        return ...

def main() -> int:
    data_source_handler: DataSourceHandlerInterface = FileDataSourceHandler('test_data_source.txt', ',', '\n')
    data_source_handler.get_info()
    return 0


if __name__ == '__main__':
    main()

import pprint
from abc import ABCMeta, abstractmethod
from typing import Dict, List


class TempParser:
    counter = 0

    def __init__(self):
        pass

    def parse_bytes(self, bytes_str: str) -> (str, Dict[str, bool]): # Я хз пока че он возвращать буедт ес честно
        # Разбиваем строку на пары символов (байты)
        byte_pairs = [bytes_str[i:i + 2] for i in range(0, len(bytes_str), 2)]

        # Создаем словарь, где ключи - индексы байтов, значения - True/False в зависимости от четности байта
        result = {f'field_{i}'.strip(): int(byte, 16) % 2 == 0 for i, byte in enumerate(byte_pairs)}
        self.counter += 1
        return f'struct_{self.counter}'.strip(), result

    def reset_counter(self):
        self.counter = 0


class DataSourceHandlerInterface(metaclass=ABCMeta):
    @abstractmethod
    def get_info(self) -> Dict[str, Dict[str, str]]:
        pass


# Класс который получает данные из файла
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
            line: str = file.readline().strip();
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

    def get_info(self) -> Dict[str, Dict[str, str]]:
        self._do_parse_file()
        pp = pprint.PrettyPrinter(indent=4)
        pp.pprint(self._map)
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
    data_source_handler: DataSourceHandlerInterface = FileDataSourceHandler('test_data_source.txt', ',', '\r\n')
    data_source_handler.get_info()
    return 0


if __name__ == '__main__':
    main()

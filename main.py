from abc import ABCMeta, abstractmethod
from typing import Dict, List


class DataSourceHandlerInterface(metaclass=ABCMeta):
    @abstractmethod
    def get_info(self) -> Dict[str, Dict[str, str]]:
        pass


# Класс который получает данные из файла
class FileDataSourceHandler(DataSourceHandlerInterface):
    _file_path: str
    _delimiter: str
    _extension_mask: str

    def _some_private_method(self) -> int:
        return 0

    def __init__(self, file_path: str, delimiter: str, extension_mask: str = ".*"):
        self._file_path = file_path
        self._delimiter = delimiter
        self._extension_mask = extension_mask

    def get_info(self) -> Dict[str, Dict[str, str]]:
        # TODO
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
    data_source_handler: DataSourceHandlerInterface = FileDataSourceHandler('', '', '')
    return 0


if __name__ == '__main__':
    main()

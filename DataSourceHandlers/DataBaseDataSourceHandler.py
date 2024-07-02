from typing import Dict
from DataSourceHandlers.DataSourceHandlerInterface import DataSourceHandlerInterface


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
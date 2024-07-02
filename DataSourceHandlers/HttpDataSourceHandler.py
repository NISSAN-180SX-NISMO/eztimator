from typing import List, Dict
from DataSourceHandlers.DataSourceHandlerInterface import DataSourceHandlerInterface


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
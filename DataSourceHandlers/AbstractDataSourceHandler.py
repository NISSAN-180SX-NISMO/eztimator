from abc import ABCMeta, abstractmethod
from typing import Dict, List


class AbstractDataSourceHandler(metaclass=ABCMeta):
    def __init__(self):
        self._source_data = dict()

    @abstractmethod
    def get_info(self, key: str) -> Dict[str, List[str]]:
        pass

    @abstractmethod
    def read_source_data(self):
        pass

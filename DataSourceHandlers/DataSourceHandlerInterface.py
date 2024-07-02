from abc import ABCMeta, abstractmethod
from typing import Dict


class DataSourceHandlerInterface(metaclass=ABCMeta):
    @abstractmethod
    def get_info(self) -> Dict[str, Dict[str, Dict[str, bool]]]:
        pass

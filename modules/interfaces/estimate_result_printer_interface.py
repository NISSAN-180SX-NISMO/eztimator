import io
from abc import ABC, abstractmethod

from modules.interfaces.estimator_interface import EstimateUniqueFieldsResult
from settings import Settings


class EstimateResultPrinterInterface(ABC):
    @staticmethod
    @abstractmethod
    def _print(result: EstimateUniqueFieldsResult, cfg: Settings.Estimate, stream: io.TextIOBase):
        pass

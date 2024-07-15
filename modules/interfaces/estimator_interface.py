from dataclasses import dataclass
from abc import ABC, abstractmethod
from typing import Dict
from modules.dtos.estimated_collection import EstimatedCollection


@dataclass
class EstimateResult:
    field: str
    value: str
    percent: float


@dataclass
class EstimateResults:
    results_map: Dict[str, EstimateResult]


class EstimatorInterface(ABC):
    @abstractmethod
    def estimate(self, collection: EstimatedCollection) -> EstimateResult:
        pass

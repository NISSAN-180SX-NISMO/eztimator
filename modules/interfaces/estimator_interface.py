from dataclasses import dataclass, field
from abc import ABC, abstractmethod


@dataclass
class EstimateResult:
    field: str
    value: str
    percent: float


class EstimatorInterface(ABS):
    @abstractmethod
    def estimate(self, structs: List[CppStruct]) -> List[EstimateResult]:
        pass

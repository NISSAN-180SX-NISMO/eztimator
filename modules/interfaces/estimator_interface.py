from dataclasses import dataclass, field
from abc import ABC, abstractmethod
from typing import Dict, List, Set, Tuple

from modules.aliases.aliases import FieldName, SourceKey, FieldValue, ValueFreq
from modules.dtos.estimated_collection import EstimatedCollection


@dataclass
class EstimateUniqueFieldValuesResult:
    freq: ValueFreq
    included_source_keys: Set[SourceKey]


@dataclass
class EstimateUniqueFieldResult:
    percentage_of_values: Dict[FieldValue, EstimateUniqueFieldValuesResult] = field(default_factory=dict)


@dataclass
class EstimateUniqueFieldsResult:
    unique_fields: Dict[FieldName, EstimateUniqueFieldResult] = field(default_factory=dict)


class EstimatorInterface(ABC):
    @abstractmethod
    def estimate(self, collection: EstimatedCollection) -> EstimateUniqueFieldsResult:
        pass

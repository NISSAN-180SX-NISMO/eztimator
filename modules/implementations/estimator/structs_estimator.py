from collections import Counter
from typing import List, Dict, Any

from modules.aliases.aliases import FieldName
from modules.dtos.estimated_collection import EstimatedCollection
from modules.interfaces.estimator_interface import EstimateUniqueFieldResult, EstimateUniqueFieldsResult, \
    EstimatorInterface, EstimateUniqueFieldValuesResult


def convert_to_tuple(data: Any) -> Any:
    if isinstance(data, list):
        return tuple(data)
    elif isinstance(data, dict):
        return tuple(data.items())
    else:
        return data


def make_hashable(data):
    if isinstance(data, dict):
        # Преобразуем словарь в список пар ключ-значение
        return tuple((key, make_hashable(value)) for key, value in data.items())
    elif isinstance(data, list):
        # Преобразуем список в кортеж
        return tuple(make_hashable(element) for element in data)
    else:
        return data


class StructsEstimator(EstimatorInterface):

    def estimate(self, collection: EstimatedCollection) -> EstimateUniqueFieldsResult:
        result: EstimateUniqueFieldsResult = EstimateUniqueFieldsResult()
        for source_key, cpp_struct in collection.all_structs():
            for key in cpp_struct.keys():
                if key not in result.unique_fields:
                    result.unique_fields[key] = EstimateUniqueFieldResult()

        for key in result.unique_fields.keys():
            for source_key, cpp_struct in collection.all_structs(False):
                if key in cpp_struct:
                    value = make_hashable(cpp_struct[key])
                    if value not in result.unique_fields[key].percentage_of_values:
                        result.unique_fields[key].percentage_of_values[value] = (
                            EstimateUniqueFieldValuesResult(freq=1, included_source_keys={source_key})
                        )
                    else:
                        result.unique_fields[key].percentage_of_values[value].freq += 1
                        result.unique_fields[key].percentage_of_values[value].included_source_keys.add(source_key)

        for key, estimate_unique_field_result in result.unique_fields.items():
            total_values = sum(
                value_result.freq for value_result in estimate_unique_field_result.percentage_of_values.values())
            for estimate_unique_field_values_result in estimate_unique_field_result.percentage_of_values.values():
                estimate_unique_field_values_result.freq = estimate_unique_field_values_result.freq / total_values * 100

        return result

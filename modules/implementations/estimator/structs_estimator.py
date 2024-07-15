from collections import Counter
from typing import List, Dict

from modules.dtos.estimated_collection import EstimatedCollection
from modules.interfaces.estimator_interface import EstimateResult, EstimatorInterface, EstimateResults


class StructsEstimator(EstimatorInterface):
    def estimate(self, collection: EstimatedCollection) -> EstimateResults:
        unique_fields = {}
        for cpp_struct in collection.all_structs():
            for key in cpp_struct.struct.keys():
                if key not in unique_fields:
                    unique_fields[key] = {}
        # print(unique_keys)
        for key in unique_fields.keys():
            for cpp_struct in collection.all_structs():
                if key in cpp_struct.struct:
                    value = cpp_struct.struct[key]
                    if value not in unique_fields[key]:
                        unique_fields[key][value] = 1
                    else:
                        unique_fields[key][value] += 1
        # print(unique_keys)
        results_map = dict()
        for key, values_dict in unique_fields.items():
            total_values = sum(values_dict.values())
            percentage_of_values = {value: (count / total_values) * 100 for value, count in values_dict.items()}
            results_map[key] = (EstimateResult(field=key, percentage_of_values=percentage_of_values))

        return EstimateResults(results_map=results_map)

from collections import Counter
from typing import List, Dict

from modules.dtos.estimated_collection import EstimatedCollection
from modules.interfaces.estimator_interface import EstimateResult, EstimatorInterface


class StructsEstimator(EstimatorInterface):
    def estimate(self, collection: EstimatedCollection) -> List[EstimateResult]:
        # 1. Список уникальных ключей
        unique_keys = set(struct.key for struct in collection.all_structs())

        results: List[EstimateResult] = []

        # 2. Идем по списку уникальных ключей
        for key in unique_keys:
            # Собираем все значения для данного ключа
            values = [struct[key] for struct in collection.all_structs() if key in struct]

            # 3. Сортируем список значений
            values.sort()

            # 4. Находим максимальную длину повторяющегося значения
            counter = Counter(values)
            max_count_value = max(counter.items(), key=lambda x: x[1])

            # 5. Вычисляем процент
            percent = max_count_value[1] / len(values) * 100

            # 6. Добавляем поле, его значение и процент в EstimateResult
            result = EstimateResult(field=key, value=max_count_value[0], percent=percent)
            results.append(result)

        return results
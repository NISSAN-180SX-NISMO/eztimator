from __future__ import annotations

from typing import Dict, List

from bitarray import bitarray


def compare_fields(source: Dict[str, bool], target: Dict[str, bool]) -> float:
    # Получаем множества ключей для словарей, где значения True
    source_keys = {key for key, value in source.items()}
    target_keys = {key for key, value in target.items()}

    print(source_keys)
    print(target_keys)
    # Вычисляем пересечение и объединение этих множеств
    intersection = source_keys & target_keys
    union = source_keys | target_keys

    print(intersection)
    print(union)

    # Создаем два bitarray для хранения бинарных значений
    source_bitarray = bitarray()
    target_bitarray = bitarray()

    # Проходимся по каждому общему ключу и добавляем значения в bitarray
    for key in intersection:
        source_bitarray.append(source[key])
        target_bitarray.append(target[key])

    # Преобразуем bitarray в целые числа (без лишних битов)
    source_number = int(source_bitarray.to01(), 2)
    target_number = int(target_bitarray.to01(), 2)

    # Выводим результаты
    print(f"Source bitarray: {source_bitarray}")
    print(f"Target bitarray: {target_bitarray}")
    print(f"Source number: {source_number:03b}")  # Форматируем вывод как 3-битное двоичное число
    print(f"Target number: {target_number:03b}")

    res = source_bitarray ^ target_bitarray # WTF

    avg = res.count(True) / len(res)
    print("avg for values: ", avg)

    # Если объединение пусто, коэффициент Жаккара равен 1
    if not union:
        return avg

    # Вычисляем коэффициент Жаккара
    jaccard_index = len(intersection) / len(union)
    print("jaccard index for keys: ", jaccard_index)

    return jaccard_index * avg


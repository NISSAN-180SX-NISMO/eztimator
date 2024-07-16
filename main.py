import asyncio
import random
from typing import List

from core.core_manager import CoreManager
from modules.dtos.response import Response, DataBaseResponse
from modules.implementations.config_parser.JsonConfigParser import JsonConfigParser
from modules.implementations.data_base_gateway.sqlite3_gateway import SQLiteDataBaseAsyncGateway
from modules.implementations.estimator.structs_estimator import StructsEstimator
from modules.implementations.source_data_parser.sourse_data_iterable_parser import SourceDataIterableParser
from modules.interfaces.estimator_interface import EstimateUniqueFieldsResult
from settings import Settings, SETTINGS

# TODO: for test
from modules.interfaces.bytes_parser_interface import BytesParserInterface, CppStruct
from modules.interfaces.data_base_gateway_interface import DataBaseGatewayInterface




class TempDataBaseGateway(DataBaseGatewayInterface):

    async def get_info(self, key: str, cfg: Settings.DataBase) -> Response:
        # Список с 6 случайными строками
        random_strings = ["aboba", "svo", "goida", 'gurenya', "zov", 'amogus']

        # Выбираем случайные 3 строки из списка
        selected_strings = random.sample(random_strings, 3)

        # Создаем словарь, где ключи - выбранные строки, а значения - случайные числа
        result_map = {s: random_strings[random.randint(1, 5)] for s in selected_strings}

        # Возвращаем ответ в виде объекта Response
        return DataBaseResponse(success=True, info=result_map)


class TempBytesParser(BytesParserInterface):

    def parse(self, bytes_str: str) -> CppStruct:
        predefined_elements = ["element1", "element2", "element3", "element4", "element5", "element6"]

        # Randomly select 3-4 elements from the predefined list
        selected_elements = random.sample(predefined_elements, random.randint(3, 4))

        # Create a dictionary with selected elements as keys and random numbers as values
        result_map = {element: random.randint(1, 6) for element in selected_elements}

        # Return the result wrapped in a Response object
        return result_map


def print_results(results: EstimateUniqueFieldsResult) -> None:
    print ("Results: ", results.unique_fields)
    for key, result in results.unique_fields.items():
        print(f"Поле: {key}")
        for value, estimate_unique_field_values_result in result.percentage_of_values.items():
            print(f"  Значение: {value} - {estimate_unique_field_values_result.freq:.2f}%\tЗадетые ключи: {sorted(estimate_unique_field_values_result.included_source_keys)}")


async def main() -> None:
    print("Settings: ", SETTINGS)
    core: CoreManager = CoreManager()
    core.set_data_source_parser(SourceDataIterableParser())
    core.set_data_base_gateway(TempDataBaseGateway())
    core.set_bytes_parser(TempBytesParser())
    core.set_estimator(StructsEstimator())

    result = await core.get_estimate_result()
    print_results(result)


if __name__ == '__main__':
    asyncio.run(main())

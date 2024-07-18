import asyncio
import io
import random

from core.core_manager import CoreManager
from modules.dtos.response import Response, DataBaseResponse
from modules.implementations.cpp_bytes_parser_adapter.bytes_parser_cpp import CppBytesParserAdapter
from modules.implementations.data_base_gateway.sqlite3_gateway import SQLiteDataBaseAsyncGateway
from modules.implementations.error_file_writer.error_file_writer import ErrorFileWriter
from modules.implementations.estimate_result_printer.estimate_result_printer import EstimateResultPrinter
from modules.implementations.estimator.structs_estimator import StructsEstimator
from modules.implementations.source_data_parser.sourse_data_iterable_parser import SourceDataIterableParser
from modules.interfaces.estimator_interface import EstimateUniqueFieldsResult
from settings import Settings, SETTINGS

# TODO: for test
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


def print_results(results: EstimateUniqueFieldsResult) -> None:
    print("Results: ", results.unique_fields)
    for key, result in results.unique_fields.items():
        print(f"Поле: {key}")
        for value, estimate_unique_field_values_result in result.percentage_of_values.items():
            print(
                f"  Значение: {value} - {estimate_unique_field_values_result.freq:.2f}%\tЗадетые ключи: {sorted(estimate_unique_field_values_result.included_source_keys)}")


async def main() -> None:
    # print("Settings: ", SETTINGS)
    core: CoreManager = CoreManager()
    core.set_data_source_parser(SourceDataIterableParser())
    core.set_data_base_gateway(TempDataBaseGateway())
    core.set_bytes_parser(CppBytesParserAdapter())
    core.set_estimator(StructsEstimator())
    core.set_error_handler(ErrorFileWriter(SETTINGS.error_handler))

    result = await core.get_estimate_result()
    stream = io.StringIO()
    EstimateResultPrinter.print(result, SETTINGS.estimate, stream)
    print(stream.getvalue())


if __name__ == '__main__':
    asyncio.run(main())

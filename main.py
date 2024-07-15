import asyncio

from core.core_manager import CoreManager
from modules.dtos.response import Response
from modules.implementations.config_parser.JsonConfigParser import JsonConfigParser
from modules.implementations.data_base_gateway.sqlite3_gateway import SQLiteDataBaseAsyncGateway
from modules.implementations.source_data_parser.sourse_data_iterable_parser import SourceDataIterableParser
from settings import Settings

# TODO: for test
from modules.interfaces.data_base_gateway_interface import DataBaseGatewayInterface
from random import random


class TempDataBaseGateway(DataBaseGatewayInterface):

    async def get_info(self, key: str, cfg: Settings.DataBase) -> Response:
        # Список с 6 случайными строками
        random_strings = ["aboba", "svo", "goida", 'gurenya', "zov", 'amogus']

        # Выбираем случайные 3 строки из списка
        selected_strings = random.sample(random_strings, 3)

        # Создаем словарь, где ключи - выбранные строки, а значения - случайные числа
        result_map = {s: random.randint(1, 100) for s in selected_strings}

        # Возвращаем ответ в виде объекта Response
        return Response(data=result_map)


async def main() -> None:
    settings = Settings.get_instance(JsonConfigParser('config.json'))
    core: CoreManager = CoreManager()
    core.set_data_source_parser(SourceDataIterableParser(settings.SourceData.value_delimiter, settings.SourceData.line_delimiter))
    core.set_data_base_gateway(TempDataBaseGateway(settings.DataBase.path))
    core.set

    print(core.get_estimate_result())


if __name__ == '__main__':
    asyncio.run(main())

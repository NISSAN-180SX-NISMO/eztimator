from core.core_manager import CoreManager
from modules.implementations.config_parser.JsonConfigParser import JsonConfigParser
from modules.implementations.data_base_gateway.sqlite3_gateway import SQLiteDataBaseAsyncGateway
from modules.implementations.source_data_parser.sourse_data_iterable_parser import SourceDataIterableParser
from settings import Settings


def main() -> None:
    settings = Settings(JsonConfigParser('config.json')).get_instance()
    core: CoreManager = CoreManager()
    core.set_data_source_parser(SourceDataIterableParser(settings.SourceData.value_delimiter, settings.SourceData.line_delimiter))
    core.set_data_base_gateway(SQLiteDataBaseAsyncGateway(settings.DataBase.path))
    core.set


if __name__ == '__main__':
    main()

import json
from dataclasses import dataclass, field
from typing import List, Dict, Any

from modules.aliases.aliases import RegexString
from modules.interfaces.config_parser_interface import ConfigParserInterface
from modules.implementations.config_parser.JsonConfigParser import JsonConfigParser

global_config_parser: ConfigParserInterface = JsonConfigParser('config.json')


@dataclass
class Settings:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not isinstance(cls._instance, cls):
            cls._instance = super(Settings, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        self._load_from_config()

    def _load_from_config(self):
        config = global_config_parser.parse()
        # Создаем экземпляры TargetKey с объектами RegexString:
        target_keys = []
        for key_data in config['estimate']['target_keys']:
            regex_string = RegexString(key_data['value'])
            target_key = self.TargetKey(key=key_data['key'], value=regex_string)
            target_keys.append(target_key)

        # Теперь создаем экземпляр Estimate, используя созданные объекты TargetKey:
        self.estimate = self.Estimate(
            target_keys=target_keys,
            matches_percent=config['estimate']['matches_percent'],
            result_printer=Settings.ResultPrinter(**config['estimate']['result_printer'])
        )
        self.data_base = self.DataBase(
            path=config['data_base']['path'],
            username=config['data_base']['username'],
            password=config['data_base']['password'],
            table=config['data_base']['table']
        )
        self.http = self.Http(
            targets=config['http']['targets']
        )
        self.source_data = self.SourceData(
            path=config['source_data']['path'],
            line_delimiter=config['source_data']['line_delimiter'],
            value_delimiter=config['source_data']['value_delimiter']
        )
        self.error_handler = self.ErrorHandler(
            path=config['error_handler']['path'],
            save_timestamp=config['error_handler']['save_timestamp']
        )

    @dataclass
    class TargetKey:
        key: str
        value: RegexString

    @dataclass
    class ResultPrinter:
        path: str
        only_filtered_view: bool

    @dataclass
    class Estimate:
        target_keys: List['Settings.TargetKey']
        matches_percent: float
        result_printer: 'Settings.ResultPrinter'

    @dataclass
    class DataBase:
        path: str
        username: str
        password: str
        table: str

    @dataclass
    class Http:
        targets: List[Any]

    @dataclass
    class SourceData:
        path: str
        line_delimiter: str
        value_delimiter: str

    @dataclass
    class ErrorHandler:
        path: str
        save_timestamp: bool

    estimate: Estimate
    data_base: DataBase
    http: Http
    source_data: SourceData
    error_handler: ErrorHandler


SETTINGS = Settings()

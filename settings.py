import json
from dataclasses import dataclass
from typing import List, ClassVar
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
        self.estimate = self.Estimate(
            target_key=config['estimate']['target_key'],
            matches_percent=config['estimate']['matches_percent']
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
            file_path=config['data_source']['path'],
            line_delimiter=config['data_source']['line_delimiter'],
            value_delimiter=config['data_source']['value_delimiter']
        )

    @dataclass
    class Estimate:
        # target_keys: List[str]
        target_key: str
        matches_percent: float

    @dataclass
    class DataBase:
        path: str
        username: str
        password: str
        table: str

    @dataclass
    class Http:
        targets: List[str]

    @dataclass
    class SourceData:
        file_path: str
        line_delimiter: str
        value_delimiter: str

    estimate: Estimate
    data_base: DataBase
    http: Http
    source_data: SourceData


SETTINGS = Settings()

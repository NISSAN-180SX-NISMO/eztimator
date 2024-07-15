import json
from dataclasses import dataclass
from typing import List, ClassVar

from modules.implementations.config_parser.JsonConfigParser import JsonConfigParser
from modules.interfaces.config_parser_interface import ConfigParserInterface


@dataclass
class Settings:
    _instance: ClassVar['Settings'] = None
    _initialized: ClassVar[bool] = False
    _config_parser = None

    @staticmethod
    def get_instance() -> 'Settings':
        if Settings._instance is None:
            Settings._config_parser = JsonConfigParser('config.json')
            Settings._instance = Settings._load_from_config()
            Settings._initialized = True
        return Settings._instance

    def _load_from_config(self, ) -> 'Settings':
        config = self._config_parser.parse()
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
        self.data_source = self.SourceData(
            path=config['data_source']['path'],
            line_delimiter=config['data_source']['line_delimiter'],
            value_delimiter=config['data_source']['value_delimiter']
        )

    @dataclass
    class Estimate:
        # target_keys: List[str]
        target_key: str
        matches_percent: int

    @dataclass
    class DataBase:
        path: str
        username: int
        password: int
        table: str

    @dataclass
    class Http:
        targets: List[str]

    @dataclass
    class SourceData:
        path: str
        line_delimiter: int
        value_delimiter: int

    estimate: Estimate
    data_base: DataBase
    http: Http
    data_source: SourceData

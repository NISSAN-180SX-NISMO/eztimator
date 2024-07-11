import json
from dataclasses import dataclass
from typing import List, ClassVar

from modules.interfaces.config_parser_interface import ConfigParserInterface


@dataclass
class Settings:
    _instance: ClassVar['Settings'] = None
    _config_parser: ConfigParserInterface

    def __init__(self, config_parser: ConfigParserInterface):
        self._config_parser = config_parser

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls._load_from_config(cls._config_parser)
        return cls._instance

    @classmethod
    def _load_from_config(cls, config_parser: ConfigParserInterface) -> 'Settings':
        config = config_parser.parse()
        estimate = cls.Estimate(
            target_keys=config['estimate']['target_keys'],
            matches_percent=config['estimate']['matches_percent']
        )
        data_base = cls.DataBase(
            path=config['data_base']['path'],
            username=config['data_base']['username'],
            password=config['data_base']['password']
        )
        http = cls.Http(
            targets=config['http']['targets']
        )
        data_source = cls.SourceData(
            path=config['data_source']['path'],
            line_delimiter=config['data_source']['line_delimiter'],
            value_delimiter=config['data_source']['value_delimiter']
        )
        return cls(config_parser, estimate, data_base, http, data_source)

    @dataclass
    class Estimate:
        target_keys: List[str]
        matches_percent: int

    @dataclass
    class DataBase:
        path: str
        username: int
        password: int

    @dataclass
    class Http:
        targets: List[str]

    @dataclass
    class SourceData:
        path: str
        line_delimiter: int
        value_delimiter: int

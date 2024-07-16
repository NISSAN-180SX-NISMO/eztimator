import json
from typing import Dict

from modules.interfaces.config_parser_interface import ConfigParserInterface


class JsonConfigParser(ConfigParserInterface):

    def __init__(self, file_path: str):
        self.file_path = file_path

    def parse(self) -> Dict:
        with open(self.file_path, 'r') as file:
            return json.load(file)

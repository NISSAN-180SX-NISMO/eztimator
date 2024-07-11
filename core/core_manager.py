# TODO: Сделать менеджер, который будет в себя всасывать интерфесы модулей всех и работать с ними, чтобы легко можно было инжектить в разные имплементации модулей \
# таких как парсер файла, парсер конфига, и самое главное - оценщик
from dataclasses import dataclass
from typing import Dict

from modules.interfaces.bytes_parser_interface import BytesParserInterface
from modules.interfaces.config_parser_interface import ConfigParserInterface
from modules.interfaces.data_base_gateway_interface import DataBaseGatewayInterface
from modules.interfaces.source_data_iterable_parser_interface import SourceDataIterableParserInterface
from modules.interfaces.estimator_interface import EstimatorInterface
from modules.interfaces.http_service_interface import HttpServiceInterface


@dataclass
class EstimateResult:
    results: Dict[str: str]  # FIXME: Некоторые красившевства


class CoreManager:
    def __init__(self):
        self.bytes_parser: BytesParserInterface = BytesParserInterface()
        self.config_parser: ConfigParserInterface = ConfigParserInterface()
        self.data_base_gateway: DataBaseGatewayInterface = DataBaseGatewayInterface()
        self.source_data_parser: SourceDataIterableParserInterface = SourceDataIterableParserInterface()
        self.estimator: EstimatorInterface = EstimatorInterface()
        self.http_service: HttpServiceInterface = HttpServiceInterface()

    def get_estimate_result(self) -> EstimateResult:
        pass

    def set_bytes_parser(self, parser: BytesParserInterface):
        self.bytes_parser = parser

    def reset_bytes_parser(self):
        self.bytes_parser = BytesParserInterface()

    def set_config_parser(self, parser: ConfigParserInterface):
        self.config_parser = parser

    def reset_config_parser(self):
        self.config_parser = ConfigParserInterface()

    def set_data_base_gateway(self, gateway: DataBaseGatewayInterface):
        self.data_base_gateway = gateway

    def reset_data_base_gateway(self):
        self.data_base_gateway = DataBaseGatewayInterface()

    def set_data_source_parser(self, parser: SourceDataIterableParserInterface):
        self.source_data_parser = parser

    def reset_data_source_parser(self):
        self.source_data_parser = SourceDataIterableParserInterface()

    def set_estimator(self, estimator: EstimatorInterface):
        self.estimator = estimator

    def reset_estimator(self):
        self.estimator = EstimatorInterface()

    def set_http_service(self, service: HttpServiceInterface):
        self.http_service = service

    def reset_http_service(self):
        self.http_service = HttpServiceInterface()
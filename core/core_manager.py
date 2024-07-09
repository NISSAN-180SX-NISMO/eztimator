# TODO: Сделать менеджер, который будет в себя всасывать интерфесы модулей всех и работать с ними, чтобы легко можно было инжектить в разные имплементации модулей \
# таких как парсер файла, парсер конфига, и самое главное - оценщик
from dataclasses import dataclass
from typing import Dict

from modules.interfaces.bytes_parser_interface import BytesParserInterface
from modules.interfaces.config_parser_interface import ConfigParserInterface
from modules.interfaces.data_base_gateway_interface import DataBaseGatewayInterface
from modules.interfaces.data_source_parser_interface import DataSourceParserInterface
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
        self.data_source_parser: DataSourceParserInterface = DataSourceParserInterface()
        self.estimator: EstimatorInterface = EstimatorInterface()
        self.http_service: HttpServiceInterface = HttpServiceInterface()

    def get_estimate_result(self) -> EstimateResult:
        pass

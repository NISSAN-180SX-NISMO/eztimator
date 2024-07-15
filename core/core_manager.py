# TODO: Сделать менеджер, который будет в себя всасывать интерфесы модулей всех и работать с ними, чтобы легко можно было инжектить в разные имплементации модулей \
# таких как парсер файла, парсер конфига, и самое главное - оценщик
from modules.dtos.estimated_collection import EstimatedCollection
from modules.dtos.response import DataBaseResponse, HttpResponse
from modules.interfaces.bytes_parser_interface import BytesParserInterface
from modules.interfaces.config_parser_interface import ConfigParserInterface
from modules.interfaces.data_base_gateway_interface import DataBaseGatewayInterface
from modules.interfaces.source_data_iterable_parser_interface import SourceDataIterableParserInterface
from modules.interfaces.estimator_interface import EstimatorInterface, EstimateResult, EstimateResults
from modules.interfaces.http_gateway_interface import HttpGatewayInterface
from settings import Settings, SETTINGS


class CoreManager:
    def __init__(self):
        self._bytes_parser: BytesParserInterface = None
        self._config_parser: ConfigParserInterface = None
        self._data_base_gateway: DataBaseGatewayInterface = None
        self._source_data_parser: SourceDataIterableParserInterface = None
        self._estimator: EstimatorInterface = None
        self._http_gateway: HttpGatewayInterface = None

        self._estimated_collection: EstimatedCollection = EstimatedCollection()

    async def _fill_estimated_collection(self) -> None:
        # Step 1. Parse txt file:
        for key, values in self._source_data_parser.iterable_line(SETTINGS.source_data):
            # Step 2. Request to DB or HTTP:
            response: DataBaseResponse = await self._data_base_gateway.get_info(key, SETTINGS.data_base)
            if not response.success:
                response: HttpResponse = await self._http_gateway.get_info(key, SETTINGS.http)
                if not response.success:
                    continue  # TODO: HANDLE ERROR (write to file)
            # Step 3. Search for target:я
            if not response.info.get(SETTINGS.estimate.target_key):
                continue  # TODO: HANDLE ERROR (write to file)
            # Step 4: Parse bytes and add to estimate:
            self._estimated_collection.add(key, [self._bytes_parser.parse(bytes_value) for bytes_value in values])

    async def get_estimate_result(self) -> EstimateResults:
        await self._fill_estimated_collection()
        return self._estimator.estimate(self._estimated_collection)

    def set_bytes_parser(self, parser: BytesParserInterface):
        self._bytes_parser = parser

    def reset_bytes_parser(self):
        self._bytes_parser = BytesParserInterface()

    def set_config_parser(self, parser: ConfigParserInterface):
        self._config_parser = parser

    def reset_config_parser(self):
        self._config_parser = ConfigParserInterface()

    def set_data_base_gateway(self, gateway: DataBaseGatewayInterface):
        self._data_base_gateway = gateway

    def reset_data_base_gateway(self):
        self._data_base_gateway = DataBaseGatewayInterface()

    def set_data_source_parser(self, parser: SourceDataIterableParserInterface):
        self._source_data_parser = parser

    def reset_data_source_parser(self):
        self._source_data_parser = SourceDataIterableParserInterface()

    def set_estimator(self, estimator: EstimatorInterface):
        self._estimator = estimator

    def reset_estimator(self):
        self._estimator = EstimatorInterface()

    def set_http_gateway(self, service: HttpGatewayInterface):
        self._http_gateway = service

    def reset_http_gateway(self):
        self._http_gateway = HttpGatewayInterface()

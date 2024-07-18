from __future__ import annotations
from modules.aliases.aliases import SourceKey, InfoStruct
from modules.dtos.estimated_collection import EstimatedCollection
from modules.dtos.response import DataBaseResponse, HttpResponse, Response
from modules.interfaces.bytes_parser_interface import BytesParserInterface
from modules.interfaces.config_parser_interface import ConfigParserInterface
from modules.interfaces.data_base_gateway_interface import DataBaseGatewayInterface
from modules.interfaces.error_handler_interface import ErrorHandlerInterface, LEVEL
from modules.interfaces.source_data_iterable_parser_interface import SourceDataIterableParserInterface
from modules.interfaces.estimator_interface import EstimatorInterface, EstimateUniqueFieldsResult
from modules.interfaces.http_gateway_interface import HttpGatewayInterface
from settings import SETTINGS


class CoreManager:
    def __init__(self):
        self._bytes_parser: BytesParserInterface = None
        self._config_parser: ConfigParserInterface = None
        self._data_base_gateway: DataBaseGatewayInterface = None
        self._source_data_parser: SourceDataIterableParserInterface = None
        self._estimator: EstimatorInterface = None
        self._http_gateway: HttpGatewayInterface = None
        self._error_handler: ErrorHandlerInterface = None

        self._estimated_collection: EstimatedCollection = EstimatedCollection()

    async def _request_info(self, source_key: SourceKey) -> Response:
        response: DataBaseResponse = await self._data_base_gateway.get_info(source_key, SETTINGS.data_base)

        if not response.success:
            self._error_handler.handle(LEVEL.WARNING,  # info:
                                       f'error get info from data base for source key = \'{source_key}\'. ' +
                                       f'data base config: {SETTINGS.data_base}')

            response: HttpResponse = await self._http_gateway.get_info(source_key, SETTINGS.http)

            if not response.success:
                self._error_handler.handle(LEVEL.WARNING,  # info:
                                           f'error get info from http for source key = \'{source_key}\'. ' +
                                           f'http config: {SETTINGS.http}')

        return response

    def _check_target_keys(self, info: InfoStruct, source_key: SourceKey) -> bool:
        for target_key in SETTINGS.estimate.target_keys:
            if info.get(target_key.key):
                if not target_key.value.match(info[target_key.key]):
                    return False
            else:
                self._error_handler.handle(LEVEL.ERROR,  # info:
                                           f'target key {target_key} not found for source key = \'{source_key}\'. ')
                return False
        return True

    async def _fill_estimated_collection(self) -> None:
        # Step 1. Parse txt file:
        for source_key, values in self._source_data_parser.iterable_line(SETTINGS.source_data):
            # Step 2. Request to DB or HTTP:
            response: Response = await self._request_info(source_key)
            if not response.success:
                continue
            # Step 3. Check target keys:
            if not self._check_target_keys(response.info, source_key):
                continue
            # Step 4: Parse bytes and add to estimate:
            self._estimated_collection.add(source_key, [self._bytes_parser.parse(bytes_str) for bytes_str in values])

    async def get_estimate_result(self) -> EstimateUniqueFieldsResult:
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

    def set_http_gateway(self, gateway: HttpGatewayInterface):
        self._http_gateway = gateway

    def reset_http_gateway(self):
        self._http_gateway = HttpGatewayInterface()

    def set_error_handler(self, error_handler: ErrorHandlerInterface):
        self._error_handler = error_handler

    def reset_error_handler(self):
        self._error_handler = ErrorHandlerInterface()

from DataSourceHandlers.AbstractDataSourceHandler import AbstractDataSourceHandler


class ZoydaSimilarityEstimator:
    _data_source_handler: AbstractDataSourceHandler
    _cpp_parser: ...

    def __init__(self, data_source_handler: AbstractDataSourceHandler, _cpp_parser: ... = None):
        self._data_source_handler = data_source_handler
        self._cpp_parser = _cpp_parser

    def run(self) -> int:
        if self._data_source_handler is None:
            return -1

        # todo check parser



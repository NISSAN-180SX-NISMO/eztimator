from modules.interfaces.bytes_parser_interface import CppStruct, BytesParserInterface
import zparser


class BytesParserCpp(BytesParserInterface):
    def __init__(self):
        self._parser = zparser.zparser

    def parse_bytes(self, bytes_str: str) -> CppStruct:
        return CppStruct(struct=self._parser.parse(bytes_str))

from modules.interfaces.bytes_parser_interface import CppStruct, BytesParserInterface
import zparser


class BytesParserCpp(BytesParserInterface):

    def parse_bytes(self, bytes_str: str) -> CppStruct:
        zparser.parse(bytes_str)


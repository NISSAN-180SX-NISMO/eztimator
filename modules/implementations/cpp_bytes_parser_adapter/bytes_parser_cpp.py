import json
from modules.interfaces.bytes_parser_interface import CppStruct, BytesParserInterface
import zparser


class CppBytesParserAdapter(BytesParserInterface):

    def parse(self, bytes_str: str) -> CppStruct:
        try:
            json_cpp_struct = zparser.parse_to_json(bytes_str)
            # print("JSON Cpp Struct: ", json_cpp_struct)
        except ValueError as e:
            print(f"Ошибка при разборе строки: {e}")
            # Обработка ошибки или повторная генерация исключения
            raise

        return json.loads(json_cpp_struct)

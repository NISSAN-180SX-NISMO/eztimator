import re
from dataclasses import dataclass
from typing import TypeAlias, Dict, Any

# Ключ из исходного файла с байтовыми последовательностями:
SourceKey: TypeAlias = str

# Сишная структура, представленная в виде словаря, где ключ - название поля, значение - значение поля:
CppStruct: TypeAlias = Dict[Any, Any]

# Структура, пролученная в ответ на запрос к бд или http из get_info:
InfoStruct: TypeAlias = Dict[str, str]


# Ну типа чтобы хранить значение target_key
class RegexString:
    def __init__(self, pattern: str):
        self.pattern = pattern
        self.regex = re.compile(pattern)

    def match(self, string: str) -> bool:
        return bool(self.regex.match(string))

    def __repr__(self) -> str:
        return f"RegexString({self.pattern})"


## FOR ESTIMATE RESULTS:

# Название поля в структуре:
FieldName: TypeAlias = str

# Значнеие поля в структуре:
FieldValue: TypeAlias = Any

# Частота, с которой значение встречается для какого-то поля, среди всех других значений этого поля (в %)
ValueFreq: TypeAlias = float

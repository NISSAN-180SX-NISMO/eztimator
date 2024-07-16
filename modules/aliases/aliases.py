from typing import TypeAlias, Dict, Any

# Ключ из исходного файла с байтовыми последовательностями:
SourceKey: TypeAlias = str

# Один из ключей, полученный из get_info, по которому осуществляется выборка для анализ:
TargetKey: TypeAlias = str

# Сишная структура, представленная в виде словаря, где ключ - название поля, значение - значение поля:
CppStruct: TypeAlias = Dict[Any, Any]

# Структура, пролученная в ответ на запрос к бд или http из get_info:
InfoStruct: TypeAlias = Dict[str, str]

## FOR ESTIMATE RESULTS:

# Название поля в структуре:
FieldName: TypeAlias = str

# Значнеие поля в структуре:
FieldValue: TypeAlias = Any

# Частота, с которой значение встречается для какого-то поля, среди всех других значений этого поля (в %)
ValueFreq: TypeAlias = float

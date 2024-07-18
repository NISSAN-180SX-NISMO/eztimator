# С++ binding with python (pybind11)
- `CMakeLists.txt` по сути не нужен, так как сборка происходит через скрипт `build.py`, однако я использую его чтобы сконфигурировать проект с++
- !!! необходимо добавить путь до `.pyd` в `PYTHONPATH` !!!
- для корректной сборки `.pyd` необходимо, чтобы название библиотеки было одинаковое:
  - в файле `python_interface.cpp` при объяявлении модуля `PYBIND11_MODULE(<lib_name>, m)`.
  - в файле `build.py` в списке расширений `Extension( '<lib_name>', ... )`.
  - в файле `build.py` в конфигурации пакета `setup( name='<lib_name>', ... )`.


### Источники:
- [СОЗДАЕМ С++ PYTHON РАСШИРЕНИЯ С ПОМОЩЬЮ PYBIND11](https://smyt.ru/blog/sozdaem-s-python-rasshireniya-s-pomshyu-pybind11/)
- [C/C++ из Python (CFFI, pybind11)](https://habr.com/ru/articles/468099/)



# Estimate
В первую очередь нужно разобраться с условными обозначениями:
1) `source_key: str` - самый главный исходный ключ, полученный из файла
2) `target_key: {key: str, value: str}` - пара (структура) ключ - значение, полученная из бд или http запроса. Множество таких пар будет составлять словарь `info`
3) `cpp_struct: Dict[Any, Any]` - сишная структура в формате json. Особенность в том, что может иметь в себе любые поля, коллекции, а также другие структуры любой вложенности

## Алгоритм оценки
1) Если представить связи между всем объемом исходных данных, то это можно отобразить в виде:
```
    .-- [<cpp_struct>, ...]
   |
source_key
   |
    `-- {<source_key>: <target_key>, ...}
```
То есть `source_key` связывает между собой список `[<cpp_struct>, ...]`, который представлен в виде списка байтовых последовательностей `'structs'`, и множество `{<source_key>: <target_key>, ...}`, которое представляет из себя мапу `'info'` 
Задача стоит в том, чтобы сравнить между собой структуры `'structs'`, выбранные по 1-му или нескольким `target_key`
1) Первым шагом нужно отфильтровать `'structs'` с учетом множества `'target_keys' = [<target_key>, ...]`. Изначально нам доступен `.txt` файл, который хранит исходные данные - ключи и их последовательности байтов. После парсинга, в программе это представленно в виде: `{source_key: [<cpp_struct>, ...], ...}`.
Таким образом, нужно выбрать только те пары `{source_key: [<cpp_struct>, ...]}`, для которых в мапе `'info'` найдутся сразу *<strong>ВСЕ</strong>* `target_key`
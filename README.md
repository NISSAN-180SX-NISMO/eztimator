## c++ binding with python (pybind11)
- ```CMakeLists.txt``` по сути не нужен, так как сборка происходит через скрипт ```build.py```, однако я использую его чтобы сконфигурировать проект с++
- !!! необходимо добавить путь до ```.pyd``` в ```PYTHONPATH``` !!!
- для корректной сборки ```.pyd``` необходимо, чтобы название библиотеки было одинаковое 
  - в файле ```python_interface.cpp``` при объяявлении модуля ```PYBIND11_MODULE(<lib_name>, m)```
  - в файле ```build.py``` в списке расширений ```Extension( '<lib_name>', ... )```
  - в файле ```build.py``` в конфигурации пакета ```setup( name='<lib_name>', ... )```


### Источники:
- [СОЗДАЕМ С++ PYTHON РАСШИРЕНИЯ С ПОМОЩЬЮ PYBIND11](https://smyt.ru/blog/sozdaem-s-python-rasshireniya-s-pomshyu-pybind11/)
- [C/C++ из Python (CFFI, pybind11)](https://habr.com/ru/articles/468099/)
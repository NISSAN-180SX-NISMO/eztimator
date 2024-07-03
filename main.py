import pprint
import sys
from DataSourceHandlers.FileDataSourceHandler import FileDataSourceHandler
from DataSourceHandlers.DataSourceHandlerInterface import DataSourceHandlerInterface

from comparator.FieldsComparator import compare_fields
source = {
    'field_0': True,
    'field_1': False,
    'field_2': True
    # 'field_3': True,
    # 'field_4': False
}

target = {
    'field_0': False,
    'field_1': False,
    'field_2': True
    # 'field_3': True,
    # 'field_4': False
}


def main() -> int:
    # data_source_handler: DataSourceHandlerInterface = FileDataSourceHandler('test_data_source.txt', ',', '\r\n')
    # pp = pprint.PrettyPrinter(indent=4)
    # pp.pprint(data_source_handler.get_info())
    # data_source_handler

    print(compare_fields(source, target))

    # Исходные наборы битов
    a = 0b010  # 2 в десятичной системе
    b = 0b110  # 6 в десятичной системе

    # Применение операции XOR
    xor_result = a ^ b

    # Вывод результата в двоичном виде
    print(f'{xor_result:03b}')

    return 0


if __name__ == '__main__':
    main()

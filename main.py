import pprint
import sys
from DataSourceHandlers.FileDataSourceHandler import FileDataSourceHandler
from DataSourceHandlers.DataSourceHandlerInterface import DataSourceHandlerInterface
import time
import keyboard

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

Parser = zparser.zparser()

def on_d_pressed():
    print("Button 'd' pressed")
    Parser.do_work(5)




def do_something():
    try:
        while True:
            start_time = time.time()

            # Выполнение функции do_something
            work_status = "done" if Parser.checkWorkIsDone() == zparser.WORK_STATUS.DONE else "not done"
            work_result = Parser.getWorkResult()

            print(f"work status: {work_status}; work result: {work_result}")

            # Проверка нажатия клавиши "d"
            if keyboard.is_pressed('d'):
                on_d_pressed()

            # Задержка до следующей итерации (раз в секунду)
            elapsed_time = time.time() - start_time
            time.sleep(max(1.0 - elapsed_time, 0))
    except KeyboardInterrupt:
        print("Program interrupted and exiting...")


def main() -> int:
    print(zparser.hello_from_cpp())

    z = zparser.zparser()
    print(z.hello_from_zparser())
    Parser.init()

    print(compare_fields(source, target))

    # Исходные наборы битов
    a = 0b010  # 2 в десятичной системе
    b = 0b110  # 6 в десятичной системе

    # Применение операции XOR
    xor_result = a ^ b

    # Вывод результата в двоичном виде
    print(f'{xor_result:03b}')
    do_something()
    return 0


if __name__ == '__main__':
    main()

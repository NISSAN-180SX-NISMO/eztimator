import pprint
import sys
from DataSourceHandlers.FileDataSourceHandler import FileDataSourceHandler
from DataSourceHandlers.DataSourceHandlerInterface import DataSourceHandlerInterface
import time
import keyboard

import zparser

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
    do_something()
    return 0


if __name__ == '__main__':
    main()

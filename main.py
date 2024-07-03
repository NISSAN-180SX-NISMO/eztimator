import pprint
import sys
from DataSourceHandlers.FileDataSourceHandler import FileDataSourceHandler
from DataSourceHandlers.DataSourceHandlerInterface import DataSourceHandlerInterface

import zparser


def main() -> int:

    print(zparser.hello_from_cpp())

    z = zparser.zparser()
    print(z.hello_from_zparser())
    return 0


if __name__ == '__main__':
    main()

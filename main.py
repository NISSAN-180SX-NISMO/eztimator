import pprint
import sys
from DataSourceHandlers.FileDataSourceHandler import FileDataSourceHandler
from DataSourceHandlers.DataSourceHandlerInterface import DataSourceHandlerInterface
sys.path.append('zparser/')
import Zzz



def main() -> int:
    data_source_handler: DataSourceHandlerInterface = FileDataSourceHandler('test_data_source.txt', ',', '\r\n')
    pp = pprint.PrettyPrinter(indent=4)
    # pp.pprint(data_source_handler.get_info())
    print(Zzz.hello_from_cpp())
    return 0


if __name__ == '__main__':
    main()

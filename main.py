from typing import Iterator, Tuple, List, Dict

import zparser


def get_split_line_iterator(file_path: str, line_delimiter: str, value_delimiter: str) \
        -> Iterator[Tuple[str, List[str]]]:
    with open(file_path, 'r', newline=line_delimiter) as file:
        line: str = file.readline().strip()
        while line:
            values: List[str] = line.split(value_delimiter)
            if len(values) > 1:  # хз че с ключом без значения делать
                key = values.pop(0).strip()  # Оставшиеся элементы как значения
                yield key, values
            line: str = file.readline().strip()


def get_parsed_source_data(file_path: str, line_delimiter: str, value_delimiter: str) \
        -> Dict[str, List[str]]:
    source_data: Dict[str, List[str]] = dict()
    for key, values in get_split_line_iterator(file_path, line_delimiter, value_delimiter):
        source_data[key] = values
    return source_data


db: ... = ...           # TODO
http: ... = ...         # TODO
http_config: ... = ...  # TODO


def get_info(key: str):
    pass
    db_response = db.request(key)
    if db_response is not None:
        return db_response
    else:
        http_response = http.request(key, http_config)
        return http_response


def write_fail_log_to_file():
    pass  # TODO

class Estimator():
    def __init__(self):
        pass

    def add_to_estimate(self, values: ...):
        pass

    def start_estimate(self):
        # TODO: вызов алгоритма на множестве значений
        pass


def main() -> None:
    estimator: Estimator = Estimator()
    TARGET_FIELD: str = 'Type'
    structured_data: Dict[str, List[str]] = get_parsed_source_data('test_data_source.txt', '\r\n', ',')
    requested_data = dict()
    parsed_data = dict()
    for key, value in structured_data.items():
        requested_data[key] = get_info(key).get(TARGET_FIELD)
        if requested_data[key] is None:
            write_fail_log_to_file()
        else:
            parsed_data[key] = [zparser.parseStructA(bytes_str) for bytes_str in structured_data[key]]
            estimator.add_to_estimate(parsed_data[key])


if __name__ == '__main__':
    main()

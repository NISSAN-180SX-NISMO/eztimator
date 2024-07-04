from typing import Iterator, Tuple, List, Dict


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
    db_response = db.request(key)
    if db_response is not None:
        return db_response
    else:
        http_response = http.request(key, http_config)
        return http_response


def write_fail_log_to_file():
    pass  # TODO


def parse_in_cpp(bytes: str) -> Dict[str, bool]:
    pass


def main() -> int:
    TARGET_FIELD: str = 'Type'
    structured_data: Dict[str, List[str]] = get_parsed_source_data('test_data_source.txt', '\r\n', ',')
    parsed_data = dict()
    for key, value in structured_data.items():
        parsed_data[key] = get_info(key).get(TARGET_FIELD)
        if parsed_data[key] is None:
            write_fail_log_to_file()
        else:
            for bytes in structured_data[key]:
                struct = parse_in_cpp(bytes)
                # todo

    return 0


if __name__ == '__main__':
    main()

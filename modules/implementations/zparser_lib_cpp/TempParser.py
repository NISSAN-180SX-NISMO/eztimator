from typing import Dict


class TempParser:
    counter = 0

    def __init__(self):
        pass

    def parse_bytes(self, bytes_str: str) -> (str, Dict[str, bool]): # Я хз пока че он возвращать буедт ес честно
        # Разбиваем строку на пары символов (байты)
        byte_pairs = [bytes_str[i:i + 2] for i in range(0, len(bytes_str), 2)]

        # Создаем словарь, где ключи - индексы байтов, значения - True/False в зависимости от четности байта
        result = {f'field_{i}'.strip(): int(byte, 16) % 2 == 0 for i, byte in enumerate(byte_pairs)}
        self.counter += 1
        return f'struct_{self.counter}'.strip(), result

    def reset_counter(self):
        self.counter = 0
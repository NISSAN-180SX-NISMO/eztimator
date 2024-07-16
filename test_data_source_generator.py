import random
import string

def generate_unique_keys(num_keys):
    keys = set()
    while len(keys) < num_keys:
        key = ''.join(random.choices(string.ascii_uppercase, k=3))
        keys.add(key)
    return list(keys)

def generate_random_hex(length):
    return ''.join(random.choices('0123456789ABCDEF', k=length))

def generate_predefined_values(predefined_values, num_values):
    return random.choices(predefined_values, k=num_values)

def generate_data(num_entries, predefined_values=None):
    keys = generate_unique_keys(num_entries)
    data = []

    for key in keys:
        num_values = random.randint(1, 3)
        if predefined_values:
            values = generate_predefined_values(predefined_values, num_values)
        else:
            # Modify this part to generate hex strings of lengths 4, 6, or 8
            values = [generate_random_hex(random.choice([4, 6, 8])) for _ in range(num_values)]
        entry = f"{key},{','.join(values)}"
        data.append(entry)

    return data

def write_to_file(data, filename):
    with open(filename, 'w') as file:
        for line in data:
            file.write(line + '\n')

if __name__ == "__main__":
    num_entries = 10000  # Количество записей
    filename = 'test_data_source.txt'
    use_predefined_values = False  # Переключение между режимами
    predefined_values = ['A1B2C3', 'D4E5F6', '123ABC', '456DEF', '789012'] if use_predefined_values else None

    data = generate_data(num_entries, predefined_values)
    write_to_file(data, filename)
    print(f"Data successfully written to {filename}")
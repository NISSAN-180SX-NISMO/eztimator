#include <sstream>
#include <random>
#include "zparser.h"

std::string Parser::Struct::to_json(const Parser::Struct::zstruct &obj) {
    std::ostringstream oss;
    oss << "{";
    oss << "\"name\": \"" << obj.name << "\", ";
    oss << "\"capacity\": " << obj.capacity << ", ";
    oss << "\"temperature\": ";
    if (obj.temperature.has_value()) {
        oss << obj.temperature.value();
    } else {
        oss << "null";
    }
    oss << ", \"friends_id\": [";
    for (size_t i = 0; i < obj.friends_id.size(); ++i) {
        oss << obj.friends_id[i];
        if (i < obj.friends_id.size() - 1) {
            oss << ", ";
        }
    }
    oss << "]}";
    return oss.str();
}

std::string Parser::Struct::to_json(const Parser::Struct::vstruct &obj) {
    std::ostringstream oss;
    oss << "{";
    oss << "\"name\": \"" << obj.name << "\", ";
    oss << "\"capacity\": " << obj.capacity << ", ";
    oss << "\"weight\": " << obj.weight << ", ";
    oss << "\"friends_id\": [";
    for (size_t i = 0; i < obj.friends_id.size(); ++i) {
        oss << obj.friends_id[i];
        if (i < obj.friends_id.size() - 1) {
            oss << ", ";
        }
    }
    oss << "]}";
    return oss.str();
}

std::string Parser::parse(Parser::byte_vector bytes) {
    Parser::Struct::TYPE type;
    if (!parse_header(bytes, type)) return ""; // FIXME: mb throw except
    switch (type) {
        case Parser::Struct::TYPE::ZSTRUCT:
        {
            using namespace Parser::Struct;
            zstruct instance;
            if (!parse_zstruct(bytes, instance)) return ""; // FIXME: mb throw except
            return to_json(instance);
        }
        case Parser::Struct::TYPE::VSTRUCT:
        {
            using namespace Parser::Struct;
            vstruct instance;
            if (!parse_vstruct(bytes, instance)) return ""; // FIXME: mb throw except
            return to_json(instance);
        }
        default: return ""; // FIXME: mb throw except
    }
}

bool Parser::parse_header(const Parser::byte_vector& bytes, Struct::TYPE &type) {
    if (bytes.size() <= 1) return false;
    switch (bytes.front() % 2)
    {
        case 0: type = Parser::Struct::TYPE::ZSTRUCT; return true;
        case 1: type = Parser::Struct::TYPE::VSTRUCT; return true;
        default: return false;
    }

}

Parser::Struct::zstruct generate_random_zstruct(int);
Parser::Struct::vstruct generate_random_vstruct(int);

bool Parser::parse_zstruct(const Parser::byte_vector& bytes, Struct::zstruct &instance) {
    instance = generate_random_zstruct(bytes.size());
    return true;
}

bool Parser::parse_vstruct(const Parser::byte_vector& bytes, Struct::vstruct &instance) {
    instance = generate_random_vstruct(bytes.size());
    return true;
}

Parser::Struct::zstruct generate_random_zstruct(int friends_size) {
    // Задаем диапазоны значений
    std::vector<std::string> names = {"alpha", "beta", "gamma"};
    std::vector<int> capacities = {10, 20, 30};
    std::vector<std::optional<float>> temperatures = {36.6f, 37.0f, std::nullopt};
    std::vector<int> friends_ids_pool = {1, 2, 3, 4};

    // Генераторы случайных чисел
    std::random_device rd;
    std::mt19937 gen(rd());

    std::uniform_int_distribution<> name_dist(0, names.size() - 1);
    std::uniform_int_distribution<> capacity_dist(0, capacities.size() - 1);
    std::uniform_int_distribution<> temperature_dist(0, temperatures.size() - 1);
    std::uniform_int_distribution<> friends_dist(0, friends_ids_pool.size() - 1);

    // Заполняем поля случайными значениями
    Parser::Struct::zstruct obj;
    obj.name = names[name_dist(gen)];
    obj.capacity = capacities[capacity_dist(gen)];
    obj.temperature = temperatures[temperature_dist(gen)];

    // Заполняем friends_id случайным количеством друзей
    for (int i = 0; i < friends_size; ++i) {
        obj.friends_id.push_back(friends_ids_pool[friends_dist(gen)]);
    }

    return obj;
}

Parser::Struct::vstruct generate_random_vstruct(int friends_size) {
    // Задаем диапазоны значений
    std::vector<std::string> names = {"alpha", "beta", "gamma"};
    std::vector<int> capacities = {10, 20, 30};
    std::vector<float> weights = {70.5f, 75.0f, 80.5f};
    std::vector<int> friends_ids_pool = {1, 2, 3, 4, 5};

    // Генераторы случайных чисел
    std::random_device rd;
    std::mt19937 gen(rd());

    std::uniform_int_distribution<> name_dist(0, names.size() - 1);
    std::uniform_int_distribution<> capacity_dist(0, capacities.size() - 1);
    std::uniform_int_distribution<> weight_dist(0, weights.size() - 1);
    std::uniform_int_distribution<> friends_dist(0, friends_ids_pool.size() - 1);

    // Заполняем поля случайными значениями
    Parser::Struct::vstruct obj;
    obj.name = names[name_dist(gen)];
    obj.capacity = capacities[capacity_dist(gen)];
    obj.weight = weights[weight_dist(gen)];

    // Заполняем friends_id случайным количеством друзей
    for (int i = 0; i < friends_size; ++i) {
        obj.friends_id.push_back(friends_ids_pool[friends_dist(gen)]);
    }

    return obj;
}

std::vector<uint8_t> Api::ApiConverter::hex_string_to_bytes(const std::string &hexString)
{
    std::vector<uint8_t> bytes;

    // Проверяем, что длина строки четная
    if (hexString.length() % 2 != 0) {
        throw std::invalid_argument("Invalid hex string length");
    }

    // Итерируемся по строке с шагом 2, так как каждые два символа - это один байт
    for (size_t i = 0; i < hexString.length(); i += 2) {
        // Получаем подстроку из двух символов
        std::string byteString = hexString.substr(i, 2);

        // Преобразуем подстроку в число типа uint8_t
        uint8_t byte = static_cast<uint8_t>(std::stoi(byteString, 0, 16));

        // Добавляем байт в вектор
        bytes.push_back(byte);
    }

    return bytes;
}

std::string Api::parse_to_json(const std::string & str_bytes) {
    return Parser::parse(Api::ApiConverter::hex_string_to_bytes(str_bytes));
}

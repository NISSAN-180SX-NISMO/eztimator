//
// Created by user on 02/07/2024.
//

#ifndef ZPARSER_ZPARSER_H
#define ZPARSER_ZPARSER_H
#include <string>
#include <vector>
#include <cstdlib>
#include <optional>
#include <cstdint>
namespace Api
{
    namespace ApiConverter
    {
        std::vector<uint8_t> hex_string_to_bytes(const std::string& hexString);
    } // namespace ApiConverter

    std::string parse_to_json(const std::string&);
}

namespace Parser
{
    namespace Struct
    {
        enum TYPE {
            ZSTRUCT,
            VSTRUCT,
            NESTED
        };

        struct nested_struct
        {
            int id = 123;
            std::string title = "hello, petyhon!";
            std::vector<uint8_t> command = {0xFF, 0xD3, 0x4E, 0x00};
        };

        struct zstruct
        {
            std::string name;
            int capacity;
            std::optional<float> temperature;
            std::vector<int> friends_id;
            nested_struct nstruct = nested_struct();
        };

        struct vstruct
        {
            std::string name;
            int capacity;
            float weight;
            std::vector<int> friends_id;
            nested_struct nstruct = nested_struct();
        };

        std::string to_json(const zstruct&);
        std::string to_json(const vstruct&);
        std::string to_json(const nested_struct&);
    } // namespace Struct

typedef std::vector<uint8_t> byte_vector;

std::string parse(byte_vector);
bool parse_header(const byte_vector&, Struct::TYPE&);
bool parse_zstruct(const byte_vector&, Struct::zstruct&);
bool parse_vstruct(const byte_vector&, Struct::vstruct&);
} // namespace parser

#endif //ZPARSER_ZPARSER_H

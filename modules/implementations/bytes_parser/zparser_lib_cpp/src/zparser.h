//
// Created by user on 02/07/2024.
//

#ifndef ZPARSER_ZPARSER_H
#define ZPARSER_ZPARSER_H
#include <string>
#include <vector>
#include <cstdlib>

struct BaseStruct {
    std::string struct_type;
};

struct zstruct : public BaseStruct {
    int a;
    double b;
    char c;
};

struct vstruct : public BaseStruct {
    int d;
    double e;
    char c;
};

void parse_zstruct(zstruct& zs) {
    zs.a = rand() % 100;
    zs.b = (double)(rand() % 10000) / 100;
    zs.c = 'A' + (rand() % 26);
}

void parse_vstruct(vstruct& vs) {
    vs.d = rand() % 100;
    vs.e = (double)(rand() % 10000) / 100;
    vs.c = 'A' + (rand() % 26);
}

BaseStruct* process_bytes(const std::string& byte_string) {
    if (byte_string.empty()) {
        return nullptr;
    }

    uint8_t first_byte = byte_string[0];
    if (first_byte % 2 == 0) {
        zstruct zs;
        parse_zstruct(zs);
        return &zs;
    } else {
        vstruct vs;
        parse_vstruct(vs);
        return &vs;
    }
}


#endif //ZPARSER_ZPARSER_H

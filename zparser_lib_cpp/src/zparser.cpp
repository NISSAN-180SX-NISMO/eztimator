//
// Created by user on 03/07/2024.
//

#include <thread>
#include <vector>
#include <array>
#include "zparser.h"

std::string zparser::hello_from_zparser() {
    return "omg, zparser!";
}

void zparser::init() {
    this->workResult = "nothing";
    this->status = WORK_STATUS::NOTHING_TO_DO;
}

void zparser::do_work(uint8_t secForWork) {
    this->status = WORK_STATUS::IN_PROCESS;
    std::this_thread::sleep_for(std::chrono::seconds(secForWork));
    this->workResult = "ABOBA NUMBER " + std::to_string(rand() % 5);
    this->status = WORK_STATUS::DONE;
}

zparser::WORK_STATUS zparser::checkWorkIsDone() {
    return this->status;
}

std::string zparser::getWorkResult() {
    auto _workResult = this->workResult;
    this->workResult = "nothing";
    this->status = WORK_STATUS::NOTHING_TO_DO;
    return _workResult;
}

std::string hello_from_cpp() {
    return "omg, cpp!";
}

StructA parseStructA(const std::string &byte_string) {
    return StructA
            {
                    bool(rand() & 2),
                    bool(rand() & 2),
                    bool(rand() & 2)
            };
    // TODO: Придумать чета епта
//    std::stringstream stream(byte_string, std::ios::in | std::ios::binary);
//    stream.exceptions(std::ios_base::failbit | std::ios_base::badbit);
//
//    uint8_t field1, field2, field3;
//    try {
//        stream.read(reinterpret_cast<char*>(&field1), sizeof(field1));
//        a.field1 = !(field1 % 2);
//        stream.read(reinterpret_cast<char*>(&field2), sizeof(field2));
//        a.field2 = !(field2 % 2);
//        stream.read(reinterpret_cast<char*>(&field3), sizeof(field3));
//        a.field3 = !(field3 % 2);
//    } catch (const std::ios_base::failure& e) {
//        std::cerr << "Exception: " << e.what() << std::endl;
//    }
}

bool parse(const std::vector<uint8_t> &bytes) {
    for (auto& byte: bytes)
        std::cout << byte;

    std::cout << std::endl
            << "bytes.size: " << bytes.size()
            << "; bytes sizeof: " << sizeof(bytes)
            << std::endl;
    return true;
}




bool parse(const std::string &bytes) {
    auto byte_vector = std::vector<uint8_t>(bytes.begin(), bytes.end());
    for (auto& byte: byte_vector)
        std::cout << byte;

    std::cout << std::endl
            << "bytes.size: " << byte_vector.size()
            << "; bytes sizeof: " << sizeof(byte_vector)
            << std::endl;
    return true;
}

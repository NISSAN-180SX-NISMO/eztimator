//
// Created by user on 02/07/2024.
//

#ifndef ZPARSER_ZPARSER_H
#define ZPARSER_ZPARSER_H
#include <string>
#include <cstdint>
#include <sstream>
#include <iostream>

class zparser
{
public:
    enum WORK_STATUS: uint8_t
    {
        IN_PROCESS,
        DONE,
        NOTHING_TO_DO
    };
    std::string hello_from_zparser();
/// interface:
    void init();
    void do_work(uint8_t secForWork);
    WORK_STATUS checkWorkIsDone();
    std::string getWorkResult();
private:
    std::string workResult;
    WORK_STATUS status;
};

std::string hello_from_cpp();


struct StructA
{
    bool field1;
    bool field2;
    bool field3;
};

StructA parseStructA(const std::string& byte_string);


#endif //ZPARSER_ZPARSER_H

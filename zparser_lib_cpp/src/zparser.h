//
// Created by user on 02/07/2024.
//

#ifndef ZPARSER_ZPARSER_H
#define ZPARSER_ZPARSER_H
#include <string>
#include <cstdint>

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


#endif //ZPARSER_ZPARSER_H

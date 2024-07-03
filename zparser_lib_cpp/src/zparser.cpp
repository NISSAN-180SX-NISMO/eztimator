//
// Created by user on 03/07/2024.
//

#include <thread>
#include "zparser.h"

std::string zparser::hello_from_zparser()
{
    return "omg, zparser!";
}

void zparser::init()
{
    this->workResult = "nothing";
    this->status = WORK_STATUS::NOTHING_TO_DO;
}

void zparser::do_work(uint8_t secForWork)
{
    this->status = WORK_STATUS::IN_PROCESS;
    std::this_thread::sleep_for(std::chrono::seconds(secForWork));
    this->workResult = "ABOBA NUMBER " + std::to_string(rand()%5);
    this->status = WORK_STATUS::DONE;
}

zparser::WORK_STATUS zparser::checkWorkIsDone()
{
    return this->status;
}

std::string zparser::getWorkResult()
{
    auto _workResult = this->workResult;
    this->workResult = "nothing";
    this->status = WORK_STATUS::NOTHING_TO_DO;
    return _workResult;
}

std::string hello_from_cpp()
{
    return "omg, cpp!";
}
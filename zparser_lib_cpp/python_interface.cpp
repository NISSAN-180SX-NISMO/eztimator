#include <pybind11/pybind11.h>
#include "src/zparser.h"

namespace py = pybind11;

PYBIND11_MODULE(zparser, m) {
    m.def("hello_from_cpp", &hello_from_cpp);

    py::class_<zparser>(m, "zparser")
        .def(py::init<>())
        .def("hello_from_zparser", &zparser::hello_from_zparser)
        .def("init", &zparser::init)
        .def("do_work", &zparser::do_work)
        .def("checkWorkIsDone", &zparser::checkWorkIsDone)
        .def("getWorkResult", &zparser::getWorkResult);

    py::enum_<zparser::WORK_STATUS>(m, "WORK_STATUS")
        .value("IN_PROCESS", zparser::WORK_STATUS::IN_PROCESS)
        .value("DONE", zparser::WORK_STATUS::DONE)
        .value("NOTHING_TO_DO", zparser::WORK_STATUS::NOTHING_TO_DO)
        .export_values();
}

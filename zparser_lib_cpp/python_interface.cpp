//
// Created by user on 02/07/2024.
//
#include <pybind11/pybind11.h>
#include "src/zparser.h"
namespace py = pybind11;

PYBIND11_MODULE(zparser, m) {
    m.def("hello_from_cpp", &hello_from_cpp);

    py::class_<zparser>(m, "zparser")
        .def(py::init<>())
        .def("hello_from_zparser", &zparser::hello_from_zparser);
};
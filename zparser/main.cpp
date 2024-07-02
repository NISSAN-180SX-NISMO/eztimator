//
// Created by user on 02/07/2024.
//
#include <pybind11/pybind11.h>
#include "zparser.h"
namespace py = pybind11;

PYBIND11_MODULE(Zzz, m) {
    m.def("hello_from_cpp", &hello_from_cpp);
};
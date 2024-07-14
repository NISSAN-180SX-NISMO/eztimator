#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include "src/zparser.h"

namespace py = pybind11;

PYBIND11_MODULE(zparser, m) {
    py::class_<BaseStruct>(m, "BaseStruct")
        .def(py::init<>())
        .def_readwrite("struct_type", &BaseStruct::struct_type);

    py::class_<zstruct, BaseStruct>(m, "zstruct")
        .def(py::init<>())
        .def_readwrite("a", &zstruct::a)
        .def_readwrite("b", &zstruct::b)
        .def_readwrite("c", &zstruct::c);

    py::class_<vstruct, BaseStruct>(m, "vstruct")
        .def(py::init<>());
        .def_readwrite("d", &zstruct::d)
        .def_readwrite("e", &zstruct::e)
        .def_readwrite("c", &zstruct::c);

    m.def("parse_zstruct", &parse_zstruct, "A function that fills a zstruct with random values");
    m.def("parse_vstruct", &parse_vstruct, "A function that fills a vstruct with random values");
    m.def("process_bytes", &process_bytes, "A function that processes a byte string");
}

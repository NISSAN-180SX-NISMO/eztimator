#include "src/zparser.h"
#include <pybind11/stl.h>
#include <pybind11/pybind11.h>

namespace py = pybind11;

PYBIND11_MODULE(zparser, m) {
    m.def("parse_to_json", &Api::parse_to_json);
}

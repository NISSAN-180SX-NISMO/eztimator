cmake_minimum_required(VERSION 3.12)
project(zparser-lib)

set(CMAKE_CXX_STANDARD 14)

# Указываем путь к установленной pybind11
set(pybind11_DIR C:/Users/user/AppData/Local/Programs/Python/Python39/Lib/site-packages/pybind11)

# Включаем модуль pybind11
find_package(pybind11 REQUIRED PATHS ${pybind11_DIR})

# Добавляем вашу библиотеку
add_library(zparser-lib MODULE python_interface.cpp)
target_link_libraries(zparser-lib PRIVATE pybind11::module)

cmake_minimum_required(VERSION 3.12)
project(zparser)

set(CMAKE_CXX_STANDARD 17)

# Указываем путь к установленной pybind11
set(pybind11_DIR C:/Users/user/AppData/Local/Programs/Python/Python39/Lib/site-packages/pybind11)

# Включаем модуль pybind11
find_package(pybind11 REQUIRED PATHS ${pybind11_DIR})

# Добавляем вашу библиотеку
add_library(zparser MODULE python_interface.cpp src/zparser.cpp)

# Указываем имя выходного файла с расширением .pyd
set_target_properties(zparser PROPERTIES SUFFIX ".pyd")

target_link_libraries(zparser PRIVATE pybind11::module)

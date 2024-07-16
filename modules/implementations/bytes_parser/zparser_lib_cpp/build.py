import pybind11
from setuptools import setup, Extension
import os

# Задайте полный путь к вашему компилятору GCC
gcc_path = 'C:/Qt/Tools/mingw1120_64/bin/gcc.exe'
gxx_path = 'C:/Qt/Tools/mingw1120_64/bin/g++.exe'

# Установка переменных среды для использования конкретного GCC
os.environ['CC'] = gcc_path
os.environ['CXX'] = gxx_path
os.environ['LDSHARED'] = f'{gxx_path} -shared'

extra_compile_args = ['/std:c++17']

ext_modules = [
    Extension(
        'zparser',  # название нашей либы
        ['python_interface.cpp', 'src/zparser.cpp'],  # файлы, которые компилируем
        include_dirs=[pybind11.get_include()],  # добавляем include для pybind11
        language='c++',
        extra_compile_args=extra_compile_args,  # используем соответствующий стандарт для компилятора
    ),
]

setup(
    name='zparser',
    version='0.1.0',
    author='user',
    author_email='user@user.ru',
    description='pybind11 extension',
    ext_modules=ext_modules,
    requires=['pybind11'],
    python_requires='==3.10',  # указываем, что ваше расширение предназначено именно для Python 3.10
)


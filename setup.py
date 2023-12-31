from setuptools import setup, find_packages

from bank_algorithms.bank_priority_sort_algorithm import __version__

setup(
    name='bank_algorithms',
    version="0.1",

    url='https://github.com/Gorodskoy-Konh/MORE-5.0-Algorithm',
    author='Nagim Isyanbaev',
    author_email='n.isyanbaev@innopol.university',
    packages=find_packages(),

    py_modules=['bank_algorithms'],
)
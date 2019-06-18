#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from setuptools import setup

# requirements
reqs = list()
with open('requirements.txt') as file:
    for line in file:
        reqs.append(line.strip())

# readme
README = open('README.rst').read()
HISTORY = open('HISTORY.rst').read()

setup(
    name='coindata',
    version='1.4',
    description='Historical data manager for cryptos.',
    long_description=README + (os.linesep * 2) + HISTORY,
    packages=['coindata'],
    url='https://github.com/Anaxilaus/coindata',
    author='Anaxilaus',
    install_requires=reqs
)

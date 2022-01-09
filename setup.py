#!/usr/bin/env python
"""
MCV 09.01.2022
"""

import sys

from setuptools import find_packages, setup

if sys.version_info < (3, 5):
    raise RuntimeError(
        "This Repo supports Python 3.6 and above. "
    )

INSTALL_REQUIRES = [

]

setup(
    name='hammuon',
    version='0.1.11',
    description='Base Data Structures Algorithm',
    url='https://github.com/mcvarer/algorithms.git',
    author='M.C.V',
    author_email='ktuce.mcanv@gmail.com',
    license='licensed',
    packages=find_packages(),
    install_requires=INSTALL_REQUIRES,
    python_requires=">=3.6, <4",
    project_urls={  # Optional
            'Bug Reports': 'https://github.com/mcvarer/algorithms/issues'
        },
)
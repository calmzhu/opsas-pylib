#!/usr/bin/env python

"""
distutils/setuptools install script.
"""
import os
import sys

import setuptools
import importlib

ROOT = os.path.dirname(__file__)

sys.path.append(ROOT)


def get_version():
    module = importlib.import_module("configer")
    return module.VERSION


with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="opsas configer",
    version=get_version(),
    author="Calm Zhu",
    author_email="saint@justcalm.org",
    description="A configer Adapter for python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pipeline-factory/py-configerAdapter",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)

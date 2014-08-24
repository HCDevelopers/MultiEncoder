#!/usr/bin/env python
# coding=utf-8
#
# Setup script for the MultiEncoder package.
#
# Author: Psycho_Coder <psychocoder@outlook.com>
# URL: https://github.com/HCDevelopers/MultiEncoder
# For license information, see LICENSE

import os
import sys

from setuptools import setup, find_packages


def read_files(filename):
    try:
        with open(os.path.join(os.path.dirname(__file__), filename), "r") as f:
            return f.read()
    except IOError:
        return ""


long_desc = read_files("README.md")
requirements = read_files("REQUIREMENTS").splitlines()
version = read_files("hcdev/VERSION")
classifiers = read_files("CLASSIFIERS").splitlines()

packages = find_packages(exclude=["tests"])
sys.dont_write_bytecode = True

setup(
    name="MultiEncoder",
    version=version,
    description="MultiEncoder is a tool that provides various chain encryptions and encodings",
    long_description=long_desc,
    url="https://github.com/HCDevelopers/MultiEncoder",
    license="MIT",
    author="Psycho_Coder, Deque, Ex094, noize",
    author_email="psychocoder@outlook.com",
    packages=packages,
    maintainer="Psycho_Coder",
    maintainer_email="psychocoder@outlook.com",
    classifiers=classifiers,
    download_url="https://codeload.github.com/HCDevelopers/MultiEncoder/zip/master",
    keywords=[
        "Python",
        "Encoding Tool",
        "Cryptography",
        "String encodings",
        "Chain encryptions"
    ]
)

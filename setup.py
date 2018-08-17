#!/usr/bin/env python3

# io.open is needed for projects that support Python 2.7
# It ensures open() defaults to text mode with universal newlines,
# and accepts an argument to specify the text encoding
# Python 3 only projects can skip this import
from io import open
from os import path

# Always prefer setuptools over distutils
try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages

here = path.abspath(path.dirname(__file__))

# Main
# ------------------------------------------------
try:
    long_description = open("README.md").read()
except OSError:
    long_description = "not available"

try:
    license_ = open("LICENSE.md").read()
except OSError:
    license_ = "not available"

setup(
    name="flowjs",
    packages=["flowjs"],
    platforms=["any"],
    version="0.1.1",
    description="Python server implementation for flow.js upload library",
    long_description=long_description,
    author="Huw Jones",
    author_email="huwcbjones@gmail.com",
    url="https://github.com/huwcbjones/py-flowjs",
    download_url="https://github.com/huwcbjones/py-flowjs/archive/master.zip",
    license=license_,
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Development Status :: 5 - Production/Stable",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Intended Audience :: Developers",
        "Topic :: Internet",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: HTTP Servers",
        "Topic :: Software Development :: Libraries"
    ],
    install_requires=[
        'filelock'
    ],
)

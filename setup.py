# coding: utf-8



import sys
from setuptools import setup, find_packages

NAME = "flockos"
VERSION = "1.2.0"

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["requests", "six >= 1.10", "PyJWT"]

setup(
    name=NAME,
    version=VERSION,
    description="Flock API",
    author_email="",
    url="",
    keywords=["Flock API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    Integrate your apps with flock using this API
    """
)

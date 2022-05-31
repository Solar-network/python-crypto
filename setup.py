import sys

import setuptools

requires = [
    "base58==2.1.1",
    "binary-helpers==0.0.4",
    "coincurve==16.0.0",
    "btclib==2022.2.9",
    "pycryptodome==3.14.1",
]

tests_require = [
    "flake8==4.0.1",
    "flake8-import-order==0.18.1",
    "flake8-print==4.0.1",
    "flake8-quotes==3.3.1",
    "pytest==7.0.1; python_version < '3.7'",
    "pytest==7.1.2; python_version >= '3.7'",
    "isort==5.10.1",
    "pytest-cov==2.5.1",
    "black==22.3.0",
]

extras_require = {"test": tests_require, "dev": requires + tests_require}

setup_requires = ["pytest-runner"] if {"pytest", "test", "ptr"}.intersection(sys.argv) else []

setuptools.setup(
    name="solarnetwork-crypto",
    description="A simple Cryptography Implementation in Python for the Solar Blockchain.",
    version="3.0.0",
    author="Solar-Network",
    author_email="hello@solar.org",
    url="https://github.com/Solar-network/python-crypto",
    packages=setuptools.find_packages(exclude=["tests", "tests.*"]),
    install_requires=requires,
    extras_require=extras_require,
    tests_require=tests_require,
    setup_requires=setup_requires,
)

import sys

import setuptools

requires = ["base58", "binary-helpers", "coincurve", "btclib", "pycryptodome"]

tests_require = [
    "flake8>=4.0.1",
    "flake8-import-order>=0.18.1",
    "flake8-print>=5.0.0",
    "flake8-quotes>=3.3.1",
    "pytest>=3.6.1",
    "isort>=5.10.1",
    "pytest-cov>=2.5.1",
    "black>=22.3.0",
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

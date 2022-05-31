import sys

import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

requires = ["base58", "binary-helpers", "coincurve", "btclib"]

tests_require = [
    "flake8",
    "flake8-import-order",
    "flake8-print",
    "flake8-quotes",
    "pytest",
    "isort",
    "pytest-cov",
    "black",
]

extras_require = {"test": tests_require, "dev": requires + tests_require}

setup_requires = ["pytest-runner"] if {"pytest", "test", "ptr"}.intersection(sys.argv) else []

setuptools.setup(
    name="solar-crypto",
    description="A simple Cryptography Implementation in Python for the Solar Blockchain.",
    version="3.0.0",
    author="Solar-Network",
    author_email="hello@solar.org",
    url="https://github.com/Solar-network/python-crypto",
    packages=setuptools.find_packages(exclude=["tests", "tests.*"]),
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=requires,
    extras_require=extras_require,
    tests_require=tests_require,
    setup_requires=setup_requires,
    python_requires=">=3.6",
)

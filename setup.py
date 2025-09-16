"""Setup.py for human_typer."""

import os
from pathlib import Path

from setuptools import find_packages, setup

# allow setup.py to be run from any path
os.chdir(Path(__file__).resolve().parent)

setup(
    name="human_typer",
    version="1.0.8",
    packages=find_packages(),
    include_package_data=True,
    license="MIT License",
    description="Python package to simulate human keyboard typing",
    keywords="human typing bot keyboard",
    url="https://github.com/UnMars/human_typer",
    author="UnMars",
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
)

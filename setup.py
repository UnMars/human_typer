"""Setup.py for human_typer."""

import os
from pathlib import Path

from setuptools import find_packages, setup

# allow setup.py to be run from any path
os.chdir(Path(__file__).resolve().parent)

setup(
    name="human_typer",
    version="1.0.9",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    include_package_data=True,
    license="MIT License",
    description="Python package to simulate human keyboard typing",
    long_description=Path("README.md").read_text(encoding="utf-8"),
    long_description_content_type="text/markdown",
    keywords="human typing bot keyboard selenium automation",
    url="https://github.com/UnMars/human_typer",
    author="UnMars",
    author_email="guillaume_roboam@hotmail.fr",
    python_requires=">=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*",
    install_requires=[
        "keyboard>=0.13.5",
        "selenium>=3.0.0",
    ],
    extras_require={
        "dev": [
            "pytest>=6.0",
            "black>=21.0",
            "flake8>=3.8",
        ],
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
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
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Software Development :: Testing",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)

#!/usr/bin/env python

from setuptools import setup, find_packages  # type: ignore

with open("README.md") as readme_file:
    readme = readme_file.read()

setup(
    author="Joao Filho Drummer",
    author_email="devdrummerzzz@gmail.com",
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
    ],
    description="Faz a validação de CPF Brasileiro",
    entry_points={"console_scripts": ["validate_cnpj=validate_cnpj.cli:main",],},
    install_requires=[],
    license="MIT license",
    long_description=readme,
    long_description_content_type="text/markdown",
    package_data={"validate_cnpj": ["py.typed"]},
    include_package_data=True,
    keywords="validate_cnpj",
    name="validate_cnpj",
    package_dir={"": "src"},
    packages=find_packages(include=["src/validate_cnpj", "src/validate_cnpj.*"]),
    setup_requires=[],
    url="https://github.com/drummerzzz/pypi_validate_cnpj",
    version="0.0.1",
    zip_safe=False,
)

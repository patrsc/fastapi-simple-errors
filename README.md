[![Tests](https://github.com/patrsc/fastapi-simple-errors/actions/workflows/tests.yml/badge.svg)](https://github.com/patrsc/fastapi-simple-errors/actions/workflows/tests.yml)
[![Linting](https://github.com/patrsc/fastapi-simple-errors/actions/workflows/linting.yml/badge.svg)](https://github.com/patrsc/fastapi-simple-errors/actions/workflows/linting.yml)

# fastapi-simple-errors

Simple error handling for fastapi using custom error classes.

## Introduction

This small Python package aims to simplify error handling for
[FastAPI](https://fastapi.tiangolo.com/):
* It allows defining custom exception classes in a simple way with little boilerplate code.
* Your application functions can raise these errors and they will be propageted to FastAPI and
  result in a proper 4xx or 5xx status code to be sent to the client.
* Proper OpenAPI documentation can be generated using the correct response schema for errors. 

## Usage

The package [fastapi-simple-errors](https://pypi.org/project/fastapi-simple-errors/) is available
on [PyPi](https://pypi.org/), so it can be installed with Python package managers such as
`pip` or [poetry](https://python-poetry.org/).

Usage example:

TODO

## Licence

MIT

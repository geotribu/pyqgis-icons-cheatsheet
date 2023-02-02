# PyQGIS icons cheatsheet generator

[![🚀 Build & publish](https://github.com/geotribu/pyqgis-icons-cheatsheet/actions/workflows/deploy.yml/badge.svg)](https://github.com/geotribu/pyqgis-icons-cheatsheet/actions/workflows/deploy.yml)

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![flake8](https://img.shields.io/badge/linter-flake8-green)](https://flake8.pycqa.org/)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)

----

## Development

### Requirements

- Python 3.10+
- network connection authorized to github.com
- [Material for Mkdocs Insiders](https://squidfunk.github.io/mkdocs-material/insiders/) (sponsorware) token set as environment variable `GH_TOKEN_MATERIAL_INSIDERS`

### Setup

Typically on Ubuntu:

```sh
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -U pip setuptools wheel
python -m pip install -U -r requirements.txt
pre-commit install
```

### Cheatsheet

Run the script:

```sh
python qrc_preview_in_md.py
```

The output markdown page is located at `docs/index.md`, overriding the version pushed as project has been started.

### Website

Build:

```sh
mkdocs build
```

Serve locally:

```sh
mkdocs serve
```

Open your browser on: `http://localhost:8000`

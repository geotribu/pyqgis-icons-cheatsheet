# PyQGIS icons cheatsheet generator

[![🚀 Build & publish](https://github.com/geotribu/pyqgis-icons-cheatsheet/actions/workflows/deploy.yml/badge.svg)](https://github.com/geotribu/pyqgis-icons-cheatsheet/actions/workflows/deploy.yml)

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![flake8](https://img.shields.io/badge/linter-flake8-green)](https://flake8.pycqa.org/)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/geotribu/pyqgis-icons-cheatsheet/main.svg)](https://results.pre-commit.ci/latest/github/geotribu/pyqgis-icons-cheatsheet/main)

Script to convert a remote QRC (Qt Resources Collection files) into a markdown table to preview images.

This project covers [QGIS project](https://github.com/qgis/QGIS/) and generates a cheatsheet published on <https://geotribu.github.io/pyqgis-icons-cheatsheet/>.

## Credits

Author: Julien M. (:octopus: [Guts on GitHub](https://github.com/guts/), :bird: [GeoJulien on Twitter](https://twitter.com/geojulien/)) for [Geotribu collaborative website](http://geotribu.fr).

Code under MIT license.  
Content and methodolgy under [Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)](https://creativecommons.org/licenses/by-sa/4.0/).  
Website [icon by Arunmozhi](https://commons.wikimedia.org/wiki/File:PyQgis_Logo_Illustration.png), CC BY-SA 4.0 <https://creativecommons.org/licenses/by-sa/4.0>, via Wikimedia Commons.

### Related plugin

There is also a [plugin that allow to browse resources right into QGIS](https://guts.github.io/qgis-plugin-resource-browser/). [Don't miss it](https://plugins.qgis.org/plugins/pyqgis_resource_browser/)!

[Demonstration video of the QGIS plugin PyQGIS Resource Browser](https://user-images.githubusercontent.com/1596222/232868878-1134695b-5dd8-405e-96af-00a2856d4535.webm)

### Related contents

- blog posts/tutorials (in French :fr:):
    - [How to use embedded images in PyQGIS?](http://geotribu.fr/articles/2021/2021-01-19_pyqgis_utiliser_icones_integrees/)
    - [How to generate a table of embedded images in PyQGIS?](http://geotribu.fr/articles/2021/2021-02-02_pyqgis_previsualiser_images_integrees/)
- resources file in QGIS project: <https://github.com/qgis/QGIS/blob/master/images/images.qrc>
- Qt documentation: <https://doc.qt.io/qt-5/resources.html>

----

## Development

### Requirements

- Python 3.10+
- network connection authorized to github.com
- [Material for Mkdocs](https://squidfunk.github.io/mkdocs-material/)
- [dependencies for images processing listed on theme documentation](https://squidfunk.github.io/mkdocs-material/setup/dependencies/image-processing/). Typically, on Ubuntu:

    ```sh
    sudo apt install libcairo2-dev libfreetype6-dev libffi-dev libjpeg-dev libpng-dev libz-dev pngquant
    ```

### Setup

Typically on Ubuntu:

```sh
python3 -m venv .venv
source .venv/bin/activate
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

Copy the `README.MD` into the `docs` folder:

```sh
cp README.md docs/credits.md
```

Build:

```sh
mkdocs build
```

Serve locally:

```sh
mkdocs serve
```

Open your browser on: `http://localhost:8000`

----

## Deployment

The website is monthly regenerated and [deployed on GitHub Pages](https://geotribu.github.io/pyqgis-icons-cheatsheet/) using GitHub Actions. For more details, see the [deploy.yml workflow](https://github.com/geotribu/pyqgis-icons-cheatsheet/blob/51179754fca14ea993d84877714eeeb121cf4fcf/.github/workflows/deploy.yml).

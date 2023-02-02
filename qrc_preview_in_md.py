#! python3  # noqa: E265

"""
    Script to convert a remote QRC (Qt Resources Collection files) into a markdown table to \
        preview images. This example covers QGIS project.

    Author: Julien M. (https://twitter.com/geojulien)

    See:

        - tutorial (in French): https://static.geotribu.fr/articles/2021/2021-01-25_pyqgis_previsualiser_images_integrees
        - https://github.com/qgis/QGIS/blob/master/images/images.qrc
        - https://doc.qt.io/qt-5/resources.html
"""


# libraries
import xml.etree.ElementTree as ET
from pathlib import Path
from sys import exit
from urllib.parse import urljoin
from urllib.request import urlopen

# variables
resources_url = "https://raw.githubusercontent.com/qgis/QGIS/master/images/images.qrc"
base_path = "https://raw.githubusercontent.com/qgis/QGIS/master/"  # with backslash
pymd_attr_list = "{: loading=lazy width=100px }"

# parse file
tree = ET.parse(urlopen(resources_url))
root = tree.getroot()

# check if it's really a QRC file
if not root.tag == "RCC":
    exit(
        "{} doesn't seem to be a Qt Resources Collection file: {}. "
        "Please Chuck, check the given path 'resources_file`."
    )

# prepare markdown file
out_markdown = """---\ncomments:\n  - true\nhide:\n  - navigation\n---\n\n# QGIS embedded images\n\nRemember how to use it:\n\n```python\nfrom qgis.core import QgsApplication\nfrom qgis.PyQt.QtGui import QIcon, QPixmap\n```\n"""
md_table_header = (
    "| Preview | Using QgsApplication | QIcon/QPixmap |\n" "| ----------- | ------- | ------- |\n"
)
md_table_row_tpl = """| ![{}]({}){} | `#!python QIcon(QgsApplication.iconPath(":{}"))` | `#!python QIcon(":{}")`<br/>`QPixmap(":{}")` |\n"""

# iterate over resources
for prefix in root:
    if prefix.tag == "qresource" and "prefix" in prefix.attrib:
        # set prefix (= level 2 in markdown)
        prefix_name = prefix.attrib.get("prefix")[1:]
        out_markdown += "\n## {}\n".format(prefix_name.title())

        # iterate over files under prefix, after sorting them by filepath
        previous_subfolder = ""
        for binimg in sorted(prefix.findall("file"), key=lambda x: x.text.rsplit("/", 1)[0]):
            # build path to image
            img_path_abs = urljoin(base_path,  f"{prefix_name}/{binimg.text}")
            img_path_rel = Path(prefix_name, binimg.text)

            # use subfolder as markdown level 3
            if binimg.text.rsplit("/", 1)[0] != previous_subfolder:
                out_markdown += "\n### {}\n\n".format(binimg.text.rsplit("/", 1)[0])
                out_markdown += md_table_header
                previous_subfolder = binimg.text.rsplit("/", 1)[0]

            # add line for image
            out_markdown += md_table_row_tpl.format(
                img_path_rel.stem,
                img_path_abs,
                pymd_attr_list,
                img_path_rel.name,
                img_path_rel,
                img_path_rel,
            )

with Path("docs/index.md").open("w") as io_out:
    io_out.write(out_markdown)

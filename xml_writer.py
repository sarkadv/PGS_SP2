from xml.dom import minidom

from stats import *


class XMLWriter:
    def __init__(self, stats: Stats):
        self.__stats = stats

    def create_XML(self, output_file: str):
        root = minidom.Document()

        xml = root.createElement('root')
        root.appendChild(xml)

        productChild = root.createElement('product')
        productChild.setAttribute('name', 'test')

        xml.appendChild(productChild)

        xml_str = root.toprettyxml(indent="\t", encoding="utf-8")

        save_path_file = "test.xml"

        with open(save_path_file, "wb") as f:
            f.write(xml_str)

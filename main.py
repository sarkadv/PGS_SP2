from xml.dom import minidom
import os

root = minidom.Document()

xml = root.createElement('root')
root.appendChild(xml)

productChild = root.createElement('product')
productChild.setAttribute('name', 'Geeks for Geeks')

xml.appendChild(productChild)

xml_str = root.toprettyxml(indent="\t", encoding="utf-8")

save_path_file = "gfg.xml"

with open(save_path_file, "wb") as f:
    f.write(xml_str)

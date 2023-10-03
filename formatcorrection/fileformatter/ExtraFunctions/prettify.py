from xml.etree.ElementTree import Element, SubElement, Comment, tostring
from xml.dom import minidom
import lxml.etree as ET

from xml.etree import ElementTree

tree = ET.parse('formatcorrection\\fileformatter\\pool\\formatted_xmlfile.xml')
root = ET.tostring(tree)
print(root)
reparsed = minidom.parseString(root)
print(reparsed.toprettyxml(indent="\t"))
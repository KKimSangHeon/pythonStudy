import xml.etree.ElementTree as ET
import datetime

doc = ET.parse('country_data.xml')
root = doc.getroot()

print(root[0][2].text)

# for child in root:
   # print(child.tag, child.attrib)

# for child in root.iter("aa"):
   # print(child.tag, child.attrib)


for rank in root.iter("rank"):
    new_rank = int(rank.text)+1
    rank.text = str(new_rank)
    rank.attrib["updated"] = "yes"

for country in root.findall('aa'):
    rank = int(country.find('rank').text)
    if rank > 50:
        root.remove(country)


for country in root.findall('country'):
    e = datetime.datetime.now()
    last_updated = ET.Element("last_updated")
    last_updated.text = str(e)
    country.append(last_updated)


def auto_indent(elem, level = 0):
    indent = "\n"+level * " "

    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = indent+" "
        if not elem.tail or not elem.tail.strip():
            elem.tail = indent
        for elem in elem:
            auto_indent(elem, level+1)
        if not elem.tail or not elem.tail.strip():
            elem.tail = indent
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = indent

auto_indent(root)
ET.dump(root)


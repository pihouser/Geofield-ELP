import yaml
import xml.etree.ElementTree as xml_tree

with open('feed.yaml', 'r') as file:
    yaml_data = yaml.safe_load(file)

    rss_element = xml_tree.Element('rss', {'version':'2.0',
        'feed xmlns':'http://www.w3.org/2005/Atom' ,
        'xmlns:georss':'http://www.georss.org/georss'})

channel_element = xml_tree.SubElement(rss_element, 'channel')

xml_tree.SubElement(channel_element, 'title').text = yaml_data['title']

output_tree = xml_tree.ElementTree(rss_element)
output_tree.write('quakeDaily.xml', encoding='UTF-8', xml_declaration=True)

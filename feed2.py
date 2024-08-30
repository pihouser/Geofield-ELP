import yaml
import xml.etree.ElementTree as xml_tree

with open('buda.yaml', 'r') as file:

    yaml_data = yaml.safe_load(file)

    xml_element = xml_tree.Element('xml', {'version':'1.0'})
  
channel_element = xml_tree.SubElement(xml_element, 'channel')
xml_tree.SubElement(channel_element, 'Title').text = yaml_data['Title']
xml_tree.SubElement(channel_element, 'Author').text = yaml_data['Author']

for ObjectPropertyAssertion in yaml_data['ObjectPropertyAssertion']:
    item_element = xml_tree.SubElement(channel_element, 'ObjectPropertyAssertion')
    xml_tree.SubElement(item_element, 'NamedIndividual').text = ObjectPropertyAssertion['NamedIndividual']
    xml_tree.SubElement(item_element, 'NamedIndividual').text = ObjectPropertyAssertion['NamedIndividual']

output_tree = xml_tree.ElementTree(xml_element)
output_tree.write('budaMembers.xml', encoding='UTF-8', xml_declaration=True)

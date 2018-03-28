#!/usr/bin/env python

from bioc import BioCXMLReader
from bioc import BioCJSONReader
from bioc import BioCXMLWriter
from bioc import BioCJSONWriter

test_xml = '../test_input/example_input.xml'
test_json = '../test_input/example_input.json'
dtd_file = '../test_input/BioC.dtd'


def main():
    # Read XML, write JSON.
    xml_reader = BioCXMLReader(test_xml, dtd_valid_file=dtd_file)
    xml_reader.read()

    json_writer = BioCJSONWriter()
    json_writer.collection = xml_reader.collection
    json_writer.write('output_bioc.json', indent=2)
    print(json_writer)

    # Read JSON, write XML.
    json_reader = BioCJSONReader(test_json)
    json_reader.read()

    xml_writer = BioCXMLWriter('output_bioc.xml', xml_reader.collection)
    xml_writer.write()
    print(xml_writer)


if __name__ == '__main__':
    main()

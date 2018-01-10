#!/usr/bin/env python

from bioc import BioCReader
from bioc import BioCXMLWriter
from bioc import BioCJSONWriter

test_file = '../test_input/example_input.xml'
dtd_file = '../test_input/BioC.dtd'


def main():
    bioc_reader = BioCReader(test_file, dtd_valid_file=dtd_file)
    bioc_reader.read()
    '''
    sentences = bioc_reader.collection.documents[0].passages[0].sentences
    for sentence in sentences:
        print sentence.offset
    '''

    bioc_xml_writer = BioCXMLWriter('output_bioc.xml', bioc_reader.collection)
    bioc_xml_writer.write()
    print(bioc_xml_writer)

    bioc_json_writer = BioCJSONWriter()
    bioc_json_writer.collection = bioc_reader.collection
    bioc_json_writer.write('output_bioc.json', indent=2)
    print(bioc_json_writer)


if __name__ == '__main__':
    main()

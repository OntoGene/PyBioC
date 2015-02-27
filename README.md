#PyBioC

**[PyBioC][1] is a native python library to deal with BioCreative XML data,
i. e. to read from and to write to it.**

More information about BioC available [online][2].

----------

##Usage:

Two example programs, test_read+write.py and stemming.py are shipped in the `src/` folder.

- `test_read+write.py` shows the very
basic reading and writing capability
of the  library.
- `stemming.py` uses the Python Natural
Language Toolkit (NLTK) library to 
manipulate a BioC XML file read in
before; it then tokenizes the
corresponding text, does stemming on
the tokens and transforms the
manipulated PyBioC objects back to
valid BioC XML format.


[1]: http://bioc.sourceforge.net/
[2]: http://bioc.sourceforge.net/
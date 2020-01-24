# XML using Perl
{id: perl-xml}

## XML sample data
{id: xml-data}

{aside}
We are going to use the following XML file
and will try to answer te various questions that are listed
in the comment at the top of the file.
{/aside}

![](examples/xml/data.xml)


## XML Definitions
{id: xml-definition}

* Tags, attributes
* Well formed

```
  <tag>text</tag>
```

or an empty element:

```
  <tag />
```

* Valid XML (DTD, XML Schema, RelexNG, Schematron)
* Namespaces, Entity references,


## XML processing modes
{id: xml-processing-modes}

* DOM - build an in-memory representation of the XML (tree)
* SAX - process the XML chunk-by-chunk (stream)


## XML::Simple
{id: xml-simple}

Let's see some of the parameters controlling the way XML is read
into memory by XML::Simple.

{aside}
XML::Simple is, well, relatively simple but it can still be used in a number of ways.
The most straight forward way is to import the XMLin function, and pass a filename
to it or a scalar with XML data in it. In addition the XMLin subroutine accepts several
options. Two of them are the most important:
ForceArray and KeyAttr. Also interesting is KeepRoot.

ForceArray defaults to 0
KeyAttr defaults to ['name', 'key', 'id']
KeepRoot defaults to 0

'Array folding' feature is controlled by KeyAttr
{/aside}

![](examples/xml/xml_simple_intro.pl)

{aside}
Without any options this will generate something that is apparently a mess. This is
caused by the fact that KeyAttr is trying to be nice and uses the value of the 'name'
tag and the 'id' attribute as the keys to the hash it is generating.
{/aside}

![](examples/xml/xml_simple.pl)


## XML::Simple dumped
{id: xml-simple-data-dumped}

```
$VAR1 = {
          'country' => {
                       'Israel' => {
                                   'currency' => 'NIS',
                                   'languages' => {
                                                  'language' => [
                                                                'Hebrew',
                                                                'English',
                                                                'Arabic',
                                                                'Russian'
                                                              ]
                                                },
                                   'id' => '2'
                                 },
                       'Hungary' => {
                                    'currency' => 'HUF',
                                    'languages' => {
                                                   'language' => 'Hungarian'
                                                 },
                                    'id' => '3'
                                  },
                       'USA' => {
                                'currency' => 'USD',
                                'languages' => {
                                               'language' => [
                                                             'English',
                                                             'Spanish'
                                                           ]
                                             },
                                'id' => '1'
                              }
                     }
        };
```


## XML::Simple processing
{id: xml-simple-process}
![](examples/xml/xml_simple_extract.pl)



## XML::Parser
{id: xml-parser}


Originally written by Larry Wall, using expat written by James Clark
allow several styles of parsing such as Stream, Object, Tree.




## XML::Parser tree
{id: xml-parser-tree}
![](examples/xml/xml_parser_tree.pl)

```
Run the code and see what is dumped out

Read the documentation of XML::Parser (search Tree)
```


## XML::Parser tree results
{id: xml-parser-tree-results}

```
$VAR1 =
[
    'data',
    [
        {},
        0,
        '',
        'country',
        [
            {'id' => '1'},
            0,
            '',
            'name',
            [
                {},
                0,
                'USA'
            ],
            0,
            '',
            'languages',
            [
                {},
                0,
                '',
                'language',
                [
                    {},
                    0,
                    'English'
                ],
                0,
                '',
                'language',
                [
                    {},
                    0,
                    'Spanish'
                ],
                0,
                ''
            ],
            0,
            '',
            'currency',
            [
                {},
                0,
                'USD'
            ],
            0,
            ''
        ],
        0,
        '',
        'country',
        [
            {'id' => '2'},
            0,
            '',
            'name',[{},0,'Israel'],....
        ],
        0,
        '',
        'country',
        [
            {'id' => '3'},
            0,
            '',
            'name',[{},0,'Hungary'],....
        ],
    ]
];
```


## XML::Parser
{id: xml-parser-tree-process}
![](examples/xml/xml_parser_tree_process.pl)


## XML::LibXML
{id: xml-libxml}

```
Low level library, Perl binding to libxml2 supports the standard
XML processing mode called Document Object Mode (DOM).
```
![](examples/xml/libxml.pl)

```
Other Node types (taken from the source code)

XML_COMMENT_NODE
XML_TEXT_NODE
XML_CDATA_SECTION_NODE
XML_ELEMENT_NODE
XML_ENTITY_REF_NODE
XML_DOCUMENT_NODE
XML_HTML_DOCUMENT_NODE
XML_DOCUMENT_FRAG_NODE
XML_PI_NODE
XML_XINCLUDE_START
XML_XINCLUDE_END
XML_DTD_NODE
```


## XML::XPath
{id: xml-xpath}

```
Built on XML::Parser
```
![](examples/xml/xpath.pl)


## XML::Twig
{id: xml-twig}

```
```
![](examples/xml/twig.pl)
![](examples/xml/twig1.pl)


## XML::Writer
{id: xml-writer}

```
Close to handwriting of the XML but can also check well formedness.
```
![](examples/xml/xml_writer.pl)


## XML::Dumper
{id: xml-dumper}

```
```
![](examples/xml/xml_dumper.pl)


## Exercise: parse glade.xml
{id: xml-exercise-parse-gladexml}

![](examples/xml/entry.glade)

```
Given the XML file created by Glade write the following functions:

my @names   = get_all_widget_names(); # all the names
my @widgets = get_all_widges();       # all the objects
my $widget  = get_widget($name);      # an object representing the widget
$widget->get_handler($name);          # name of the handler function
$widget->get_property($name);
$widget->set_property($name, $value);
```


## DTD validation
{id: xml-dtd-validation}

```
Using XML::LibXML;

XML::Checker
```


## Specialized XML modules
{id: specialized-xml-modules}

```
SOAP::Lite
Gtk2::GladeXML
XML::RSS
XML::RSS::SimpleGen
XML::Atom
XML::Atom::SimpleFeed
```


## Resources
{id: xml-resources}

```
See CPAN for uncounted number of XML related modules.

The perl-xml mailing list
http://aspn.activestate.com/ASPN/Mail/Browse/Threaded/perl-xml

http://xmltwig.com/

http://perl-xml.sourceforge.net/

http://www.xml.com

"Perl and XML" (first ed) By Erik T. Ray, Jason McIntosh, Published by O'Reilly

Many of our examples are taken from these places either directly or
after some transformation.
```






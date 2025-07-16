# XML::Simple

Let's see some of the parameters controlling the way XML is read
into memory by XML::Simple.

XML::Simple is, well, relatively simple but it can still be used in a number of ways.
The most straight forward way is to import the XMLin function, and pass a filename
to it or a scalar with XML data in it. In addition the XMLin subroutine accepts several
options. Two of them are the most important:
ForceArray and KeyAttr. Also interesting is KeepRoot.

ForceArray defaults to 0
KeyAttr defaults to ['name', 'key', 'id']
KeepRoot defaults to 0

'Array folding' feature is controlled by KeyAttr

{% embed include file="src/examples/xml/xml_simple_intro.pl" %}

Without any options this will generate something that is apparently a mess. This is
caused by the fact that KeyAttr is trying to be nice and uses the value of the 'name'
tag and the 'id' attribute as the keys to the hash it is generating.

{% embed include file="src/examples/xml/xml_simple.pl" %}



# XML
{id: xml}

## XML Data
{id: xml-data}
{i: xml}
![](examples/xml/data.xml)


## Expat - Callbacks
{id: xml-expat-callbacks}
{i: xml.parsers.expat}
![](examples/xml/callbacks.py)


## XML DOM - Document Object Model
{id: xml-dom}
![](examples/xml/dom.py)

```
main

name:  person
id:  1
name:  person
id:  3

email home moo@zorghome.com
email work moo@work.com
```


<a href="http://docs.python.org/2/library/xml.dom.html">xml.dom</a>
<a href="http://docs.python.org/2/library/xml.dom.minidom.html">xml.dom.minidom</a>




## XML SAX - Simple API for XML
{id: xml-sax}
![](examples/xml/sax.py)

```
start (u'main', {})
start (u'person', {u'id': u'1'})
start (u'fname', {})
text Foo
end fname
start (u'lname', {})
text Bar
end lname
end person
start (u'person', {u'id': u'3'})
start (u'fname', {})
text Moo
end fname
start (u'lname', {})
text Zorg
end lname
start (u'email', {u'id': u'home'})
text moo@zorghome.com
end email
start (u'email', {u'id': u'work'})
text moo@work.com
end email
end person
end main
```


<a href="http://docs.python.org/2/library/xml.sax.html">xml.sax</a>
<a href="http://docs.python.org/2/library/xml.sax.handler.html">xml.sax.hanldler</a>
<a href="http://docs.python.org/2/library/xml.sax.reader.html">xml.sax.reader</a>




## SAX collect
{id: xml-sax-collect}
![](examples/xml/sax_collect.py)

```
End name:  fname
End name:  lname
End name:  person
End name:  fname
End name:  lname
End name:  email
End name:  email
End name:  person
End name:  main
[{'text': u'moo@zorghome.com', 'name': u'email', 'attr': {u'id': u'home'}},
 {'text': u'moo@work.com', 'name': u'email', 'attr': {u'id': u'work'}}]
```


## XML elementtree
{id: xml-elemttree}
![](examples/xml/tree.py)

```
main
{'id': '1'}
{'id': '3'}

{'id': 'home'} moo@zorghome.com
{'id': 'work'} moo@work.com

email {'id': 'home'}
```


<a href="http://docs.python.org/2/library/xml.etree.elementtree.html">xml.etree.elementtree</a>






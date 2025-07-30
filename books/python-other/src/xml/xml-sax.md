# XML SAX - Simple API for XML

{% embed include file="src/examples/xml/sax.py" %}

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

* [xml.sax](http://docs.python.org/library/xml.sax.html)
* [xml.sax.hanldler](http://docs.python.org/library/xml.sax.handler.html)
* [xml.sax.reader](http://docs.python.org/library/xml.sax.reader.html)



# Monostate (Borg)

* [Monostate Pattern](http://c2.com/cgi/wiki?MonostatePattern)

```
class Monostate(object):
    _shared_state = {}
    def __new__(cls, *a, **kw):
        obj = super(Monostate, cls).__new__(*a, **kw)
        obj.__dict__ = _shared_state
        return obj

class Foo(Monostate) pass
class Bar(Foo) pass
f = Foo()
b = Bar()
```


Better than singleton, data overriding to the rescue:
But what if two calls to the constructor provide different initial data?



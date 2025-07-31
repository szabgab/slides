# Singleton

```
   class Singleton(object):
   def __new__(cls, *a, **kw):
       if not hasattr(cls, '_inst'):
           cls._inst = super(Singleton, cls).__new__(*a, **kw)
       return cls._inst
```

the problem


```
   class Foo(Singleton): pass
   class Bar(Foo): pass
   f = Foo()
   b = Bar()
   # what class is b now? is that a Bar or a Foo instance?
```




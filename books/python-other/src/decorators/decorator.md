# Decorator

* @

* A function that changes the behaviour of other functions.
* The input of a decorator is a function.
* The returned value of a decorator is a modified version of the same function.


```
from some_module import some_decorator

@some_decorator
def f(...):
    ...
```

```
def f(...):
    ...
```

```
f = some_decorator(f)
```



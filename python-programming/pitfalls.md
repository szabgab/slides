# Python Pitfalls
{id: pitfalls}

## Reuse of existing module name
{id: reuse-module-name}
![](examples/pitfalls/random.py)

```
$ python examples/pitfalls/random.py

Traceback (most recent call last):
  File "examples/pitfalls/random.py", line 1, in <module>
    import random
  File ".../examples/pitfalls/random.py", line 3, in <module>
    print(random.random())
TypeError: 'module' object is not callable
```

* Write an example to use random number and call your example **number.py**
* Same with any other module name.
* Lack of multi-level namespaces
* Solution: user longer names. Maybe with project specific names.



## Use the same name more than once
{id: overwrite-names}
![](examples/pitfalls/corp.py)

```
$ python examples/pitfalls/corp.py

19
Traceback (most recent call last):
  File "examples/pitfalls/corp.py", line 19, in <module>
    print(c.total())
TypeError: 'int' object is not callable
```


## Compare string and number
{id: compare-string-and-number}
![](examples/pitfalls/compare.py)

Python 2 - compares them based on the type of values (wat?)


```
$ python examples/pitfalls/compare.py
False
True
```

Python 3 - throws exception as expected.


```
$ python3 examples/pitfalls/compare.py
Traceback (most recent call last):
  File "examples/pitfalls/compare.py", line 4, in <module>
    print(x > y)
TypeError: unorderable types: int() > str()
```


## Compare different types
{id: compare-different-types-in-python3}
![](examples/pitfalls/compare_equal.py)

In both Python 2 and Pyhton 3 these return **False**

![](examples/pitfalls/compare_input.py)

Will never match. Even if user types in 42. - Hard to debug and understand as there is no error.




## Sort mixed data
{id: sort-mixed-data}
![](examples/pitfalls/sort.py)

In Python 2 it "works" is some strange way.


```
$ python examples/pitfalls/sort.py
[10, '1 foo', 42, '4 bar']
[10, 42, '1 foo', '4 bar']
```

In Python 3 in **correctly** throws an exception.


```
air:python gabor$ python3  examples/pitfalls/sort.py
[10, '1 foo', 42, '4 bar']
Traceback (most recent call last):
  File "examples/pitfalls/sort.py", line 5, in <module>
    mixed.sort()
TypeError: unorderable types: str() < int()
```





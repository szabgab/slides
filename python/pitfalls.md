# Python Pitfalls
{id: pitfalls}

## Reuse of existing module name
{id: reuse-module-name}

![](examples/pitfalls/random.py)

```
$ python examples/pitfalls/random.py
```
![](examples/pitfalls/random.out)

* Write an example to use random number and call your example **number.py**
* Same with any other module name.
* Lack of multi-level namespaces
* Solution: user longer names. Maybe with project specific names.


## Use the same name more than once
{id: overwrite-names}

![](examples/pitfalls/corp.py)

```
$ python examples/pitfalls/corp.py
```

![](examples/pitfalls/corp.out)


## Compare string and number
{id: compare-string-and-number}

![](examples/pitfalls/compare.py)

Python 2 - compares them based on the type of values (wat?)

```
$ python examples/pitfalls/compare.py
```

![](examples/pitfalls/compare2.out)

Python 3 - throws exception as expected.


```
$ python3 examples/pitfalls/compare.py
```

![](examples/pitfalls/compare3.out)


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
```

![](examples/pitfalls/sort2.out)

In Python 3 in **correctly** throws an exception.


```
air:python gabor$ python3  examples/pitfalls/sort.py
```
![](examples/pitfalls/sort3.out)


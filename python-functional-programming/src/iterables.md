# Iterators (Iterables)

You already know that there are all kinds of objects in Python that you can iterate over using the **for-in** construct.
For example, you can iterate over the characters of a string, or the elements of a list, or whatever **range()** returns.
You can also iterate over the lines of a file
and you have probably seen the **for in** construct in other cases as well. The objects that can be iterated over are collectively called
[iterables](https://docs.python.org/glossary.html#term-iterable).
You can do all kind of interesting things on such **iterables**. We'll see a few now.

* There are several data types that we can iterate over using the **for ... in ...** construct. For example, strings, lists, tuples, filehandles, and range:

## string

We can iterate over the "elements" of a string that are the characters. We can also print the whole string.

{% embed include file="src/examples/functional/iterable_string.py" %}

**Output:**

{% embed include file="src/examples/functional/iterable_string.out" %}


## list

We can iterate over the elements of a list. We can also print the whole list at once.

{% embed include file="src/examples/functional/iterable_list.py" %}

**Output:**

{% embed include file="src/examples/functional/iterable_list.out" %}

## tuple

We can iterate over the elements of a tuple. We can also print the whole tuple at once.

{% embed include file="src/examples/functional/iterable_tuple.py" %}

**Output:**

{% embed include file="src/examples/functional/iterable_tuple.out" %}


## filehandle

We can iterate over a filehandle. On each iteration we'll get one line from the file.

{% embed include file="src/examples/functional/iterable_fh.py" %}

Running this program will print itself.

We can also print the filehandle: `print(fh)`, but the output will be:

```
<_io.TextIOWrapper name='iterable_fh.py' mode='r' encoding='UTF-8'>
```

not the content of the file.

So the "thing" that the `open` function returned is iterable, but it is different from the previous 3 types.

## range

The `range` function returns something, that we can use in a **for-in** loop to iterate over and we'll get the expected numbers.

However, if we print the value that we got back from the `range` function it looks strange. It looks exactly as we called it.
This is the representation of the `range` object.

Unlike in Python 2, here in Python 3 the `range` function does **not** return a list of numbers.
It returns an object that allows us to iterate over the numbers, but it does not hold the numbers.

{% embed include file="src/examples/functional/iterable_range.py" %}

**Output:**

{% embed include file="src/examples/functional/iterable_range.out" %}

`range` is interesting. We are going to take a closer look in the next few pages.


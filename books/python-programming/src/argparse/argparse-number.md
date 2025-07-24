# Convert to integer


{% embed include file="src/examples/argparse/argparse_type.py" %}

```
$ argparse_type.py abc
usage: argparse_type.py [-h] number
argparse_type.py: error: argument number: invalid int value: 'abc'
```


We got a much better error message as argparse already found out the
argument was a string and not a number as expected.

```
$ python argparse_type.py 3.14
usage: argparse_type.py [-h] number
argparse_type.py: error: argument number: invalid int value: '3.14'
```

```
$ argparse_type.py 23
529
```

The `type` parameter can be used to define the type restriction
and type conversion of the attributes.




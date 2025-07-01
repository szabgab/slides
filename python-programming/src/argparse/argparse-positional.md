# Positional argument

{% embed include file="src/examples/argparse/argparse_positional.py" %}

```
$ python argparse_positional.py
usage: argparse_positional.py [-h] name
argparse_positional.py: error: too few arguments
```

```
$ python argparse_positional.py -h
usage: argparse_positional.py [-h] name

positional arguments:
  name        your full name

optional arguments:
  -h, --help  show this help message and exit
```


```
$ python argparse_positional.py Foo
Foo
```


```
$ python argparse_positional.py Foo Bar
usage: argparse_positional.py [-h] name
argparse_positional.py: error: unrecognized arguments: Bar
```


```
$ python argparse_positional.py "Foo Bar"
Foo Bar
```



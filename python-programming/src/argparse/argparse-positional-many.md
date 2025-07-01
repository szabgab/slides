# Many positional argument

{% embed include file="src/examples/argparse/argparse_positional_many.py" %}

```
$ python argparse_positional_many.py 
usage: argparse_positional_many.py [-h] files [files ...]
argparse_positional_many.py: error: too few arguments
```


```
air:python gabor$ python argparse_positional_many.py a.txt b.txt
['a.txt', 'b.txt']
```



# Basic usage of argparse


Setting up the argparse already has some (little) added value.

{% embed include file="src/examples/argparse/argparse_basic.py" %}



Running the script without any parameter will not interfere...


```
$ python argparse_basic.py
the code...
```



If the user tries to pass some parameters on the command line, the argparse will
print an error message and stop the execution.


```
$ python argparse_basic.py foo
usage: argparse_basic.py [-h]
argparse_basic.py: error: unrecognized arguments: foo
```

```
$ python argparse_basic.py -h
usage: argparse_basic.py [-h]

optional arguments:
  -h, --help  show this help message and exit
```


The minimal set up of the argparse class already provides a (minimally) useful help message.




# Argparse xor - mutual exlucise - only one - exactly one


{% embed include file="src/examples/argparse/argparse_xor.py" %}

```
$ python argparse_xor.py
usage: argparse_xor.py [-h] [--name NAME] (--add | --remove)
argparse_xor.py: error: one of the arguments --add --remove is required

$ python argparse_xor.py --add
$ python argparse_xor.py --remove

$ python argparse_xor.py --add --remove
usage: argparse_xor.py [-h] [--name NAME] (--add | --remove)
argparse_xor.py: error: argument --remove: not allowed with argument --add


$ python argparse_xor.py --help
usage: argparse_xor.py [-h] [--name NAME] (--add | --remove)

optional arguments:
  -h, --help   show this help message and exit
  --name NAME
  --add
  --remove
```



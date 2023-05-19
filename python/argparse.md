# Command line arguments with argparse
{id: argparse}


## Command line arguments
{id: argparse-command-line-arguments}

```
myprog.py  data1.xls data2.xls
myprog.py --input data1.xls --output data2.xls
```

![](examples/argparse/argparse_two_filenames.py)


## Modules to handle the command line
{id: command-line-modules}
{i: argparse}

You would like to allow the user to pass arguments on the command line. For example:


```
myprog.py server_name name True True

myprog.py --machine server_name --test name --verbose --debug
myprog.py -v -d
myprog.py -vd
myprog.py -dv
myprog.py -v -d -m server_name
myprog.py -vdm server_name
myprog.py file1 file2 file3
myprog.py file1 file2 file3
myprog.py --machine server_name --debug file1 file2 file3
myprog.py file1 file2 file3 --machine server_name --debug
```

* [sys.argv](http://docs.python.org/library/sys.html)  manual parsing?
* [argparse](http://docs.python.org/library/argparse.html)



## argparse
{id: argparse-full}
![](examples/argparse/argparse_full.py)


## Basic usage of argparse
{id: argparse-basic}

Setting up the argparse already has some (little) added value.

![](examples/argparse/argparse_basic.py)

{aside}

Running the script without any parameter will not interfere...
{/aside}

```
$ python argparse_basic.py
the code...
```

{aside}

If the user tries to pass some parameters on the command line, the argparse will
print an error message and stop the execution.
{/aside}

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




## Positional argument
{id: argparse-positional}
![](examples/argparse/argparse_positional.py)

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


## Many positional argument
{id: argparse-positional-many}
![](examples/argparse/argparse_positional_many.py)

```
$ python argparse_positional_many.py 
usage: argparse_positional_many.py [-h] files [files ...]
argparse_positional_many.py: error: too few arguments
```


```
air:python gabor$ python argparse_positional_many.py a.txt b.txt
['a.txt', 'b.txt']
```


## Convert to integers
{id: argparse-type}
![](examples/argparse/argparse_number.py)

```
$ python argparse_number.py abc
```
![](examples/argparse/argparse_number_abc.out)


Trying to the argument received from the command
line as an integer, we get a TypeError. The same would happen
even if a number was passed, but you could call `int()`
on the parameter to convert to an integer.
However there is a better solution.



The same with the following


```
$ python argparse_number.py 23
```
![](examples/argparse/argparse_number_23.out)


## Convert to integer
{id: argparse-number}

![](examples/argparse/argparse_type.py)

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



## Named arguments
{id: argparse-named}
![](examples/argparse/argparse_named.py)

**python argparse_named.py --color Blue**


```
Blue
```

**python argparse_named.py**


```
None
```


Named parameters are optional by default. You can pass the
`required=True` parameter to make them required.


## Boolean Flags
{id: argparse-boolean}

![](examples/argparse/argparse_boolean.py)

**python argparse_boolean.py --color Blue --verbose**


```
Blue
True
```

**python argparse_boolean.py**


```
None
False
```


## Short names
{id: argparse-shortnames}

![](examples/argparse/argparse_shortname.py)

```
python argparse_shortname.py -c Blue -v
python argparse_shortname.py -vc Blue
```


## argparse print help explicitely
{id: argparse-print-help}
{i: print_help}

![](examples/argparse/argparse_print_help.py)

## Argparse xor - mutual exlucise - only one - exactly one
{id: argparse-xor}

![](examples/argparse/argparse_xor.py)

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

## Argparse argument with default and optional value
{id: argparse-with-default-and-optional-value}
{i: nargs}
{i: const}

* Instead of `default` we use the `const` parameter here
* We tell argparse that the value of the parameter is optional by `nargs='?'`

![](examples/argparse/argument_with_optional_value.py)

```
$ python argument_with_optional_value.py
None
```

```
$ python argument_with_optional_value.py --level
10
```

```
$ python argument_with_optional_value.py --level 20
20
```

## Conditional required parameter with argparse
{id: argparse-conditional-required-parameter}

![](examples/argparse/conditional_required_arguments.py)

## Exercise: Command line parameters
{id: exercise-argparse}

Take the code from the color selector exercise in the files section and change it so
the user can supply the name of the file where the colors are listed using the
`--file filename` option.

If the user supplies an incorrect color name (which is not listed among the accepted colors)
give an error message and stop execution.

Allow the user to supply a flag called `--force` that will
override the color-name-validity checking and will allow any color name.

## Exercise: argparse positional and named
{id: exercise-argparse-positional-and-named}

Create a script that can accept any number of filenames, the named parameter `--machine` and the flag `--verbose`.
Like this:

```
python ex.py file1 file2 file3 --machine MACHINE --verbose
```



# Command line arguments with argparse
{id: argparse}

## Modules to handle the command line
{id: command-line-modules}
{i: argparse}

You would like to allow the user to pass arguments on the command line. For example:


```
myprog.py --machine server_name --test name --verbose --debug
myprog.py -v -d
myprog.py -vd
myprog.py file1 file2 file3
```

* [sys.argv](http://docs.python.org/library/sys.html)  manual parsing?
* [optparse](http://docs.python.org/library/optparse.html) (deprecated)
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
even if a number was passed, but you could call <command>int()</command>
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
$ argparse_type.py 23
529
```

The <emp>type</emp> parameter can be used to define the type restriction
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
<command>required=True</command> parameter to make them required.




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

**python argparse_shortname.py -c Blue -v**


**python argparse_shortname.py -vc Blue**




## Exercise: Command line parameters
{id: exercise-argparse}


Take the code from the color selector exercise in the files section and change it so
the user can supply the name of the file where the colors are listed using the
<command>--file filename</command> option.




If the user supplies an incorrect color name (which is not listed among the accepted colors)
give an error message and stop execution.




Allow the user to supply a flag called <command>--force</command> that will
override the color-name-validity checking and will allow any color name.








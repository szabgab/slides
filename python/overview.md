# Overview of Python syntax
{id: overview}

## Scalars
{id: overview-scalars}

* Numbers (int, float)
* Strings (str)
* Boolean

## Numbers
{id: overview-numbers}

![](examples/overview/numbers.py)

## Strings
{id: overview-strings}

![](examples/overview/strings.py)


```
var[3]
var[3:7]

len(var)

ord(char)
chr(number)

var.title()
var.upper()
var.lower()
var.index(sub)
var.rindex(sub)
var.find(sub)

short in long
if short in long:
    print('in')


':'.join(list_of_strings)
some_string.split(':')
```

## int - float - string conversion
{id: overview-conversion}

```
int()
float()
str()
```

## Booleans
{id: overview-booleans}

```
True
False
```


## Lists
{id: overview-lists}

```
fruits = ['apple', 'banana', 'peach', 'pear']
fruits[2]
fruits[1:3]
fruits[::2]
fruits[:]

len(fruits)

import copy
copy.copy(fruits)     # shallow copy
copy.deepcopy(fruits)

element in some_list
if element in some_list:
    print('in')

fruits.index(sub)  # return location or raises Exception

fruits.insert(location, anothe_fruit)
fruits.append(another_fruit)
fruits.remove(some_fruit)   # remove by value
fruits.pop(location)        # remove by location
list()

fruits.sort()
sorted(fruits)
```

## Queue and Stack
{id: overview-queue-and-stack}

Stack:

```
append
pop
```

Queue:

```
append
pop(0)
```


```
from collections import deque
```

Stack

```
fruits.append(...)
fruits.pop()
```

Queue

```
fruits = deque()
fruits.append(...)
fruits.popleft()
```

## Dictionaries
{id: overview-dictionaries}

## Tuples
{id: overview-tuples}

"inmutable list"

```
tuple()
fruits = ('apple', 'banana', 'peach')
```

## Sets
{id: overview-sets}

```
set()
set(some_list)
fruits = {'apple', 'banana', 'peach'}
```

## I/O
{id: overview-io}

```
print(var)
print(var, end=" ", sep="")
```

## STDIN - Standard input
{id: overview-stdin}

```
input("Some question: ")
```


## CLI
{id: overview-cli}

```
sys.argv
argparse
```

## Control flow
{id: overview-control-flow}

* Loops
* Conditionals
* Boolean operators
* Conditional (ternary) operator
* Exceptions

## While - Loops
{id: overview-while-loops}

```
while cond:
    pass

break

continue
```

## For - Loops
{id: overview-for-loops}


```
for var in some_string:
    print(var)

for var in range(3, 15, 2):
    print(var)

for var in some_list:
    print(var)

for var in some_iterable:
    print(var)

for var in some_iterable:
    print(var)
else:
    print("finished iterating")
```



## Conditionals
{id: overview-conditionals}

```
if cond1:
    pass
elif cond1:
    pass
else:
    pass
```

## Comparision operators
{id: overview-comparision-operators}

```
==
!=
<
<=
>=
>
```

## Boolean operators
{id: overview-boolean-operators}

```
and
or
not
```


## The conditional (ternary) operator
{id: overview-ternary-operator}

```
result = this if condition else that
```

## Random Values
{id: random-values}

```
import random
random.seed(42)
random.random()
random.randrange(1, 7)
random.choice(values)
random.sample(values)
```

## Math
{id: overview-math}

```
import math
math.pi
math.sin()
```

## Exceptions
{id: overview-exceptions}


```
raise Exception("Some text")
raise ValueError("Some text")
```

```
try:
    # Risky code
except Exception as err:
    # Handle exception



## Files
{id: overview-files}

(Plain text, CSV, Excel, JSON, YAML)

## Functions
{id: overview-functions}


## Modules
{id: overview-modules}




bytes

Exception handling

Flake8
Pylint
assert


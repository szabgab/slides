# Python types at PyWeb 2024.12
{id: python-types-at-pyweb-2024-12}

## The Answer
{id: python-types-at-pyweb-2024-12-answer}

![](examples/python-types-at-pyweb-2024-12/answer.py)

{aside}
Why would anyone write such obviously incorrect code?
{/aside}

## Add
{id: python-types-at-pyweb-2024-12-add}

What is the result of this code in Perl / Python / Rust?

![](examples/python-types-at-pyweb-2024-12/add.rs)

![](examples/python-types-at-pyweb-2024-12/add.py)

![](examples/python-types-at-pyweb-2024-12/add.pl)

```
rustc add.rs
```

{aside}
* The Rust code will have a compilation error.

* The Python code will have a runtime exception.

* The Perl code will print the correct answer: 42.


Howeever, in these example the problem is in-front of us. We can easily see it.
{/aside}

## Add in function
{id: python-types-at-pyweb-2024-12-add-in-function}

![](examples/python-types-at-pyweb-2024-12/function.rs)

![](examples/python-types-at-pyweb-2024-12/function.py)

![](examples/python-types-at-pyweb-2024-12/function.pl)

{aside}
Much less obvious if we are calling a function with parameters that are not the correct type.

The result is the same as in the previous example.
{/aside}

## Shift-left
{id: python-types-at-pyweb-2024-12-shift-left}

* Rust is the shift-left language noticing bugs earlier in the development process.
* How can we get Python to also complain earlier?

## Function with type annotation
{id: python-types-at-pyweb-2024-12-add-in-function-with-type-annotation}

* We can add type-annotations to the function parameters and even to the return value.

![](examples/python-types-at-pyweb-2024-12/function_with_type.py)

* However, Python will disregard these type-annotations and we still get a run-time exception.

## Use mypy
{id: python-types-at-pyweb-2024-12-mypy}

* Use some external tool [mypy](https://www.mypy-lang.org/) to check the types in your code. (Are there any other tools looking at the type-annotations?)

```
$ mypy function_with_type.py

function_with_type.py:7: error: Argument 1 to "add" has incompatible type "str"; expected "int"  [arg-type]
Found 1 error in 1 file (checked 1 source file)
```


```
$ mypy answer.py

answer.py:2:15: error: Incompatible types in assignment (expression has type "int", variable has type "str")  [assignment]
Found 1 error in 1 file (checked 1 source file)
```


## Define the type of variables
{id: python-types-at-pyweb-2024-12-type-of-variables}

![](examples/python-types-at-pyweb-2024-12/variable_and_function.py)

```
$ mypy variable_and_function.py
variable_and_function.py:7:15: error: Incompatible types in assignment (expression has type "int", variable has type "str")  [assignment]
Found 1 error in 1 file (checked 1 source file)


$ mypy --strict variable_and_function.py
variable_and_function.py:2:1: error: Function is missing a return type annotation  [no-untyped-def]
Found 1 error in 1 file (checked 1 source file)
```

## Define the return type
{id: python-types-at-pyweb-2024-12-define-return-type}

![](examples/python-types-at-pyweb-2024-12/variable_and_function_with_return_type.py)

```
$ mypy variable_and_function_with_return_type.py
variable_and_function_with_return_type.py:8:15: error: Incompatible types in assignment (expression has type "int", variable has type "str")  [assignment]
Found 1 error in 1 file (checked 1 source file)
```

## Infer (deduct) the type
{id: python-types-at-pyweb-2024-12-infer-the-type}

* We can define every variable, but in many cases Python will infer them from other definitions.

![](examples/python-types-at-pyweb-2024-12/deduct_type_of_variable.py)


## Type in unannotated function
{id: python-types-at-pyweb-2024-12-unannotated-function}

![](examples/python-types-at-pyweb-2024-12/unannotated_function.py)

```
$ mypy unannotated_function.py
unannotated_function.py:3:5: note: By default the bodies of untyped functions are not checked, consider using --check-untyped-defs  [annotation-unchecked]
Success: no issues found in 1 source file


$ mypy --check-untyped-def unannotated_function.py 
unannotated_function.py:3:19: error: Incompatible types in assignment (expression has type "int", variable has type "str")  [assignment]
Found 1 error in 1 file (checked 1 source file)


$ mypy --strict unannotated_function.py 
unannotated_function.py:2:1: error: Function is missing a return type annotation  [no-untyped-def]
unannotated_function.py:2:1: note: Use "-> None" if function does not return a value
unannotated_function.py:3:19: error: Incompatible types in assignment (expression has type "int", variable has type "str")  [assignment]
unannotated_function.py:6:1: error: Call to untyped function "do_something" in typed context  [no-untyped-call]
Found 3 errors in 1 file (checked 1 source file)
```


## Built-in types
{id: python-types-at-pyweb-2024-12-built-in-types}
{i: str}
{i: int}
{i: float}
{i: bool}
{i: list}
{i: tuple}
{i: dict}
{i: set}

![](examples/python-types-at-pyweb-2024-12/built_in_types.py)

## Complex types
{id: python-types-at-pyweb-2024-12-complex-types}
{i: List}
{i: Dict}
{i: Set}
{i: Tuple}

* For Python 3.8 and before

![](examples/python-types-at-pyweb-2024-12/complex_types_old.py)

* For Python 3.9+

![](examples/python-types-at-pyweb-2024-12/complex_types.py)

## Either this or that type
{id: python-types-at-pyweb-2024-12-either-this-or-that-type}
{i: Union}

* Before 3.10

![](examples/python-types-at-pyweb-2024-12/union.py)

```
$ python union.py
int
str
float

$ mypy union.py
union.py:8:9: error: Argument 1 to "my_exit" has incompatible type "float"; expected "str | int"  [arg-type]
Found 1 error in 1 file (checked 1 source file)
```

* Python 3.10+

![](examples/python-types-at-pyweb-2024-12/pipe.py)

```
$ python union.py
int
str
float

$ mypy pipe.py
pipe.py:6:9: error: Argument 1 to "my_exit" has incompatible type "float"; expected "str | int"  [arg-type]
Found 1 error in 1 file (checked 1 source file)
```
## mypy generics
{id: python-types-at-pyweb-2024-12-mypy-generics}

![](examples/python-types-at-pyweb-2024-12/generics.py)

## mypy suggestions
{id: python-types-at-pyweb-2024-12-mypy-suggestions}

Defined parameters and the return value of a function
Simple types such as int

from typing import Dict, List, Union, KeysView, Tuple, Optional
from typing_extensions import Literal, TypedDict, NotRequired  # TODO move to typing after upgrading python to 3.8
import numpy as np
import numpy.typing as npt
import uuid
import pandas as pd

LabelType = str  # "square \u2208 shape"
WebReturnType = Dict[str, Union[str, int]]
XYModelType = Literal["umap", "tsne", "pca"]
ActivationType = npt.NDArray[np.complex64]
HashType = str  # should be 40 bytes long, this is the hashed ID of an image
HistoryType = TypedDict('HistoryType', {'date' : str, 'event': str, 'info': str})

PipelineStepType = TypedDict('PipelineStepType', {
    "step_type": str,
    "step_name": str,
})



* Set `MYPY_CACHE_DIR` environment variable
* Create `mypy.ini`

![](examples/python-types-at-pyweb-2024-12/mypy.ini)


## The end
{id: python-types-at-pyweb-2024-12-the-end}

* Don't forget to run mypy!



# Python types at PyWeb 2025.05
{id: python-types-at-pyweb-2025-05}


## Python types at PyWeb 2025.05
{id: python-types-at-pyweb-2025-05-open}

[see the types](https://python.org.il/en/people/)


## The Answer
{id: python-types-at-pyweb-2025-05-answer}

![](examples/python-types-at-pyweb-2025-05/answer.py)

{aside}
Why would anyone write such obviously incorrect code?
{/aside}

## Add
{id: python-types-at-pyweb-2025-05-add}

What is the result of this code in Perl / Python / JavaScript / Rust?

![](examples/python-types-at-pyweb-2025-05/add.rs)

![](examples/python-types-at-pyweb-2025-05/add.py)

![](examples/python-types-at-pyweb-2025-05/add.js)

![](examples/python-types-at-pyweb-2025-05/add.pl)

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
{id: python-types-at-pyweb-2025-05-add-in-function}

![](examples/python-types-at-pyweb-2025-05/function.rs)

![](examples/python-types-at-pyweb-2025-05/function.py)

![](examples/python-types-at-pyweb-2025-05/function.js)

![](examples/python-types-at-pyweb-2025-05/function.pl)

{aside}
Much less obvious if we are calling a function with parameters that are not the correct type.

The result is the same as in the previous example.
{/aside}

## Shift-left (testing, programming)
{id: python-types-at-pyweb-2025-05-shift-left}

* Rust is the shift-left language noticing bugs earlier in the development process.
* How can we get Python to also complain earlier?

## Function with type annotation
{id: python-types-at-pyweb-2025-05-add-in-function-with-type-annotation}

* We can add type-annotations to the function parameters and even to the return value.

![](examples/python-types-at-pyweb-2025-05/function_with_type.py)

* However, Python will disregard these type-annotations and we still get a run-time exception.

## Use mypy
{id: python-types-at-pyweb-2025-05-mypy}

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

## How add type annotation?
{id: python-types-at-pyweb-2025-05-add-type-annotation}

* We already saw the two examples:
* Add type annotation to variables.
* Add type annotation to the function signature.

![](examples/python-types-at-pyweb-2025-05/type_annotation.py)



## Infer (deduct) the type
{id: python-types-at-pyweb-2025-05-infer-the-type}

* We can define every variable, but in many cases Python will infer them from other definitions.

![](examples/python-types-at-pyweb-2025-05/deduct_type_of_variable.py)


## Type in unannotated function
{id: python-types-at-pyweb-2025-05-unannotated-function}
{i: --check-untyped-def}
{i: --strict}

![](examples/python-types-at-pyweb-2025-05/unannotated_function.py)

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
{id: python-types-at-pyweb-2025-05-built-in-types}
{i: str}
{i: int}
{i: float}
{i: bool}
{i: list}
{i: tuple}
{i: dict}
{i: set}

![](examples/python-types-at-pyweb-2025-05/built_in_types.py)

## Complex types
{id: python-types-at-pyweb-2025-05-complex-types}

* For Python 3.9+

![](examples/python-types-at-pyweb-2025-05/complex_types.py)

## Either this or that type (Union)
{id: python-types-at-pyweb-2025-05-either-this-or-that-type}
{i: Union}

* Python 3.10+

![](examples/python-types-at-pyweb-2025-05/pipe.py)

```
$ python union.py
int
str
float

$ mypy pipe.py
pipe.py:6:9: error: Argument 1 to "my_exit" has incompatible type "float"; expected "str | int"  [arg-type]
Found 1 error in 1 file (checked 1 source file)
```

## Optional type (variable can also be None)
{id: python-types-at-pyweb-2025-05-optional-type-with-pipe}
{i: Optional}
{i: split}

![](examples/python-types-at-pyweb-2025-05/this_or_none.py)

## Define type alias
{id: python-types-at-pyweb-2025-05-define-type-alias}

![](examples/python-types-at-pyweb-2025-05/defined_type_alias.py)

## Define complex type alias
{id: python-types-at-pyweb-2025-05-define-complex-type-alias}

![](examples/python-types-at-pyweb-2025-05/defined_complex_type_alias.py)

## Define type for enum and complex dictionary
{id: python-types-at-pyweb-2025-05-define-type-for-enum}

![](examples/python-types-at-pyweb-2025-05/defined_types.py)

## mypy generics - plain
{id: python-types-at-pyweb-2025-05-mypy-generics-plain}

* We can use [generics](https://mypy.readthedocs.io/en/stable/generics.html) to say that we accept any type and we can use it to indicate that some other parameter or the return type will be the same type.

![](examples/python-types-at-pyweb-2025-05/generics_plain.py)

## mypy generics - cannot be any type
{id: python-types-at-pyweb-2025-05-mypy-generics-cannot-be-any-type}

![](examples/python-types-at-pyweb-2025-05/generics_cannot_be_any_type.py)

```
mypy generics_cannot_be_any_type.py

generics_limit_types_by_listing.py:2:12: error: Unsupported left operand type for + ("T")  [operator]
Found 1 error in 1 file (checked 1 source file)
```

## mypy generics - limit the types by listing
{id: python-types-at-pyweb-2025-05-mypy-generics-limit-the-types-by-listing}

![](examples/python-types-at-pyweb-2025-05/generics_limit_types_by_listing.py)

## mypy generics - limit by functionality
{id: python-types-at-pyweb-2025-05-mypy-generics}

* A more generic way to define generics is by creating types that need to have certain functionality

![](examples/python-types-at-pyweb-2025-05/generics.py)

## Two variables of the same and different types
{id: python-types-at-pyweb-2025-05-same-and-different-types}

![](examples/python-types-at-pyweb-2025-05/generics_two_types.py)

```
$ mypy generics_two_types.py
generics_two_types.py:10:1: error: Value of type variable "T" of "the_same" cannot be "object"  [type-var]
Found 1 error in 1 file (checked 1 source file)
```

## mypy suggestions
{id: python-types-at-pyweb-2025-05-mypy-suggestions}

* Set `MYPY_CACHE_DIR` environment variable
* Create `mypy.ini`

![](examples/python-types-at-pyweb-2025-05/mypy.ini)


## The end
{id: python-types-at-pyweb-2025-05-the-end}

* Don't forget to run mypy!

## Bloopers
{id: python-types-at-pyweb-2025-05-bloopers}

## Define the type of variables
{id: python-types-at-pyweb-2025-05-type-of-variables}

![](examples/python-types-at-pyweb-2025-05/variable_and_function.py)

```
$ mypy variable_and_function.py
variable_and_function.py:7:15: error: Incompatible types in assignment (expression has type "int", variable has type "str")  [assignment]
Found 1 error in 1 file (checked 1 source file)


$ mypy --strict variable_and_function.py
variable_and_function.py:2:1: error: Function is missing a return type annotation  [no-untyped-def]
Found 1 error in 1 file (checked 1 source file)
```

## Define the return type
{id: python-types-at-pyweb-2025-05-define-return-type}

![](examples/python-types-at-pyweb-2025-05/variable_and_function_with_return_type.py)

```
$ mypy variable_and_function_with_return_type.py
variable_and_function_with_return_type.py:8:15: error: Incompatible types in assignment (expression has type "int", variable has type "str")  [assignment]
Found 1 error in 1 file (checked 1 source file)
```

## Complex types for Python 3.8 and before
{id: python-types-at-pyweb-2025-05-complex-types-for-older-versions}
{i: List}
{i: Dict}
{i: Set}
{i: Tuple}

![](examples/python-types-at-pyweb-2025-05/complex_types_old.py)

## Either this or that type for Python before 3.10
{id: python-types-at-pyweb-2025-05-either-this-or-that-type-for-older-version}
{i: Union}

![](examples/python-types-at-pyweb-2025-05/union.py)
```
$ python union.py
int
str
float

$ mypy union.py
union.py:8:9: error: Argument 1 to "my_exit" has incompatible type "float"; expected "str | int"  [arg-type]
Found 1 error in 1 file (checked 1 source file)
```




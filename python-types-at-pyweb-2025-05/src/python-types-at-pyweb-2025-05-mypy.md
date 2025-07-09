# Use mypy

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




# Mixing positional and named parameters - order



We can also mix the parameters passed to any user-defined function, but we have to make sure that
positional parameters always come first and named (key-value) parameter come at the
end of the parameter list.


{% embed include file="src/examples/functions/named_and_positional_params.py" %}

```
  File "examples/functions/named_and_positional_params.py", line 14
    'gabor@szabgab.com',
    ^
SyntaxError: positional argument follows keyword argument
```

{% embed include file="src/examples/functions/positional_and_named_params.py" %}



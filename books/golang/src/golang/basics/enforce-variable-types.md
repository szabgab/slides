# Enforce variables types

Each variable in Go has a type and Go will not let you mix values and variables of
different types. When we created the variable with the `:=`
operator Go automatically deducted the type from the assigned value. In this case it was `string`.


{% embed include file="src/examples/variable/variable.go" %}
{% embed include file="src/examples/variable/variable.out" %}

```
# command-line-arguments
./variable.go:8:7: cannot use 42 (type int) as type string in assignment
```

* Compile-time error



# Defer

* defer


Every `defer` statement is executed after the enclosing function ends.
In reverse order. (Similar to `END` block in Perl, similar to `with` context in python)

{% embed include file="src/examples/defer/defer.go" %}

```
$ go run defer.go

first
second
third
two
one
```



# Defer in if-statements

* Even if we put the defer call inside an if-statement, the deferred function will only execute at the end of the enclosing function.

{% embed include file="src/examples/defer-no-in-if/defer_no_in_if.go" %}




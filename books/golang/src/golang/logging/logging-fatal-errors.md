# Logging Fatal errors

* `Fatal`, `Fatalf`, and `Fataln` print the message and call `os.Exit(1)` for the program to  exit with code 1.
* Does not execute the lines after calling `Fatal`

{% embed include file="src/examples/logging-fatal/logging_fatal.go" %}
{% embed include file="src/examples/logging-fatal/logging_fatal.out" %}



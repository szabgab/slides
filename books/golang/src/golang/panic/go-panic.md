# Panic

In many other programming languages (e.g Python, Java) if the code encounters a problem it raises an exception that if not treated properly will stop the execution.
In some other programming languages (e.g. C, Perl) functions return an error code when something does not work.



Go leans towards the languages that return error, though it usually returns it as a separate value.
In addition Go has a concept similar to exceptions, but is rarely used and to reflect the different usage it also has a different name. It is called `panic`.



In Go if you try to open a file and you fail, this is considered as a normal situation - not an exceptional one, hence Go will return a representation of the
error but won't try to stop the program. On the other hand if you try to divide by 0, Go will freak out and `panic`.



Let's see how does that work.


{% embed include file="src/examples/go-panic/go_panic.go" %}
{% embed include file="src/examples/go-panic/go_panic.out" %}



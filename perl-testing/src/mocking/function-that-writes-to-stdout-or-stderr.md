# Function that (also) writes to STDOUT or STDERR

There are many cases when we encounter a function that does more than one things. For example in the following simplified
example we have a function that both makes some (simple) mathematical calculation and prints to the screen.
For added fun it also prints to the Standard Error channel.

We will probably want to refactor it to separate the concerns of calculating and IO, but first we'd like to write a unit-test.

In this example we use the capture function of the Capture::Tiny module that will capture and return as a string everything that is
printed to STDOUT and STDERR. (It could also capture the exit value of an external call, but this is not relevant in our case.

The whole code is wrapped in a subtest so the external $result variable will be lexically scoped.


{% embed include file="src/examples/capture-stdout-stderr/lib/CalcOutput.pm" %}

{% embed include file="src/examples/capture-stdout-stderr/bin/calc.pl" %}

```
perl -Ilib bin/calc.pl 7 8
```



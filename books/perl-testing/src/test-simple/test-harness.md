# Harness

* harness
* Test::Harness


This is a module that can analyze the ok / not ok printouts with the numbers.
In particular, it can analyze the output of Test::Simple and a whole class of
other modules in the Test::* namespace on CPAN we are going to see later.

The harness.pl script is just a sample usage of the Test::Harness module.
It accepts one or more test files, runs them and analyzes the output they generated.


{% embed include file="src/examples/test-simple/harness.pl" %}


Run the previous test file using Test::Harness


```
$ perl ../test-simple/harness.pl tests/t24.pl
```


If the original test script had very few test units then this output won't make much sense, but if the original
test script had hundreds of OKs, we would not be really interested on all those OKs. We would be mainly interested
in a summary, and in the (hopefully) little number of "NOT OK" printouts. This is how the output of Test::Harness looks like:


{% embed include file="src/examples/test-simple/tests/large_harness.out" %}




# Testing demo - use the module


Before we start writing an "automated test", let's see how one could test this code "manually". In reality I see this
many times, that people write short snippets of code to check if their real code works properly, but they
don't turn these small snippets into real tests.

Basically the question is "How can we use the add function of the mymath module?"

The code is straight forward. We import the module. We import the "sys" module to be able to access the command line arguments.
We take two arguments from the command line, call the function, and print the result.

Then, if we would like to make sure our code works well, we can compare that result to some expected result.

Based on this everything works fine.


{% embed include file="src/examples/testing-demo/use_mymath.py" %}

```
python use_mymath.py 2 2
4
```




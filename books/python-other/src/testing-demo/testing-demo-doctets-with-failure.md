# Testing demo: doctest with failure

Of course we know that our code is not perfect (to say the least) so at one point someone will complain about the
incorrect results received, for example in case they try to add 3 and 3. Before running and fixing the code however
it is better to write a test case with the expected correct result that will fail.

So we added another example to the documentation.

If we run the same command as we did earlier we'll get an extensive output on the screen and the exit code
with have some value different from 0.

At this point you'd probably also go and fix the code, but you have also increased the number of tests and
eliminated the possibility of this failure to return unnoticed.


{% embed include file="src/examples/testing-demo/doctest_fail/mymath.py" %}


{% embed include file="src/examples/testing-demo/doctest_fail/mymath.out)

```
$ python -m doctest mymath.py
$ echo $?
1
```

```
> python -m doctest mymath.py
> echo %ERRORLEVEL%
1
```



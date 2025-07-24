# Pytest failing test in one function

Once we had that passing test we might have shared our code just to receive complaints that it does not always work properly. One use might complain that passing in 2 and 3 does not give the expected 5.

So for your investigation the first thing you need to do is to write a test case expecting it to work proving that your code works. So you add a second assertion.

{% embed include file="src/examples/pytest/math/test_mymath_more.py" %}

To your surprise the tests fails with the following output:


{% embed include file="src/examples/pytest/math/test_mymath_more.out" %}

We see the `collected 1 item` because we still only have one test function.

Then next to the test file we see the letter F indicating that we had a single test failure.

Then we can see the details of the test failure. Among other things we can see the actual value returned by the `add` function
and the expected value.

Knowing that `assert` only receives the True or False values of the comparision, you might wonder how did this happen.
This is part of the magic of pytest. It uses some introspection to see what was in the expression that was passed to `assert` and it can print out the details
helping us see what was the expected value and what was the actual value. This can help understanding the real problem behind the scenes.


You can also check the exit code and it will be something different from 0 indicating that something did not work.
The exit code is used by CI-systems to see which test run were successful and which failed.

```
$ echo $?
1
```

```
> echo %ERRORLEVEL%
1
```

One big disadvantage of having two asserts in the same test function is that we don't have clear indication that the first assert was successful.
Moreover if the first assert fails then the second would not be even executed so we would not know what is the status of that case.



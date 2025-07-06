# Compare actual with expected values and print only pass/fail


{% embed include file="src/examples/php/intro/t03.php" %}

Result:

```
pass
pass
fail
```

Instead of manually comparing the actual results with the expected values
let the computer do the hard work and let it only print if there was a success
or a failure. We introduce some new code that will print "pass" for every case
when the result was the expected value and "fail" when they were different.

This is certainly an improvement but before we further improve our display let's
turn our attention to our own testing code.



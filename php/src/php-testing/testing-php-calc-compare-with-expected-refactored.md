# Refactor to get assertTrue


As we are also programmers we will soon recognize that there
is code duplication in our test script and will factor out the
whole printing of pass/fail part to a function that we call assertTrue().
It should receive a true or false value and it will print "pass" or "fail"
accordingly.

{% embed include file="src/examples/php/intro/t04.php" %}

Result:

```
pass
pass
fail
```


As in every refactoring the functionality and the output should remain the
same, just the implementation improves. (Hopefully)



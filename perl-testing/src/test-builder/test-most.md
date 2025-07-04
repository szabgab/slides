# Test::Most

* Test::Most
* die_on_fail


[Test::Most](https://metacpan.org/pod/Test::Most) by Curtis "Ovid" Poe
is a replacement of Test::More with even more stuff.
It exports the functions of the following test modules
making it a bit more convenient to use them.



* Test::More
* Test::Exception
* Test::Differences
* Test::Deep



It also provides a nice set of extra features such as
the `die_on_fail;` and `bail_on_fail` calls.


{% embed include file="src/examples/test-perl/t/test_most.t" %}

```
prove examples/test-perl/t/test_most.t
DIE_ON_FAIL=1 prove examples/test-perl/t/test_most.t
BAIL_ON_FAIL=1 prove examples/test-perl/t/test_most.t
```




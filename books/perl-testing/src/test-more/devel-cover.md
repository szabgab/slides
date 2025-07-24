# Test coverage using Devel::Cover


* Devel::Cover

```
cover --test
```



Once we know that our tests are passing we could check which lines
are exercised in the code during the test execution. For this
we can use Devel::Cover by Paul Johnson.
First we need to run the tests again now instrumenting with Devel::Cover.
This will be much slower than the regular execution but in the end
we will get a text report and we will be able to build a nice HTML
report with drill down about all the code we ran.

{% embed include file="src/coverage_summary.png)

```
All tests successful.
Files=11, Tests=2078, 50 wallclock secs
```

* [Devel::Cover](https://metacpan.org/pod/Devel::Cover)
* [CPAN Cover](http://cpancover.com/)
* [Meta::CPAN](https://metacpan.org/)



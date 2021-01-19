# Test::More
{id: test-more}

## Moving over to Test::More
{id: moving-to-test-more}
{i: Test::More}

Test::Simple is really a very simple module. Its sole exported function is the "ok" function.

Test::More has the same "ok" function - so it is a drop-in replacement - but it also has lots of
other functions and tools:

* `ok`
* `is`
* `isnt`
* `diag`
* `node`
* `like`
* `cmp_ok`
* `is_deeply`
* `SKIP`
* `TODO`
* `done_testing`
* `subtest`


```
Better error reporting.
```

In the end every test can be based on the single ok() function.
The additional functions mainly serve as convenience methods
to allow better error reporting.

## Test::Simple ok(  trueness,     name);
{id: test-simple-ok}
{i: ok|Test::Simple}

* The previous examples using Test::Simple.

![](examples/test-more/t/30.t)

```
perl t/30.t
```

![](examples/test-more/t/30.t.out)


## Test::More ok(  trueness,     name);
{id: test-more-ok}
{i: ok|Test::More}

* Test::More is a drop-in replacement of Test::Simple.

![](examples/test-more/t/31.t)

```
perl t/31.t
```

![](examples/test-more/t/31.t.out)

## Test::More is(  value,   expected_value,   name);
{id: test-more-is}
{i: is}


It would be much better to see the expected value and the actually received value.
This usually helps in locating the problem.


![](examples/test-more/t/32.t)

```
perl t/32.t
```

![](examples/test-more/t/32.t.out)

See, in this case we can already guess that it cannot add 3 values.

* `is` compares using `eq`

## Test::More isnt( value, not_expected_value,  name);
{id: test-more-isnt}
{i: isnt}

Sometimes you are expecting to get a value but you don't really know what.
You just know one specific value that you want to make sure you have not
received.

![](examples/test-perl/t/isnt.t)

```
perl t/isnt.t
```

![](examples/test-perl/t/isnt.t.out)

This isn't a good example though.


## Test::More isnt undef
{id: test-more-isnt-undef}
{i: undef}

![](examples/test-more/t/isnt_undef.t)

```
perl t/isnt_undef.t
```

Output:

![](examples/test-more/t/isnt_undef.t.out)


## note( message ) or diag( message );
{id: test-more-diag-note}
{i: diag}
{i: note}

* `diag` prints out a message along with the rest of the output.
* `note()` does the same, but when running under the prove it does not show up.

Use it for whatever extra output in order to ensure that
your printouts will not interfere with future changes in the
test environment modules (such as `prove` or `Test::Harness`).


![](examples/test-more/t/messages.t)

```
$ perl t/messages.t
```

![](examples/test-more/t/messages.t.out)

```
prove t/messages.t
```

![](examples/test-more/t/messages.t.prove.out)

```
prove -v t/messages.t
```

![](examples/test-more/t/messages.t.prove-v.out)



## (note or diag) explain( a_variable );
{id: test-more-explain}
{i: explain}

* `explain();` will recognize if its parameter is a simple scalar or a reference to a more complex data structure.

Its result must be passed to either note(); does or diag();


![](examples/test-more/t/explain.t)

```
perl t/explain.t
```

![](examples/test-more/t/explain.t.out)

## TODO
{id: test-more-todo}
{i: TODO}

When you don't want to see the failing tests any more

![](examples/test-more/t/34.t)

```
$ prove -l t/34.t
```

![](examples/test-more/t/34.t.prove.out)

## TODO Verbose output
{id: test-more-todo-verbose}
{i: TODO}

```
$ prove -lv t/34.t
```

![](examples/test-more/t/34.t.prove-v.out)

{aside}
In the eXtreme Programming paradigm the following two key aspects are somewhat
in contradiction:
1) Write your test before you write your code.
2) Make sure your test suit always passes at 100%.

Of course after you already wrote your tests for a new feature but before you
can write the actual code there is a short time period when your test suit will
not pass 100%.

Worse than that, it is also recommended that immediately when you get a bug report
from somewhere you should write a test case that reproduces this bug. Obviously
this test will fail before you fix the bug and will hopefully pass once you fixed it.

In order to make the test suit happy there is a way to tell the harness tool that a test
is *supposed to fail*. That is, we know it will fail. What we can do to achieve this is
to set one or more tests to be in a TODO block.
{/aside}


## TODO: unexpected success
{id: test-more-todo-unexpected-success}

What if the bug gets fixed - accidentally?

![](examples/test-more/t/35.t.out)

![](examples/test-more/t/35.t.verbose.out)

## TODO: unexpected success (the code)
{id: test-more-todo-unexpected-success-the-code}

![](examples/test-more/lib/MySimpleCalcFixed.pm)

![](examples/test-more/t/35.t)


## MyTools with various functions
{id: mytools-with-various-functions}

![](examples/test-more/lib/MyTools.pm)

## like(value, qr/expected regex/, name);
{id: test-more-like-date}

What if you don't want or can't realisticly expect an exact match with the result?

You can use `like` that compares with regex `=~`.

![](examples/test-more/show_last_update.pl)

```
This page was last updated at 2020-11-10T09:19:38
```

![](examples/test-more/t/last_update.t)

```
prove t/last_update.t
```

![](examples/test-more/t/last_update.t.out)

## like(value, qr/expected regex/, name);
{id: test-more-like}
{i: like}

![](examples/test-more/show_copyright.pl)

![](examples/test-more/show_copyright.out)

![](examples/test-more/t/copyright.t)


![](examples/test-more/t/copyright.t.out)


## Another example with like
{id: test-more-like2}

![](examples/test-more/t/like.t)

![](examples/test-more/t/like.t.out)


## cmp_ok(   this,   op,  that,    name);
{id: test-more-cmp-ok}
{i: cmp_ok}

{aside}
Sometimes an eq by is() or a regular expression by like() just isn't good enough.
For example what if you would like to check the rand() function of perl? Its result 
must be between 0 (inclusive) and 1 (non inclusive).
{/aside}

{aside}
In other case you might have a function that should happen within a certain period of time.
You don't have an exact expectation but you know the elapsed time must be between a lower
and upper limit.
{/aside}

`cmp_ok` compares with any operator you like.

![](examples/test-more/t/cmp_ok.t)

![](examples/test-more/t/cmp_ok.t.out)

![](examples/test-more/t/cmp_ok.t.2.out)

* Actually this is a really bad test as it can fail randomnly


## is_deeply(  complex_structure,   expected_complex_structure,   name);
{id: test-more-is-deeply}
{i: is_deeply}


Compare two Perl data structures:

![](examples/test-more/t/is_deeply.t)

![](examples/test-more/t/is_deeply.t.out)


## Function returning data from bug-tracker
{id: function-returning-data-from-bugtracker}

{aside}
Look at the code that generates the bug reports you'll see that testing the 4th return value
- which is quite complex already - is hard. We cannot test against a fixed hash as some
of the values are totally dynamic (e.g. a timestamp).
{/aside}

![](examples/test-more/lib/MyBugs.pm)


## is_deeply on a hash
{id: test-more-is-deeply-hash}


Another example with `is_deeply`
checking the returned hash from a bug tracking system.


![](examples/test-more/t/is_deeply_bugs.t)

![](examples/test-more/t/is_deeply_bugs.t.out)

{aside}
What if we are testing a live system and so not interested in the exact values,
just in the keys and the fact that the values are numbers?
{/aside}


## Platform dependent tests
{id: platform-dependent-tests}

![](examples/test-more/t/without_skip.t)

![](examples/test-more/t/without_skip.t.out)

{aside}
Sometimes, you know that a part of your test suite isn't relevant.
Running them - if at all possible - would report false results.
Maybe some of the features of your system are platform dependent, you don't want to
test them on an unsupported platform. Sometimes failure of previous tests make a
test irrelevant.

In all such cases what you actually want is to skip the tests. Surprisingly the way
to do that is to enclose the tests in a SKIP block.
{/aside}


## SKIP some tests
{id: test-more-skip}
{i: SKIP}

![](examples/test-more/t/skip.t)

Output:

```
1..2
ok 1
ok 2 # skip Windows related tests
```


## locale
{id: test-more-locale}
{i: locale}

![](examples/test-more/t/locale.t)


## Stop running current test script
{id: test-more-stop-testing}

{aside}
When running a test script sometimes we reach a
failure that is so problematic you cannot go on testing.
This can be in the scope of a single test script in which case
you would call exit() to abort the current test script or it can
be so bad that all the testing should stop. In that case you should call
BAIL_OUT(). That will indicate the harness that it should not call
any other test script.
{/aside}

![](examples/test-more/t/exit.t)

```
prove t/exit.t t/other.t
```

![](examples/test-more/t/exit.out)


## Stop all the test scripts
{id: test-more-bail-out}
{i: BAIL_OUT}

![](examples/test-more/t/bail_out.t)

```
prove t/bail_out.t t/other.t
```

![](examples/test-more/t/bail_out.out)


## Exercises
{id: exercise-test-more}

* Take a local copy of the Math::RPN module located in (examples/Math-RPN) and add 30 test cases. See what is [Reverse Polish Notation](https://en.wikipedia.org/wiki/Reverse_Polish_notation).
* You can also look for a module on [CPAN](https://metacpan.org/) - maybe one that you are using a lot.  Maybe one that you found a problem with.
* Download the tar.gz file from CPAN unzip it (don't install the module) and write at least 20 tests.


## Test coverage using Devel::Cover
{id: devel-cover}
{i: Devel::Cover}

```
cover --test
```


{aside}
Once we know that our tests are passing we could check which lines
are exercised in the code during the test execution. For this
we can use Devel::Cover by Paul Johnson.
First we need to run the tests again now instrumenting with Devel::Cover.
This will be much slower than the regular execution but in the end
we will get a text report and we will be able to build a nice HTML
report with drill down about all the code we ran.
{/aside}
![](coverage_summary.png)

```
All tests successful.
Files=11, Tests=2078, 50 wallclock secs
```

* [Devel::Cover](https://metacpan.org/pod/Devel::Cover)
* [CPAN Cover](http://cpancover.com/)
* [Meta::CPAN](https://metacpan.org/)

## Test coverage report example
{id: devel-cover-example}

![](examples/cover/lib/MyMath.pm)
![](examples/cover/t/test.t)
![](examples/cover/Makefile.PL)


## Declare your plan at execution time
{id: test-calculated-plan}
{i: plan}

```
use Test::More tests => 6;

or

use Test::More;
...
plan tests =>  6;
```

{aside}

No need to tell your plan at load time;
{/aside}

{aside}

Earlier when we were talking about Test::Simple we had a case when
the test data was placed in an array and the test script looped over
the array executing the function to be tested for each input.
{/aside}

{aside}

Later we moved the data to an external file which made it even more
difficult to declare the plan so we used lengthy code in the BEGIN block
in order to have the expected number of tests before Test::Simple is loaded
into memory.
{/aside}

{aside}

With Test::More we have a much better solution. We don't have to
declare the plan on the use Test::More line. We can do that later,
in the run time of the Perl script.
{/aside}

![](examples/test-more/t/plan_tests.t)

## done_testing
{id: done-testing}
{i: done_testing}

{aside}
I am not a fan of it, but in rare cases it is useful to know that **done_testing** can be used to signal all tests have been done.
This way we don't need to have a "plan".
{/aside}

![](examples/test-more/t/done_testing.t)


## subtest with plan
{id: subtest-with-plan}

![](examples/test-more/t/planned_subtest.t)

```
prove -l t/planned_subtest.t
```

![](examples/test-more/t/planned_subtest.out)


## subtest with implicit done_testing
{id: subtest}
{i: done_testing}

![](examples/test-more/t/subtest.t)
![](examples/test-more/t/subtest.out)

Implicit call to done_testing inside. skip-able, etc.


## skip all
{id: skip-all}
{i: skip_all}

![](examples/test-more/t/skip_all.t)


## Exercise: skip test
{id: exercise-skip-test}

* Write a test that will be skipped if is run as root. (Administrator on Windows?)
* And another test that will executed only when not run as root.
* Write a test script called long.t that takes a long time to run. Execute it only if the RUN_LONG environment variable is true.
* Other ideas: Skip tests that need database access and/or tests that need network access.


## Exercise: use coverage
{id: exercise-test-coverage}

Generate a test coverage report for Math::RPN or the module you
are testing and look for holes in the coverage. Add more tests.
A few suggestions:
Archive::Zip,

[top 20](http://blogs.perl.org/users/neilb/2014/08/fix-a-bug-on-cpan-day.html).

## Test blocks (use subtest instead)
{id: test-blocks}
{i: {}}

{aside}
Create small blocks of tests
{/aside}

{aside}
When writing a test script you often write similar pieces of code that do
unrelated tests. You can reuse the same variables throughout the test script
but that means that in case of a bug in the test script the various parts might
have effects on each other.

You can also invent new names for the variables but there are only so many names
you can reasonably use for the same kind of data.

The best solution probably is to put the individual pieces into anonymous blocks.
That serves several purposes. First of all it makes clear to both the writer of the
code and the reader that the blocks are mostly independent.
It also ensures that the variables used in one block won't interfere with the variables
in the other block. You'll even have to define these variables in both blocks.
{/aside}

![](examples/test-perl/t/blocks.t)


## Counting tests in the small blocks (use subtest instead)
{id: test-begin-block}
{i: BEGIN}

{aside}

When you are writing many test in one file quickly you'll face the problem of
keeping the "plan" up to date. You will add a test and forget to update
the number worse, you'll add many tests and when you suddenly remember you
did not update the number it is too late already. Will you switch to "no_plan"?
Will you count the ok(), is() and similar calls? Will you run the test and update your expectation accordingly?

There is trick I learned on the perl-qa mailing list.

You declare a variable called $tests at the beginning of the script.
Then at the end of each section you update the number.
{/aside}
![](examples/test-perl/t/begin_block.t)

See also:
[Test::Block](http://metacpan.org/pod/Test::Block)




# Test libraries
{id: test-builder}

## Multiple expected values
{id: testing-multiple-expected-values}

`dice()` returns a whole number between 1-6.


{aside}
In the application we have a function that can return any one of a list of possible values.
In our example we have a dice() function that throws the dice. It should return a whole
number between 1-6.
{/aside}

![](examples/test-perl/t/dice_cmp_ok.t)

```
perl examples/test-perl/t/dice_cmp_ok.t
```

![](examples/test-perl/t/dice_cmp_ok.out)

It seems to be ok but we are actually not testing the correct thing.
We should check if the result is one of the following values (1, 2, 3, 4, 5, 6)


## Multiple expected values revised
{id: testing-multiple-expected-values-with-any}
{i: any}
{i: List::MoreUtils}

We are going to use the "any" function of List::MoreUtils.

![](examples/test-perl/t/dice_any.t)

Output:

![](examples/test-perl/t/dice_any.out)

{aside}
This shows that there is some problem but we still don't know what exactly is the problem.
Especially think if this is part of a larger test suit when one of the tests fail.
We would like to see the actual value and maybe even the expected values.
{/aside}


## Adding information with diag
{id: test-more-diag-information}
{i: diag}

{aside}

All the ok() and related functions return true or false depending on their reporting
success or failure. One can use this to print extra information using diag()
{/aside}
![](examples/test-perl/t/dice_any_diag.t)

Output:

![](examples/test-perl/t/dice_any_diag.out)


## My own test functions
{id: test-functions}

{aside}

After writing lots of tests, you'll see that you need the above code (with the extra diag)
in several places in your tests script, so you'll want to refactor it
and create a function wrapping it.

The story behind is that the dice() function can actually get any number ($n) and it
should then produce a random whole number between 1 and $n. The default is 6. So we
are testing dice() with several possible parameters.
{/aside}
![](examples/test-perl/t/dice_is_any.t)

{aside}

We move the ok() to a function call is_any and we are calling it with the actual value,
a reference to an array holding the expected values and the name of the test uint.
We had to slightly change the part of the ok() as now we have a reference to the expected
values and not the array itself.
{/aside}

Output:

![](examples/test-perl/t/dice_is_any.out)

{aside}

This seems to be ok but we have a slight problem here. The row number displayed in the
error report is the row number where we actually call the ok() and not where we call the
is_any().
{/aside}


## My own test functions with Test Builder level
{id: test-functions-level}
{i: Test::Builder}
{i: $Test::Builder::Level}

{aside}

Behind the scenes both Test::Simple and Test::More use a module
called Test::Builder. Actually Test::Builder is doing the hard work
of counting test and displaying error messages. Test::More is just the
user friendly front end.


Adding the local $Test::Builder::Level = $Test::Builder::Level + 1;
to our own test function will tell Test::Builder to go one level further
back in the call stack to find the location where the function was called
and where the error occurred.
{/aside}
![](examples/test-perl/t/dice_is_any_fixed.t)

Output:

![](examples/test-perl/t/dice_is_any_fixed.out)



## Create a test module
{id: test-builder-create-test-module}

{aside}

Now that we created the above is_any function we might want to use it in
other tests scripts as well. We might even want to distribute it to
CPAN. In order to do that we'll need to move it to a module. The accepted
name space for such modules is the Test::* namespace so we are going to
use that too.
Of course if you are building this for a specific project and not for general
use then you are probably better off using the Project::Test::* namespace
and if this is indented to be used in-house in a company then it might be better
to use Company::Test::* for the name so the chances your module will have the same
name as another module in CPAN are small.


If written correctly, the only extra thing we need to do is to
load the module and import the is_any function. Usually private test modules
are placed in the t/lib directory, so we have to add this to our @INC by
calling use lib.
{/aside}
![](examples/test-perl/t/dice.t)

{aside}

The problematic part is the module.
We need the **ok** and **diag** functions
from the Test::More package but we cannot load the Test::More package
as it would confuse the testing system.
So instead we are using the Test::Builder backend and the ok and diag methods
it provides.
{/aside}
![](examples/test-perl/t/lib/Test/MyTools.pm)

Output:

![](examples/test-perl/t/dice.out)


## Test::Builder
{id: test-builder-intro}
{i: Test::Builder}


Test modules created using Test::Builder all work nicely together.
Among other things, they don't get confused with the counting of the tests.




There are many Test::Builder based modules already available from CPAN.
Not only Test::Simple and Test::More.



* [Test::Warn](https://metacpan.org/pod/Test::Warn)
* [Test::NoWarnings](https://metacpan.org/pod/Test::NoWarnings)
* [Test::Exception](https://metacpan.org/pod/Test::Exception)
* [Test::Deep](https://metacpan.org/pod/Test::Deep)
* [Test::Differences](https://metacpan.org/pod/Test::Differences)
* ...



We'll see some of them here.




## Test::Builder object is a singleton
{id: test-builder-object}
![](examples/test-perl/t/builder.t)

**perl examples/test-perl/t/builder.t**


```
1..1
# Test::Builder=HASH(0x7ff234044ab8)
# Test::Builder=HASH(0x7ff234044ab8)
# Test::Builder=HASH(0x7ff234044ab8)
ok 1
```


## Skip on the fly
{id: test-builder-skip-on-the-fly}
{i: skip}

{aside}
There are cases when you cannot easily decide up front
which tests you'll need to skip. In such cases you can rely on
the skip method of Test::Builder that you can access from Test::More
as well.
{/aside}

![](examples/test-perl/t/skip.t)

## Skip on the fly based on earlier tests
{id: test-builder-skip-based-on-earlier-tests}
{i: skip}

![](examples/test-perl/t/skip_on_the_fly.t)

## Test with warnings
{id: testing-with-warnings}

{aside}
First we'll check if the fibonacci function works correctly even when called with
negative numbers.
{/aside}

![](examples/test-perl/t/fibonacci_negative.t)

```
prove -lv t/fibonacci_negative.t
```

![](examples/test-perl/t/fibonacci_negative.out)

{aside}
In the above code the tests are passing but there is a warning as well.
This is an expected warning so we don't need to worry about it. But then again people
or code using our module might start to rely on this warning. We would like to make sure
it won't disappear or change by mistake.
{/aside}


## Testing for warnings
{id: testing-for-warnings}
{i: Test::Warn}
{i: warnings}
{i: exception}

{aside}
Test code that should give a warning, and check if that is the correct warning.

So once we have tested our nicely behaving code we can also test our warnings and errors.
For this we are going to use several additional modules from CPAN. As they all use the
Test::Builder backend we can use them along with our standard Test::More setup.
{/aside}

![](examples/test-perl/t/fibonacci_negative_tested.t)

```
prove -lv t/fibonacci_negative_tested.t
```

![](examples/test-perl/t/fibonacci_negative_tested.out)


## Test::Warn
{id: test-warn}
{i: Test::Warn}

[Test::Warn](https://metacpan.org/pod/Test::Warn) can be used to test for both warnings and carp calls.
It can be used to check if there was a warning or if there was not.

* `warning_is`
* `warnings_are`
* `warning_like`
* `warnings_like`
* `warning_is {code} undef`  - to check there was no warning
* ...


## Test for no warnings - the hard way
{id: testing-for-no-warnings}
{i: warnings}


If we can test our code for specific warnings we should also test
that in other places there are no warnings.


![](examples/test-perl/t/fibonacci_test_warn.t)

```
prove -lv t/fibonacci_test_warn.t
```

![](examples/test-perl/t/fibonacci_test_warn.out)


## No warnings at all using Test::NoWarnings
{id: testing-for-no-warnings-at-all}
{i: Test::NoWarnings}

* [Test::NoWarnings](https://metacpan.org/pod/Test::NoWarnings)

![](examples/test-perl/t/fibonacci_no_warnings.t)

```
prove -lv t/fibonacci_no_warnings.t
```

![](examples/test-perl/t/fibonacci_no_warnings.out)


## Test with warnings Test::NoWarnings
{id: test-with-warnings}

![](examples/test-perl/t/fibonacci_with_warnings.t)

```
prove -lv t/fibonacci_with_warnings.t
```

![](examples/test-perl/t/fibonacci_with_warnings.out)

{aside}
It shows that there were warnings generated during the tests. It even tells us at which test.
The biggest problem with this module is that it does not work together with done_testing() and so it requires that you know how many test you are going to run.
{/aside}


## Test::NoWarnings
{id: test-nowarnings}
{i: Test::NoWarnings}

![](examples/test-perl/t/test_nowarnings.t)

```
prove -v t/test_nowarnings.t
```

![](examples/test-perl/t/test_nowarnings.out)


## Test::FailWarnings
{id: test-failwarnings}
{i: Test::FailWarnings}

{aside}
Test::NoWarnings does not [play well](http://www.dagolden.com/index.php/1905/alternative-to-testnowarnings/)
with **done_testing**, but  [Test::FailWarnings](https://metacpan.org/pod/Test::FailWarnings) does.
{/aside}

![](examples/test-perl/t/test_failwarnings.t)

```
prove -v t/test_failwarnings.t
```

![](examples/test-perl/t/test_failwarnings.out)


## Test::Exception
{id: test-exception}
{i: Test::Exception}

[Test::Exception](https://metacpan.org/pod/Test::Exception).

![](examples/test-perl/t/test_exception.t)

```
1..2
ok 1 - div by 2
ok 2 - div by zero
```

```
throws_ok { $foo->method } 'Error::Simple', 'simple error thrown';
```


Where Error::Simple is the class of the exception that have been thrown. e.g.
by [Exception::Class](https://metacpan.org/pod/Exception::Class).


## Exercise: improve test module
{id: exercise-test-builder}


Enlarge the Test::MyTools to include a test function
called my_any_num that works like is_any but compares the
values as numbers.
Write test script that uses this function.




## Exercise: add is_max
{id: exercise-test-builder-is-max}


Add another function called is_max that gets a number and
a reference to an array and will give you ok if the number
is really the max. (See List::Util for a max function)
What should it print on error?
Write test script that uses this function.




## Exercise: is_between
{id: exercise-is-between}


Add a function to Test::MyTools called is_between that will check if
the received value is between two given values:
is_between($lower_limit, $real_value, $upper_limit, $name);




## Exercise: test sum
{id: exercise-test-sum}


Write a test for the sum() function without parameter.
Normally it should return 0 and should not give any warnings.
So try to write a test that check there is no warning in this call
but mark it as TODO as it is currently failing but we have decided to
postpone it fix after we finish more urgent tasks.




## Exercise: Test::Exception
{id: exercise-test-exception}
{i: Test::Exception}

```
Similar to Test::Warn there is also a module called Test::Exception
to test for calls to die.
Try calling fibonacci(); and writing a test for it.
```
![](examples/test-perl/t/fibonacci_dies.t)
![](examples/test-perl/t/fibonacci_dies.out)



## Solution: is_between
{id: solution-is-between}

```
Maybe this is better:

is_between($lower_limit, $oper1, $real_value, $oper2, $upper_limit, $name)
```
![](examples/test-perl/t/dice_range.t)
![](examples/test-perl/t/lib/Test/Range.pm)


## Solution: test sum
{id: solution-test-sum}
![](examples/test-perl/t/empty_sum.t)
![](examples/test-perl/t/fibonacci_test_die.t)


## Perl Best Practices
{id: perl-best-practices}
{i: PBP}
{i: Perl::Critic}

{aside}

The book Perl Best Practices of Damian Conway provides a reasonable
set of guidelines on how to write a Perl program. While you might not
want to follow each guideline as it is written in the book it can be a
very good starting point. It is certainly much better than the current
practice of letting everyone write whatever she wants. This is good in
the general terms and when we are talking about individual projects.
Within a project (or within a company) it makes a lot of sense to stick
to some guidelines.
{/aside}


{aside}

So reading the book is good.
In addition there is a module called Perl::Critic by
Jeffrey Ryan Thalhammer and currently maintained by Elliot Shank that can
check each one of the practices Damian suggest. Not only that.
{/aside}


{aside}

There is also a module called Test::Perl::Critic that takes the functions of
Perl::Critic and turns them into Test::Builder based functions. So you can
get ok/not ok output from them.
{/aside}


{aside}

Using them in Perl projects can help improving the code base very quickly.
{/aside}


{aside}

You can also configure the module to check each one of the "practices"
according to the style accepted in your company.
{/aside}

```
Perl::Critic
Test::Perl::Critic
```
![](examples/test-perl/t/99-critic.t)


## Why number the test files?
{id: why-number-the-test-files}

 
By default prove will run the test script in ABC order.
One common way to make sure the test scripts run in a certain order is to name the files



```
00-basic.c
```


## Test::Differences
{id: test-differences}
{i: Test::Differences}
{i: cmp_deeply}

[Test::Differences](https://metacpan.org/pod/Test::Differences) provides UNIX-like
diff output when strings are not matching.

![](examples/test-perl/t/test_differences.t)

```
perl examples/test-perl/t/test_differences.t
```


![](examples/test-perl/t/test_differences.t.out)


## Test::Deep
{id: test-deep}


[Test::Deep](https://metacpan.org/pod/Test::Deep) by Fergal Daly provides various function
testing data structure is much better way than is_deeply of Test::More.
We return to the example examples/test-perl/lib/MyBugs.pm

* cmp_deeply
* cmp_bag
* cmp_set
* cmp_methods

![](examples/test-perl/t/test_deep.t)
![](examples/test-perl/t/test_deep.out)
![](examples/test-perl/t/bag.t)


## Test::File
{id: test-file}
{i: Test::File}
{i: file_exists_ok}
{i: file_empty_ok}
{i: file_size_ok}


[Test::File](https://metacpan.org/pod/Test::File) of brian d foy provides functions for testing meta
information about files

* file_exists_ok( FILENAME [, NAME ] )
* file_empty_ok( FILENAME [, NAME ] )
* file_size_ok( FILENAME, SIZE [, NAME ] )
* ...



## Test::LongString
{id: test-longstring}
{i: Test::LongString}
{i: like_string}
{i: is_string}


[Test::LongString](https://metacpan.org/pod/Test::LongString) of Rafael Garcia-Suarez for better error reporting
when comparing strings. Especially long strings.


![](examples/test-perl/t/test_longstring.t)
![](examples/test-perl/t/test_longstring.out)


## Test::Most
{id: test-most}
{i: Test::Most}
{i: die_on_fail}


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


![](examples/test-perl/t/test_most.t)

```
prove examples/test-perl/t/test_most.t
DIE_ON_FAIL=1 prove examples/test-perl/t/test_most.t
BAIL_ON_FAIL=1 prove examples/test-perl/t/test_most.t
```


## Test::Trap
{id: test-trap}
{i: Test::Trap}


Trap exit codes, exceptions, output.

Or use Capture::Tiny and then interrogated the returned values.

## Test::Fatal
{id: test-fatal}
{i: Test::Fatal}


For testing code with exceptions (instead of Test::Exception)
see [Test::Fatal](https://metacpan.org/pod/Test::Fatal).


## Test::XPath
{id: test-xpath}
{i: Test::XPath}
{i: XML}

[Test::XPath](https://metacpan.org/pod/Test::XPath)


## Sample script for testing Client-Server
{id: testing-client-server}

![](examples/test-perl/client_server.t)


## Sample script for testing Client-Server Win32
{id: testing-client-server-win32}

![](examples/test-perl/client_server_win32.t)


## Exercise for Test::Builder
{id: exercise-test-builder2}

Given the following convenience function (exported by MyTools.pm ),
please test if it works properly.

```
my $fh = get_fh(MODE, FILENAME)

my $in = get_fh('&lt;',  'data.txt');
```

## Exercise: Math::RPN
{id: exercise-math-rpn}

Take the Math::RPN exercise and add further tests:

* Test at least some of the warnings.
* Make sure nothing else generates warnings

## Exercise: exceptions
{id: exercise-test-fatal}

Take the earlier exercise where we used Test::Exception and see how to rewrite it using
Test::Fatal and/or Test::Trap.

## Solution
{id: solution-test-builder}

![](examples/test-perl/t/get_fh.t)



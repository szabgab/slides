# Mocking
{id: mocking}

## What is Mocking?
{id: what-is-mocking}

* It is a term we often use for various types of **test doubles**....

## Test Doubles
{id: test-doubles}

* Mocks
* Spies
* Stubs
* Fakes
* Dummies

* [Gerard Meszaros - xUnit Test Patterns](https://martinfowler.com/books/meszaros.html)
* [Test Double explained by Martin Fowler](https://martinfowler.com/bliki/TestDouble.html)

## Test Doubles explained
{id: test-doubles-explained}

**Dummy** objects are passed around but never actually used.

**Fakes** - Working implementation, but much more simple than the original
* An in-memory list of username/password pairs that provide the authentication.
* A database interface where data stored in memory only, maybe in a hash or an in-memory SQLite DB.

**Mocks** - Mocks are objects that register calls they receive, but do not execute the real system behind.

**Stubs** - Stub is an object that holds predefined data and uses it to answer calls during tests.
* A list of "random values".
* Responses given to prompt.

**Spies** usually record some information based on how they were called and then call the real method. (or not)

##  What is Monkey Patching?
{id: mocking-vs-monkey-patching}

* It is just another name of mocking.
* .. or test doubles.

* Replace some internal part of a module or class for the sake of testing.
* Monkey Patching is probably a subset of Mocking, but who knows?

## When is mocking useful?
{id: when-is-mocking-useful}

* TDD - Test Driven Development

* Write application agains API that is not ready yet or not controlled by you.

* Replace a complex object with a simpler one.

* Isolate parts of the system to test them on their own.

* Speed up tests (e.g. eliminate remote calls, eliminate database calls).

* Simulate cases that are hard to replicate. (What if the other system fails?)

* Unit tests.

## Mocking in various situations
{id: mocking-in-various-situations}

* Random
* Time
* IO (print)

* External calls.
* Method calls.
* A whole class.


## Application using random
{id: application-using-random}

![](examples/mock-random/lib/MyRandomApp.pm)
![](examples/mock-random/bin/dice.pl)

```
perl -Ilib bin/dice.pl
```

## Mock random generator in BEGIN
{id: mock-random-generator-in-beging}

![](examples/mock-random/t/test-begin.t)

```
prove -lv t/test-begin.t
```

## Mock random generator Mock::Sub
{id: mock-random-generator-with-mock-sub}

* [Mock::Sub](https://metacpan.org/pod/Mock::Sub)

![](examples/mock-random/t/test-mock-sub.t)

```
prove -lv t/test-mock-sub.t
```

## Function that (also) writes to STDOUT or STDERR
{id: function-that-writes-to-stdout-or-stderr}

{aside}
There are many cases when we encounter a function that does more than one things. For example in the following simplified
example we have a function that both makes some (simple) mathematical calculation and prints to the screen.
For added fun it also prints to the Standard Error channel.

We will probably want to refactor it to separate the concerns of calculating and IO, but first we'd like to write a unit-test.

In this example we use the capture function of the Capture::Tiny module that will capture and return as a string everything that is
printed to STDOUT and STDERR. (It could also capture the exit value of an external call, but this is not relevant in our case.

The whole code is wrapped in a subtest so the external $result variable will be lexically scoped.
{/aside}

![](examples/capture-stdout-stderr/lib/CalcOutput.pm)

![](examples/capture-stdout-stderr/bin/calc.pl)

```
perl -Ilib bin/calc.pl 7 8
```

## Capture STDOUT and STDERR in functions call
{id: capture-stdout-and-stderr-in-function-call}
{i: Capture::Tiny}
{i: capture}

* [Capture::Tiny](https://metacpan.org/pod/Capture::Tiny)

![](examples/capture-stdout-stderr/t/test.t)

```
prove -lv t/test.t
```

## Testing time-dependent module
{id: testing-time-dependent-module}

Module that must behave differently on a certain day:
* every day do A, on Sunday do B)
* On January 1 do something special
* On April 1 do something special


Code that maintains a session
* Test if the timeout works well


## Module with session timeout
{id: module-with-session-timeout}

![](examples/mock-elapsed-time/lib/MySession.pm)

![](examples/mock-elapsed-time/bin/timer.pl)

```
perl -Ilib bin/timer.pl
```

## Mocking Time
{id: mocking-time}
{i: Test::MockTime}
{i: time}

* [Test::MockTime](https://metacpan.org/pod/Test::MockTime)

![](examples/mock-elapsed-time/t/time.t)

{aside}
Make sure you load Test::MockTime before you load the module under testing. Otherwise the time function in that module won't be mocked.
{/aside}


## Mocking class
{id: mocking-class}


![](examples/mock-class/lib/MyClass.pm)

![](examples/mock-class/lib/MyApp.pm)

![](examples/mock-class/t/myapp-mocked.t)
![](examples/mock-class/t/myapp-real.t)
![](examples/mock-class/t/myclass-mocked.t)
![](examples/mock-class/t/myclass-real.t)


## Mocking MetaCPAN::Client
{id: mocking-metacpan-client}

![](examples/mock-metacpan/lib/MyMetaCPAN.pm)
![](examples/mock-metacpan/bin/my_metacpan_client.pl)
![](examples/mock-metacpan/t/metacpan.t)

## Override printing functions (mocking)
{id: testing-override-printing-functions}
{i: redefine}

{aside}
Sometimes there are functions that print directly to the screen.

The program could be tested as an external application or we can redirect the
STDOUT to a scalar variable in the memory of perl but  it might be cleaner
to replace the display function, capture the data in a variable
and then check that variable.
{/aside}

![](examples/test-perl/t/display.t)

## Monkey Patching
{id: monkey-patching}

![](examples/mock/Monkey.pm)
![](examples/mock/check_monkey.t)

```
1..4
ok 1 - bananas
ok 2 - is_hungry
not ok 3 - bananas
#   Failed test 'bananas'
#   at check_monkey.t line 13.
#          got: '9'
#     expected: '10'
not ok 4 - bananas
#   Failed test 'bananas'
#   at check_monkey.t line 15.
#          got: '8'
#     expected: '9'
# Looks like you failed 2 tests of 4.
```
![](examples/mock/patch_monkey.t)

```
1..5
ok 1 - bananas
ok 2 - is_hungry
ok 3 - eat called
ok 4 - bananas
ok 5 - bananas
```


## Mocking function of external call
{id: mocking-function}
{i: Test::Mock::Simple}
![](examples/mock/MyWebAPI.pm)
![](examples/mock/webapi.t)
![](examples/mock/webapi_mock.t)


## Mocking exception
{id: mocking-function-exception}
![](examples/mock/webapi_mock_exception.t)


## Mocking function error
{id: mocking-function-error}
![](examples/mock/webapi_mock_error.t)


## Mocking get in LWP::Simple
{id: mocking-get-in-lwp-simple}
![](examples/mock/webapi_mock_lwp_simple.t)




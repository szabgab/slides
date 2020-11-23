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

## Code with STDIN
{id: code-with-stdin}

![](examples/mock-stdin/lib/MyEcho.pm)

![](examples/mock-stdin/bin/echo.pl)

```
perl -Ilib bin/echo.pl
```

## Mock STDIN
{id: mock-stdin}

![](examples/mock-stdin/t/echo.t)


## Simple game to test
{id: simple-game-to-test}

![](examples/test-game/game_one.pl)

## Test simple game (small)
{id: test-simple-game-small}

![](examples/test-game/test_game_one_small.t)


## Test simple game (big)
{id: test-simple-game-big}
![](examples/test-game/test_game_one_big.t)


## Test simple game (exact)
{id: test-simple-game-exact}

![](examples/test-game/test_game_one_exact.t)

## Exercise: test game
{id: exercise-test-game}

![](examples/test-game/game_loop.pl)

## Testing time-dependent module
{id: testing-time-dependent-module}

Module that must behave differently on a certain day:
* every day do A, on Sunday do B.
* On January 1 do something special.
* First workday of every month pay salary.
* On April 1 do something special.

Code that maintains a session
* Test if the timeout works well.


## Module with operation based on date
{id: module-with-operation-based-on-date}

![](examples/mock-time/lib/MyDaily.pm)

![](examples/mock-time/bin/daily.pl)

## Mocking fixed absolute time
{id: mocking-fixed-absolute-time}

![](examples/mock-time/t/daily.t)


## Module with session timeout
{id: module-with-session-timeout}

![](examples/mock-elapsed-time/lib/MySession.pm)

![](examples/mock-elapsed-time/bin/timer.pl)

```
perl -Ilib bin/timer.pl
```

## Mocking relative Time
{id: mocking-relative-time}
{i: Test::MockTime}
{i: time}

* [Test::MockTime](https://metacpan.org/pod/Test::MockTime)

![](examples/mock-elapsed-time/t/time.t)

{aside}
Make sure you load Test::MockTime before you load the module under testing. Otherwise the time function in that module won't be mocked.
{/aside}


## Mocking class
{id: mocking-class}

* We have a class (our own code, or some 3rd party code)

![](examples/mock-class/lib/SomeClass.pm)

## Application using the class
{id: application-using-the-class}

* This is the application that uses the class

![](examples/mock-class/lib/MyApp.pm)

* How can we test that our application will report a correct error message if the 3rd party application breaks (instead of rasing an exception)?

## Testing the 3rd party class
{id: testing-the-3rd-party-class}

* This is probably not very interesting, just testing an object-oriented module.

![](examples/mock-class/t/someclass-real.t)
![](examples/mock-class/t/someclass-mocked.t)


## Testing our app using the 3rd party class
{id: testing-our-app-real}

![](examples/mock-class/t/myapp-real.t)

## Testing our app mocking the 3rd party class
{id: testing-our-app-mock}

![](examples/mock-class/t/myapp-mocked.t)


## Mocking function of external web call
{id: mocking-function}
{i: Test::Mock::Simple}

* We have an application that uses LWP::Simple
* It gets a list of strings and tells us how many times each string appears on that web page.
* We'll talk about the commented out code a bit later.

![](examples/mock-lwp/lib/MyWebAPI.pm)

![](examples/mock-lwp/bin/count.pl)

```
perl -Ilib bin/count.pl https://code-maven.com/ perl python Java
```

## Test the application end-to-end
{id: end-to-end-test}

* This is a very old test, and even then it did not work
* As it assumes a given content of that page

![](examples/mock-lwp/t/webapi.t)

## Mocked web test
{id: mocked-web-test}

* Here we need to mock the get function as it is already in the MyWebAPI module
* If we mocked the one inside LWP::Simple that would not impact the one we already have in the MyWebAPI module.

![](examples/mock-lwp/t/webapi_mock.t)

## Mocking to reproduce error in our function
{id: mocking-function-error}

* Someone reported that in certain cases the count does not work properly.
* For example when the multi-word name is spread to multiple lines (so there is a newline).
* This is how we can test

![](examples/mock-lwp/t/webapi_mock_error.t)

## Mocking exception
{id: mocking-function-exception}

* What if the `get` function raises an exception, how will our code handle?
* Hint: it does not, so this test will break
* But this is how we could test what will happen in that case without trying to figure out how to reliably create one using the real LWP::Simple

![](examples/mock-lwp/t/webapi_mock_exception.t)

## Using MetaCPAN::Client
{id: using-metacpan-client}

![](examples/mock-metacpan/lib/MyMetaCPAN.pm)
![](examples/mock-metacpan/bin/my_metacpan_client.pl)

## Mocking MetaCPAN::Client
{id: mocking-metacpan-client}

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

## Test STDIN
{id: test-stdin}

![](examples/test-stdin/rectangle.pl)
![](examples/test-stdin/test.t)

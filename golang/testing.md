# Testing
{id: testing}

## Testing in Go
{id: testing-in-go}

{aside}
There are a number of convetions on how to write tests in Go.
{/aside}

* Tests files have a suffix **_test** like `app_test.go`.
* They have functions where the name starts with **Test**  like `TestSometing`.
* You can run the tests by typing `go test` in the directory of the project.


## Testing modules
{id: testing-modules}

{aside}
There are a number of packages that will help you write tests. In this chapter we'll look at the standard module `testing` that comes with every installation
of Go. Then later we are going to take a look at a number of other packages that are listed here. 
{/aside}

* Standard [testing](https://golang.org/pkg/testing/)

* [Convey](http://goconvey.co/)
* [Convey in Github](https://github.com/smartystreets/goconvey)

* [testify](https://github.com/stretchr/testify)


* [is](https://github.com/matryer/is) by Mat Ryer
* [moq](https://github.com/matryer/moq) by Mat Ryer


## Simple example with testing
{id: simple-test}
{i: testing}
{i: test}

{aside}
In this example we have a single-file Go "application" called `comp.go` that has a `main` function and an additional function called `add` that is supposed to add two integers together and return the result. If you look carefully you might notice that we have a typo in the code, but that's there on purpose. Our goal now is to see how can we verify this code.
{/aside}

![](examples/simple-test/comp.go)

{aside}
So we have an additional file called `comp_test.go`. This belongs to the same `main` package and it imports the `testing` package. It has a function called `TestAdd` that received a pointer to a `testing.T` instance. Remember, not we are going to call this function, but the testing system of Go.
Inside the function we have a call to `t.Log` which is just some logging information. Then we call the `add` function that resides in the same package but in the main file. We pass two numbers an accept the results. This is how we would normally use the functions.
{/aside}

{aside}
Then we have the interesting part. We compare the received value with the expected value which is 4. If they are not the same, we call the `t.Error` function to report the problem. We can put any text there.
{/aside}

{aside}
That's it.
{/aside}

![](examples/simple-test/comp_test.go)


We can now run the tests:

```
go test
```

to get the following output:

![](examples/simple-test/test.out)

We could also pass the `-v` flag to get a bit more verbose output.

```
go test -v
```

![](examples/simple-test/test_v.out)


## Test with failure
{id: test-with-failure}
{i: testing}
{i: test}

{aside}
The previous test was great, but soon people will report that the `add` function does not always work. In fact they will report it never works properly.
If you are lucky they will also supply you with a case for which it did not work properly so you can try to reproduce the problem. You do that by writing another
test case:
{/aside}

The code is still the same:

![](examples/test-fail/comp2.go)

But now we have two separate test cases:

![](examples/test-fail/comp2_test.go)

If we run the tests now:

```
go test
```

We get a failure report in which we can see the line number of the failure and the message. If we prepare our message well, then wen can immediately see the actual value and the expected value that might be able to help us locate the problem.

![](examples/test-fail/test2.out)

If this is not enough we can ask for more verbose output:

```
go test -v
```

![](examples/test-fail/test2_v.out)


## Run selected test functions
{id: run-selected-test-functions}

{aside}
At this point you have basically two choices. Assuming you are sure the test is correct, either you can fix the code now,
or you can decide that you delay fixing this code as you have more urgent things to do.
{/aside}

{aside}
If and when you start fixing the code you will have to run the tests again and again. If you have many tests this can be time consuming.
You might want to run the specific test that is currently failing.  You can do this using the `-run` flag.
{/aside}

Only the TestAdd1:

```
go test -run TestAdd1
```

Only the TestAdd2:

```
go test -run TestAdd2
```

Both:

```
go test -run TestAdd
```

In general you can use regexes to match the names of the test functions you would like to run:

```
go test -run "^(func_test_name)$"
```


## Exercise: Test Anagram
{id: exercise-test-anagram}

* Given the following code, that checks if two strings are [anagrams](https://en.wikipedia.org/wiki/Anagram), write tests that verify the function.

![](examples/anagram/anagram.go)

## Exercise: Test Calculator
{id: exercise-test-calculator}

Given the following program with the calc function, write some tests verifying the function.

![](examples/test-calc/calc.go)


## Exercise: statistics
{id: exercises-statistics}

* Take the following program, factor out a function called stats that will get a slice of numbers and return the min, max, total, and average.

* Write test that will check the results

![](examples/statistics/statistics.go)


## Solution: Test Anagram
{id: solution-test-anagram}

![](examples/anagram/anagram_test.go)

## Solution: Test Calculator
{id: solution-test-calculator}

![](examples/test-calc/calc_test.go)

## Solution: statistics
{id: solution-statistics}

![](examples/test-statistics/stats.go)
![](examples/test-statistics/stats_test.go)

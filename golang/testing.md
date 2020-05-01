# Testing
{id: testing}

## Testing in Go
{id: testing-in-go}

* Tests files have a suffix **_test**
* They have functions where the name starts with **Test**
* You can run the tests by typing `go test` in the directory of the project.


## Testing modules
{id: testing-modules}

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

![](examples/simple-test/comp.go)

![](examples/simple-test/comp_test.go)

To run the tests:

```
go test
```

![](examples/simple-test/test.out)


```
go test -v
```

![](examples/simple-test/test-v.out)

## Test with failure
{id: test-with-failure}
{i: testing}
{i: test}

![](examples/test-fail/comp2.go)

![](examples/test-fail/comp2_test.go)

```
go test
```

![](examples/test-fail/test.out)

```
go test -v
```

![](examples/test-fail/test-v.out)

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


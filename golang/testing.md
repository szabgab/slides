# Testing
{id: testing}

## Testing in Go
{id: testing-in-go}

* Tests files have a suffix **_test**
* They have functions where the name starts wirh **Test**

* Tests a simple mathematical function
* What if a test fails?
* What if we cannot fix a test immediately?

## Simple test
{id: simple-test}
{i: test}

![](examples/simple_test/comp.go)

![](examples/simple_test/comp_test.go)

To run the tests:

```
go test
get test -v
```

## Testing Notes
{id: testing-notes}

https://github.com/stretchr/testify

go get github.com/stretchr/testify
to add asserts

* [](https://www.youtube.com/watch?v=ttKgBttwzrg)
* [](https://www.youtube.com/watch?v=_B_vCEiO4mA)


Mat Ryer
* [is](https://github.com/matryer/is)
* [moq](https://github.com/matryer/moq)

## Anagram
{id: anagram}

![](examples/anagram/anagram.go)

![](examples/anagram/anagram_test.go)

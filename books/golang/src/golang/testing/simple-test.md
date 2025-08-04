# Simple example with testing

* testing
* test


In this example we have a single-file Go "application" called `comp.go` that has a `main` function and an additional function called `add` that is supposed to add two integers together and return the result. If you look carefully you might notice that we have a typo in the code, but that's there on purpose. Our goal now is to see how can we verify this code.


{% embed include file="src/examples/simple-test/comp.go" %}


So we have an additional file called `comp_test.go`. This belongs to the same `main` package and it imports the `testing` package. It has a function called `TestAdd` that received a pointer to a `testing.T` instance. Remember, not we are going to call this function, but the testing system of Go.
Inside the function we have a call to `t.Log` which is just some logging information. Then we call the `add` function that resides in the same package but in the main file. We pass two numbers an accept the results. This is how we would normally use the functions.



Then we have the interesting part. We compare the received value with the expected value which is 4. If they are not the same, we call the `t.Error` function to report the problem. We can put any text there.



That's it.


{% embed include file="src/examples/simple-test/comp_test.go" %}


We can now run the tests:

```
go test
```

to get the following output:

{% embed include file="src/examples/simple-test/test.out" %}

We could also pass the `-v` flag to get a bit more verbose output.

```
go test -v
```

{% embed include file="src/examples/simple-test/test_v.out" %}




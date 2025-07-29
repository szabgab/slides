# Why use context managers?

In certain operations you might want to ensure that when the operation is done there will be an opportunity to clean up
after it. Even if decided to end the operation early or if there is an exception in the middle of the operation.

In the following pseudo-code example you can see that `cleanup` must be called both at the end and before the `early-end`, but
that still leaves the bad-code that raises exception avoiding the cleanup. That forces us to wrap the whole section in a try-block.

```
def sample():
    start
    do
    do
    do
    do
    cleanup
```

What is we have some conditions for early termination?

```
def sample():
    start
    do
    do
    if we are done early:
        cleanup
        return # early-end
    do
    do
    cleanup
```

What if we might have an exception in the code?

```
def sample():
    start
    try:
        do
        do
        if we are done early:
            cleanup
            return early-end
        do
        bad-code    (raises exception)
        do
        cleanup
    finally:
        cleanup
```

It is a lot of unnecessary code duplication and we can easily forget to add it in every location where we early-end our code.



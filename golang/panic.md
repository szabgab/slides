# Panic (Exception handling)
{id: panic}

## Panic
{id: go-panic}

{aside}
In many other programming languages (e.g Python, Java) if the code encounters a problem it raises an exception that if not treated properly will stop the execution.
In some other programming languages (e.g. C, Perl) functions return an error code when something does not work.
{/aside}

{aside}
Go leans towards the languages that return error, though it usually returns it as a separate value.
In addition Go has a concept similar to exceptions, but is rarely used and to reflect the different usage it also has a different name. It is called `panic`.
{/aside}

{aside}
In Go if you try to open a file and you fail, this is considered as a normal situation - not an exceptional one, hence Go will return a representation of the
error but won't try to stop the program. On the other hand if you try to divide by 0, Go will freak out and `panic`.
{/aside}

{aside}
Let's see how does that work.
{/aside}

![](examples/go-panic/go_panic.go)
![](examples/go-panic/go_panic.out)


## We Panic
{id: we-panic}
{i: panic}
{i: raise}

{aside}
We can also initiate our own "panic" by calling the `panic` function.
{/aside}

![](examples/we-panic/we_panic.go)
![](examples/we-panic/we_panic.out)

## Turn error into panic when port is used
{id: panic-when-port-is-used} 

![](examples/panic-http/panic_http.go)

## Panic after defer
{id: panic-after-defer}
{i: defer}

![](examples/panic-after-defer/panic_after_defer.go)
![](examples/panic-after-defer/panic_after_defer.out)

## Recover (and re-panic)
{id: recover}
{i: recover}
{i: try}
{i: catch}

![](examples/recover/recover.go)
![](examples/recover/recover.out)

## Recover from deep panic
{id: recover-from-deep-panic}

![](examples/deep-panic/deep_panic.go)
![](examples/deep-panic/deep_panic.out)

## Convert panic to returned error
{id: convert-panic-to-returned-error}

![](examples/deep-panic-return/deep_panic_return.go)
![](examples/deep-panic-return/deep_panic_return.out)

## Exercise: read several files
{id: exercise-read-several-files}

Given several files where each file contains two numbers separated by a comma,
print out the result of dividing the first number by the second number.
e.g. 

```
go run read_several_files.go a.txt b.txt c.txt d.txt
```

should work.

![](examples/read-several-files/a.txt)
![](examples/read-several-files/c.txt)
![](examples/read-several-files/d.txt)


## Solution: read several files
{id: solution-read-several-files}


![](examples/read-several-files/read_several_files.go)
![](examples/read-several-files/read_several_files.out)



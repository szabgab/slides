# Panic (Exception handling)
{id: panic}



## Panic
{id: go-panic}

![](examples/go-panic/go_panic.go)
![](examples/go-panic/go_panic.out)


## We Panic
{id: we-panic}
{i: panic}

![](examples/we-panic/we_panic.go)
![](examples/we-panic/we_panic.out)

## Panic when port is used
{id: panic-when-port-is-used} 

![](examples/panic-http/panic_http.go)

## Panic after defer
{id: panic-after-defer}

![](examples/panic-after-defer/panic_after_defer.go)
![](examples/panic-after-defer/panic_after_defer.out)

## Recover (and re-panic)
{id: recover}
{i: recover}

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



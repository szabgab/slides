# Time
{id: time}

## Monolitic vs Wallclock time
{id: monolitic-vs-wallclock-time}

* Wallclock - the real time, might suddently change even in negative way if the clock is updated.
* Monolitic - always growth.

* They are both stored

## Time example
{id: time-example}
{i: time}
{i: Now}
{i: Unix}

{aside}
The `Now` function of the `time` package will return a representation of the current time.
When printed it will show well formatted datetime string, but we can also use the Unix and UnixNano functions
to the the time elapsed since the epoch in seconds and nanoseconds respectively.
{/aside}

![](examples/time/time.go)
![](examples/time/time.out)


## Nanoseconds
{id: nano-seconds}
{i: UnixNano}

![](examples/nano/nano.go)
![](examples/nano/nano.out)


## sleep and elapsed time
{id: sleep-and-elapsed-time}
{i: Sleep}
{i: Now}
{i: Sub}

![](examples/sleep/sleep.go)
![](examples/sleep/sleep.out)


## Time format
{id: time-format}

![](examples/time-format/time_format.go)
![](examples/time-format/time_format.out)

## Date Arithmetic
{id: date-arithmetic}

![](examples/date-arithmetic/date_arithmetic.go)
![](examples/date-arithmetic/date_arithmetic.out)


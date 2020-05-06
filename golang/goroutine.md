# Goroutine
{id: goroutine}

## Without goroutine
{id: without-goroutine}

{aside}
Regular functions calls are executed sequentially. Each call can only start after all the previous calls have finished.
{/aside}

![](examples/without-goroutine/without_goroutine.go)
![](examples/without-goroutine/without_goroutine.out)

## goroutine example
{id: goroutine-example}
{i: go}

{aside}
If we call them with the `go` keyword they become go-routines and they start to work in parallel. So in this example you can see
the output is mixed up. 
{/aside}

![](examples/goroutine/goroutine.go)
![](examples/goroutine/goroutine.out)


## goroutine not finished yet
{id: goroutine-not-finished-yet}
{i: go}

{aside}
In this example we told the first call to run 30 times, but it could only run 6 times before the main part of the code finished that killed the whole process. So we need to be able to wait till the go-routine finishes.
{/aside}

![](examples/goroutine-not-finished-yet/goroutine_not_finished_yet.go)
![](examples/goroutine-not-finished-yet/goroutine_not_finished_yet.out)


## goroutine no wait
{id: groutine-no-wait}

{aside}
A simpler and maybe clearer example for not waiting.
{/aside}

![](examples/goroutine-nowait/goroutine_nowait.go)
![](examples/goroutine-nowait/goroutine_nowait.out)

## Wait for goroutines
{id: wait-for-goroutines}
{i: sync}
{i: WaitGroup}

{aside}
{/aside}

![](examples/wait-for-goroutines/wait_for_goroutines.go)

## Return date from goroutines
{id: return-data-from-goroutines}

![](examples/return-data-from-goroutines/return_data_from_goroutines.go)


## Channels
{id: channels}

{aside}
Either the sender or the receiver will be blocked till the other side is also ready.
Only when they are aligned the message will be sent and then both will continue running.
{/aside}

![](examples/channels/channels.go)

## TODO: select
{id: select}


* [video](https://www.youtube.com/watch?v=LvgVSSpwND8)

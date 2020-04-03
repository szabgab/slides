# goroutine
{id: goroutine}


## goroutine example
{id: goroutine-example}
{i: go}

![](examples/goroutine/goroutine.go)
![](examples/goroutine/goroutine.out)


## Wait for goroutines
{id: wait-for-goroutines}
{i: sync}
{i: WaitGroup}

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

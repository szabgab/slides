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

## Global waitgroup for goroutines
{id: global-waitgroups}
{i: sync}
{i: WaitGroup}
{i: Add}
{i: Wait}
{i: Done}

![](examples/global-wait-group/global_wait_group.go)
![](examples/global-wait-group/global_wait_group.out)


## Wait for goroutines
{id: wait-for-goroutines}
{i: sync}
{i: WaitGroup}
{i: Add}
{i: Wait}
{i: Done}

{aside}
{/aside}

![](examples/wait-for-goroutines/wait_for_goroutines.go)
![](examples/wait-for-goroutines/wait_for_goroutines.out)


## Return data from goroutines
{id: return-data-from-goroutines}

![](examples/return-data-from-goroutines/return_data_from_goroutines.go)
![](examples/return-data-from-goroutines/return_data_from_goroutines.out)

## Counter - shared variable
{id: counter}

![](examples/counter/counter.go)
![](examples/counter/counter.out)

## Mutex
{id: mutex}

```
sync.RWMutex
RLock()
Lock()
RUnlock
```


## Channels
{id: channels}

{aside}
Either the sender or the receiver will be blocked till the other side is also ready.
Only when they are aligned the message will be sent and then both will continue running.
{/aside}

![](examples/channels/channels.go)
![](examples/channels/channels.out)


## Channels are blocking
{id: channels-are-blocking}

![](examples/blocking-channels/blocking_channels.go)
![](examples/blocking-channels/blocking_channels.out)


## Channel capacity - buffered channel
{id: channel-capacity}

![](examples/channel-capacity/channel_capacity.go)


## Channel with loop
{id: channel-with-loop}

![](examples/channel-with-loop/channel_with_loop.go)
![](examples/channel-with-loop/channel_with_loop.out)


## Pipeline map
{id: pipeline-map}

![](examples/pipeline-map/pipeline_map.go)

## Pipeline filter
{id: pipeline-filter}

![](examples/pipeline-filter/pipeline_filter.go)

## TODO: Pipelines
{id: pipelines}

![](examples/pipeline/pipeline.go)

## Fibonacci goroutine
{id: fibonaci-goroutine}

![](examples/fibonacci-goroutine/fibonacci_goroutine.go)


## Loop from a channel
{id: loop-from-a-channel}

![](examples/loop-channel/loop_channel.go)

## Select channel
{id: select-channel}
{i: select}

![](examples/select-channel/select_channel.go)

## Delayed start
{id: delayed-start}

![](examples/delayed-start/delayed_start.go)

## Job pool
{id: job-pool}

![](examples/random-jobs/random_jobs.go)


## Check for race conditions
{id: check-for-race-conditions}

```
go run -race app.go
```


## Stand alone web application
{id: stand-alone-web-application}

![](examples/stand-alone/stand_alone.go)

## Maximum processes
{id: maximum-processes}

```
runtime.GOMAXPROCS(1) // set max to be used.
```

```
runtime.GOMAXPROCS(-1) // ask how many are there?
```

## Exercise: Collect data from urls
{id: exercise-collect-data-from-urls}

Given a file with a list of URLs, fetch each one of the pages and print out the size
of each page. (For a bit more complex exercise, print out their title.)

![](examples/collect-data-from-urls/urls.txt)


## Exercise: Process multiple CSV files
{id: exercise-process-multiple-csv-files}

Given a bunch of csv files, read each file and tell us how many cells were in each file.


## Exercise: counter with lock
{id: exercise-counter-with-lock}

Take the example we saw earlier where we counted in several goroutines and apply the Mutex locks to ensure it does not miss a count. 

## Exercise: Fibonacci in parallel
{id: exercise-fibonacci-in-parallel}

Take the code from the Fibonacci example and check if you could run it in parallel.
Observe how does the CPU behave as the number of concurrent jobs increas from 1 to the number of cores you have and beyond.


## Solution: Collect data from urls
{id: solution-collect-data-from-urls}

![](examples/collect-data-from-urls/collect_data_from_urls.go)

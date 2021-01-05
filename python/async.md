# Asyncronus programming with AsyncIO
{id: async}

## Event loop
{id: event-loop}

* Single thread
* Single process
* Good for IO intensive tasks
* Cooperative Multitasking

## Use cases for Async
{id: use-cases-for-async}

* Downloading web pages
* Accessing APIs
* Accessing databases (especially on other servers)
* Reading files


## Print sync
{id: print-sync}

* First let's see a few small and useless demo
* In this example we wait and print, sequentially as we expect.

![](examples/async/print_sync.py)
![](examples/async/print_sync.out)

## Print async
{id: print-async}
{i: asyncio}
{i: async}
{i: await}
{i: gather}

* This is the almost the same example but we wait in parallel.
* Run both of these using the `time` command of Linux

![](examples/async/print_async.py)
![](examples/async/print_async.out)


## Sync sleep
{id: sync-sleep}

![](examples/async/sleep_sync.py)
![](examples/async/sleep_sync.out)

## Async sleep
{id: async-sleep}

![](examples/async/sleep_async.py)
![](examples/async/sleep_async.out)

## Sync sleep in loop
{id: sync-sleep-in-loop}

![](examples/async/sleep_loop.py)

## Async sleep in loop
{id: async-sleep-in-loop}

![](examples/async/async_sleep_loop.py)

![](examples/async/count.py)
![](examples/async/other_sleep.py)

## coroutines
{id: async-coroutines}

![](examples/async/co_routine.py)

## Async Tasks
{id: async-tasks}

![](examples/async/async_task.py)

    
## Passing the baton while sleeping 0 sec
{id: async-passing-the-baton}

![](examples/async/count_sleep_0.py)

## Async example
{id: async-example}

![](examples/async/example.py)



## Sync chores
{id: sync-chorse}

We have a number of household chores to do. Each takes a couple of seconds for a machine to do
while we have time to do something else. We also have one task, cleaning potatoes, that requires
our full attention. It is a CPU-intensive process.

We also have two processes depending each other. We can turn on the dryer only after the
washing machine has finished.

![](examples/async/sync_chores.py)
![](examples/async/sync_chores.out)


## Async chores
{id: async-chorse}
{i: async}
{i: await}


![](examples/async/async_chores.py)

From the output you can see that we noticed that the washing machine has finished only after we
have finished all the potatoes. That's becasue our potato cleaning process was a long-running
CPU-intensive process. This means the dryer only starts working after the potatoes are clean.

![](examples/async/async_chores.out)

If after cleaning each potato we look up for a fraction of a second, if we let the main loop run,
then we can notice that the washing machine has ended and we can turn on the dryer before continuing
with the next potato. This will allow the dryer to work while we are still cleaning the potatoes.

![](examples/async/async_chores_async.out)



## Explanation
{id: async-explanation}

* The feeling of parallelism
* Coroutines

* async/await

* Asynchronous
* non-blocking or synchronous vs blocking (aka "normal")

## Coroutines
{id: coroutines}

* Functions that can be suspended mid-way and allow other functions to run (a generator)

* `async def` is a native coroutine or asynchronous generator
* `async with`
* `async for`


## More about asyncio
{id: more-about-async}

* [AsyncIO in Real Python](https://realpython.com/async-io-python/)
* [asyncio](https://docs.python.org/library/asyncio.html)
* [aiohttp](https://docs.aiohttp.org/)
* [aiodns](https://pypi.org/project/aiodns/)
* [cchardet](https://pypi.org/project/cchardet/)
* [uvloop](https://github.com/MagicStack/uvloop)  drop-in replacement for the standard Python event-loop

Other libraries:

* [trio](https://github.com/python-trio/trio)
* [unsync](https://github.com/alex-sherman/unsync)

aiofiles  https://pypi.org/project/aiofiles/

* mongodb: [umongo](https://pypi.org/project/umongo/) called micromongo
* postgresql: [asyncpg](https://pypi.org/project/asyncpg/)
* mysql:
* redis: [asyncio-redis](https://pypi.org/project/asyncio-redis/)
* sqlite:


## Async files
{id: async-files}

* [aiofile](https://pypi.org/project/aiofile/)

* [aiofiles](https://pypi.org/project/aiofiles/)

![](examples/async/files_sync.py)
![](examples/async/files_async.py)

## Async http
{id: async-http-request}

![](examples/async/http_request_async.py)

## Sync http requests
{id: sync-http-requests}

![](examples/async/http_requests_sync.py)

## Async http requests
{id: async-http-requests}

![](examples/async/http_requests_async.py)

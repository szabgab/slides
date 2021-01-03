# Asyncronus programming with AsyncIO
{id: async}

## Sync sleep
{id: sync-sleep}

![](examples/async/sleep.py)

## Async sleep
{id: async-sleep}

![](examples/async/async_sleep.py)



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

* Single thread
* Single process
* The feeling of parallelism
* Coroutines


* async/await

* event loop

* Cooperative Multitasking

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

## Async files
{id: async-files}

![](examples/async/http_request.py)
![](examples/async/files.py)


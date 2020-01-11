# Asyncronus programming with AsyncIO
{id: async}

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


## Sync chores
{id: sync-chorse}

![](examples/async/sync_chores.py)
![](examples/async/sync_chores.out)

## Async chores
{id: async-chorse}
{i: async}
{i: await}

![](examples/async/async_chores.py)
![](examples/async/async_chores.out)


## More about asyncio
{id: more-about-async}

* [AsyncIO in Real Python](https://realpython.com/async-io-python/)
* [asyncio](https://docs.python.org/library/asyncio.html)


## Async files
{id: async-files}

![](examples/async/http_request.py)
![](examples/async/files.py)


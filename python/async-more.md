# Async more
{id: async-more}

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

* [greenlet](https://greenlet.readthedocs.io/en/latest/)

aiofiles  https://pypi.org/project/aiofiles/

* mongodb: [umongo](https://pypi.org/project/umongo/) called micromongo
* postgresql: [asyncpg](https://pypi.org/project/asyncpg/)
* mysql:
* redis: [asyncio-redis](https://pypi.org/project/asyncio-redis/)
* sqlite:

## unsync
{id: unsync}

* [unsync](https://github.com/alex-sherman/unsync)
* Can seemlessly run tasks in async, thread, or fork so different tasks can have the appropriate solution (e.g. CPU bound processes can use fork.)


## Async files
{id: async-files}

* [aiofile](https://pypi.org/project/aiofile/)

* [aiofiles](https://pypi.org/project/aiofiles/)

![](examples/async/files_sync.py)
![](examples/async/files_async.py)

## Async example
{id: async-example}

![](examples/async/example.py)




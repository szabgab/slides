# Threads
{id: python-threads}


## Python Threading docs
{id: python-threading}

* [threading](https://docs.python.org/library/threading.html)
* [Real Python](https://realpython.com/intro-to-python-threading/)
* [Wikibooks](https://en.wikibooks.org/wiki/Python_Programming/Threading)



## Threaded counters
{id: threaded-counter}
{i: threading}
{i: Thread}
{i: run}

![](examples/threads/mini_counter.py)
![](examples/threads/mini_counter.out)


## Simple threaded counters
{id: simple-threaded-counter}
{i: threading}
{i: Thread}
{i: run}

![](examples/threads/simple_counter.py)
![](examples/threads/simple_counter.out)


## Simple threaded counters (parameterized)
{id: simple-threaded-counter-parameterized}

The same as the previous one, but with parameters controlling the numbers
of threads and the range of the counter.

![](examples/threads/simple_counter_parameterized.py)
![](examples/threads/simple_counter_parameterized.out)


## Pass parameters to threads - Counter with attributes
{id: class-counter}
{i: threading}
{i: Thread}
{i: __init__}

![](examples/threads/counter.py)
![](examples/threads/counter.out)


## Create a central counter
{id: class-counter-central}

![](examples/threads/counter_central.py)


## Lock - acquire - release
{id: class-counter-central-lock}
{i: Lock}
{i: acquire}
{i: release}

![](examples/threads/counter_central_lock.py)

## Counter - plain
{id: counter-central-plain}

![](examples/threads/counter_central_plain.py)

## GIL - Global Interpreter Lock
{id: gil}

* Solves the problem introduced by having reference count.
* Not going away any time soon.

* [GIL wiki](https://wiki.python.org/moin/GlobalInterpreterLock)
* [GIL realpython](https://realpython.com/python-gil/)
* CPython and PyPy have it.
* Jython and IronPython don't have it.
* See [PEP 554 - Multiple Interpreters in the Stdlib](https://www.python.org/dev/peps/pep-0554/) for C extensions.


## Thread load
{id: thread-load}

![](examples/threads/thread_load.py)

![](examples/threads/thread_load_1.out)

![](examples/threads/thread_load_4.out)

## Exercise: thread files
{id: exercise-threads-queue}

* Get a list of files (from the current directory or from all the files in the "slides" repository.
* Process each file:
* 1. get size of file
* 2. count how many times each character appear in the file.
* The script should accept the number of threads to use.

## Exercise: thread URL requests.
{id: exercise-threads-url-requests}

In the following script we fetch the URLs listed in a file:

![](examples/parallel/urls.txt)

It takes about 1.5-2 sec / URL from home. (It depends on a lot of factors including your network connection.)

![](examples/parallel/fetch_urls.py)

Create a version of the above script that can use K threads.

## Exercise: thread queue
{id: exercise-thread-queue}

Write an application that handles a queue of jobs in N=5 threads.
Each job contains a number between 0-5.
Each thread takes the next element from the queue and sleeps for the given amount
of second (as an imitation of actual work it should be doing). When finished it checks
for another job. If there are no more jobs in the queue, the thread can close itself.

![](examples/threads/use_queue_skeleton.py)

If that's done, change the code so that each thread will generate a random
number between 0-5 (for sleep-time) and in 33% of the cases it will add it to the central queue
as a new job.


Another extension to this exercise is to change the code to limit the number of jobs each thread
can execute in its lifetime. When the thread has finished that many jobs it will quit and the
main thread will create a new worker thread.


## Solution: thread queue
{id: solution-thread-queue}

![](examples/threads/use_queue.py)

## Solution: thread URL requests.
{id: solution-threads-url-requests}

![](examples/parallel/fetch_urls_threads.py)

## Concurrency
{id: concurrency}

![](examples/threads/concur.py)

![](examples/threads/conc.py)


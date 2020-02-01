# Parallel
{id: python-parallel}

## Types of Problems
{id: problems-solved-by-parallel}

* CPU intensive application - use more of the cores to reduce the wallclock time.
* IO intensive applications - don't waste the CPU and wallclock time while waiting for the IO process.
* Interactive applications - make sure they are responsive during long operations.


## Types of solutions
{id: types-of-solutions}

* Number of processes (forking on Unix or spawning)
* Number of threads (Single threaded vs Multi-threaded)
* Asynchronous, non-blocking or synchronous vs blocking (aka "normal") Cooperative Multitasking

## How many parallels to use?
{id: how-many-parallels-to-use}

* First of all, I call them "parallels" as this applies to forks, threads, spawns, and even to async code.

* Overhead of creating new parallel.
* Overhead of communication (sending job input to parallel, receiving results).
* Total number of items to process.
* Time it takes to process an item.
* Distribution of processing times. (e.g. one long and many short jobs.)
* Number of cores (CPUs).


## Dividing jobs
{id: dividing-jobs}

* N items to process
* K in parallel

* Divide the items in K groups of size int(N/K) and int(N/K)+1.
* Create K parallels with one item each. When it is done, give it another item.
* Create K parallels with one item each. When done let it stop and create a new parallel.



## Performance Monitoring
{id: performance-monitoring}

* Linux, OSX: htop
* Windows: Performance Monitor




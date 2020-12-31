# Parallel
{id: python-parallel}

## Types of Problems
{id: problems-solved-by-parallel}

* CPU intensive application - use more of the cores to reduce the wallclock time.
* IO intensive applications - don't waste the CPU and wallclock time while waiting for the IO process.
* Interactive applications - make sure they are responsive during long operations.


## Types of solutions
{id: types-of-solutions}

* Number of processes (forking on Unix or spawning) (called multiprocessing in Python)
* Number of threads (Single threaded vs Multi-threaded)
* Asynchronous, non-blocking or synchronous vs blocking (aka "normal") Cooperative Multitasking

## Time slicing
{id: time-slicing}

* Whiel one program waits for IO, other program can run. This is called time-slicing.

* No Multitasking (e.g. MS DOS)
* Cooperative multitasking (program gives up the CPU by going into wait-state) (MS Windows 3.1) (if not, freezing)
* Pre-emptive multitasking (OS is responsible to switch between running processes) (Unix, Linux, Windows 95/NT and later)

## Concurrencies
{id: concurrencies}

* Trival case when there is no shared data
* Shared data (Syncing processes, memory allocation, scheduling)

* Deadlocks: when two processes are waiting for each  other
* Resource starvation: running out of memory, disk space, process count

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




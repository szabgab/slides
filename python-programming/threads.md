# Threads
{id: python-threads}

## Simple threaded counters
{id: simple-threaded-counter}
{i: threading}
{i: Thread}
{i: run}
![](examples/threads/simple_counter.py)


## Simple threaded counters (parameterized)
{id: simple-threaded-counter-parameterized}


The same as the previous one, but with parameters controlling the numbers
of threads and the range of the counter.


![](examples/threads/simple_counter_parameterized.py)


## Counter with attributes
{id: class-counter}
{i: threading}
{i: Thread}
{i: __init__}
![](examples/threads/counter.py)


## Create a central counter
{id: class-counter-central}
![](examples/threads/counter_central.py)


## Lock - acquire - release
{id: class-counter-central-lock}
{i: Lock}
{i: acquire}
{i: release}
![](examples/threads/counter_central_lock.py)


## Exercise: thread queue
{id: exercise-thread-queue}


Write an application that handles a queue of jobs in N=5 threads.
Each job contains a number between 0-5.
Each thread takes the next element from the queue and sleeps for the given amount
of second (as an imitatin of actual work it should be doing). When finished it check
for another job. If there are no more jobs in the queue, the thread can close itself.


![](examples/threads/queue_skeleton.py)


If that's done, change the code so that each thread will generate a random
number between 0-5 (for sleep-time) and in 33% of the cases it will add it to the central queue
as a new job.




Another extension to this exercise is to change the code to limit the number of jobs each thread
can execute in its lifetime. When the thread has finished that many jobs it will quit and the
main thread will create a new worker thread.




## Solution: thread queue
{id: solution-thread-queue}
![](examples/threads/queue.py)


## Create a counter queue
{id: class-counter-queue}
{i: Queue}

![](examples/threads/counter_queue.py)

## A Queue of tasks
{id: class-tasks}

![](examples/threads/tasks.py)


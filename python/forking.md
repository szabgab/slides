# Forking
{id: forking-processes}

## Fork
{id: fork}
{i: fork}
{i: getpid}
{i: getppid}
{i: wait}

* [fork](https://docs.python.org/3/library/os.html#os.fork)

![](examples/fork/simple_fork.py)
![](examples/fork/simple_fork.out)


## Forking
{id: forking}
{i: fork}
{i: wait}

![](examples/fork/fork.py)
![](examples/fork/fork.out)


## Fork skeleton
{id: fork-skeleton}

![](examples/fork/fork_skeleton.py)


## Fork with load
{id: fork-load}

![](examples/fork/fork_load.py)


## Fork load results
{id: fork-load-results}
{i: time}

```
$ time python fork_load.py 1
```

![](examples/fork/fork_load_1.out)

```
$ time python fork_load.py 8
```

![](examples/fork/fork_load_8.out)


## Marshalling / Serialization
{id: marshalling}


Marshalling (or serialization) is the operation when we take an arbitrary
data structure and convert it into a string in a way that we can convert
the string back to the same data structure.

Marshalling can be used to save data persistent between execution of the same
script, to transfer data between processes, or even between machines.
In some cases it can be used to communicate between two processes written in
different programming languages.

The [marshal](http://docs.python.org/library/marshal.html) module
provides such features but it is not recommended as it was built
for internal object serialization for python.

The [pickle](http://docs.python.org/library/pickle.html) module was designed for this task.

The [json](https://docs.python.org/library/json.html) module can be used too.



## Fork with random
{id: fork-with-random}


When the **random** module is loaded it automatically calls `random.seed()` to initialize the
random generator. When we create a fork this is not called again and thus all the processes
will return the same random numbers. We can fix this by calling `random.seed()` manually.


![](examples/fork/forkrand.py)

## Exercise: fork return data
{id: exercise-fork-return-data}

Create a script that will go over a list of numbers and does some computation on each number.

![](examples/fork/compute.py)

Allow the child process to return data to the parent process. Before exiting from the child process, serialize the data-structure you want to send back and save
in a file that corresponds to the parent process and the child process. (eg. created from the PID of the paraent process and the PID of the child process)
In the parent process, when one of the children exits, check if there is a file corresponding to this child process, read the file and de-serialize it.


## Solution: fork return data
{id: solution-fork-return-data}

![](examples/fork/compute_with_fork.py)

# Forking
{id: forking-processes}

## Performance Monitoring
{id: performance-monitoring}

* Linux, OSX: htop
* Windows: Performance Monitor


## Forking
{id: forking}
{i: fork}
{i: wait}
![](examples/os/fork.py)

```
$ python fork.py
In Parent (common) The child is: 31351
In Parent PID: 31350 PPID: 10025
In Child of common
In Child PID: 31351 PPID: 31350
(31351, 768)
```


## Fork skeleton
{id: fork-skeleton}
![](examples/os/fork_skeleton.py)


## Fork with load
{id: fork-load}
![](examples/os/fork_load.py)


## Fork load results
{id: fork-load-results}

```
$ time python fork_load.py 1
In Parent of 96355
In Child
(96355, 768)

real    0m26.391s
user    0m25.893s
sys 0m0.190s
```

```
$ time python fork_load.py 8
In Parent of 96372
In Parent of 96373
In Parent of 96374
In Child
In Child
In Parent of 96375
In Child
In Child
In Parent of 96376
In Child
In Parent of 96377
In Child
In Child
In Parent of 96378
In Parent of 96379
In Child
(96374, 768)
(96372, 768)
(96375, 768)
(96373, 768)
(96376, 768)
(96377, 768)
(96378, 768)
(96379, 768)

real    0m12.754s
user    0m45.196s
sys 0m0.164s
```


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

## Fork
{id: fork}
{i: fork}
{i: getpid}
{i: wait}

![](examples/advanced/fork.py)


## Fork with random
{id: fork-with-random}


When the **random** module is loaded it automatically calls `random.seed()` to initialize the
random generator. When we create a fork this is not called again and thus all the processes
will return the same random numbers. We can fix this by calling `random.seed()` manually.


![](examples/advanced/forkrand.py)


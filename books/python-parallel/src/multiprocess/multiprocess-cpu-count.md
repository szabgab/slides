# Multiprocess CPU count

* cpu_count

* [multiprocessing](https://docs.python.org/library/multiprocessing.html)


The `multiprocessing` package makes it easy to run some function many times in parallel.

Running processes in parallel can reduce the overall runtime of the process. Generally one would think that the more we run in parallel
the faster the whole process will end, but creating the parallel processes has some overhead and the number of CPUs the computer has
also puts a limitation on the paralellizm that might be worth it.


{% embed include file="src/examples/multiprocess/cpu_count.py" %}



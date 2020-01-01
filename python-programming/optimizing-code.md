# Optimizing code
{id: optimizing-code}

## Problems
{id: problems}

* Speed
* Memory usage
* I/O (disk, network, database)



## Optimization strategy
{id: opimization-strategy}

The 3 rules of optimization


* Don't do it!
* Don't do it!
* Don't do it yet!


Premature optimization is the root of all evil ~  Donald Knuth



## Locate the source of the problem
{id: locate-the-source-of-theproblem}

* I/O is expensive! Database access, file access, GUI update
* If memory is full swapping starts - speed decreases



## Optimizing tactics
{id: optimizing-tactics}

* Choose the Right Data Structure (Dictionary?, Set?, List?)
* Sorting: Decorate Sort Undecorate (DSU) aka. Schwartzian Transform
* String Concatenation: avoid extensive concatenation
* Loops: for, list comprehension: use generators and iterators
* xrange instead of range
* Caching result, memoizing


Read more: <a href="https://wiki.python.org/moin/PythonSpeed/PerformanceTips"></a>



## Profile code
{id: profile-code}

Always profile before starting to optimize!


<a href="http://docs.python.org/2/library/profile.html"></a>



## Slow example
{id: slow-example}
![](examples/advanced/slow.py)


## profile slow code
{id: profile-slow-code}
![](examples/advanced/slow_profile.py)
![](examples/advanced/slow_profile.out)


## profile (with hotshot) slow code
{id: hotshot-slow-code}
![](examples/advanced/slow_hotshot.py)
![](examples/advanced/slow_hotshot.out)


## cProfile slow code
{id: cprofile-slow-code}
![](examples/advanced/slow_cprofile.py)
![](examples/advanced/slow_cprofile.out)



## Benchmarking
{id: benchmarking}


<a href="http://docs.python.org/2/library/timeit.html"></a>


![](examples/advanced/benchmark.py)
![](examples/advanced/benchmark.out)


## Benchmarking subs
{id: benchmarking-subs}
![](examples/advanced/benchmark_subs.py)
![](examples/advanced/benchmark_subs.out)


## Levenshtein distance
{id: levenshtein}

* [editdistance](https://github.com/aflc/editdistance) Levenshtein distance implemented in C
* [python-Levenshtein](https://github.com/ztane/python-Levenshtein/) implemented in C
* [pylev](https://github.com/toastdriven/pylev)
* [pyxdameraulevenshtein](https://github.com/gfairchild/pyxDamerauLevenshtein)
* [weighted-levenshtein](https://github.com/infoscout/weighted-levenshtein)



## Generate words
{id: generate-words}
![](examples/levenshtein/generate_words.py)


## Levenshtein - pylev
{id: use-pylev}
![](examples/levenshtein/with_pylev.py)


## Levenshtein - edittidtance
{id: use-editditance}
![](examples/levenshtein/with_editdistance.py)



## Editdistance benchmark
{id: editdistance-benchmark}

* [editdistance](https://github.com/aflc/editdistance)



## Exercise: sort files
{id: exercise-sort-files}


Write a script that given a path to a directory will print the files sorted by date. Write a simple solution and one using DSU.






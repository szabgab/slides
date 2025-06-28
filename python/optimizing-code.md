# Improving Performance - Optimizing code
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
* Sorting: Decorate Sort Undecorate (DSU) aka. [Schwartzian Transform](https://en.wikipedia.org/wiki/Schwartzian_transform).
* String Concatenation: avoid extensive concatenation.
* Loops: for, list comprehension: use generators and iterators.
* Delay expanding range, map, filter, etc. iterables.
* Caching results, memoizing.

Read more [performance tips](https://wiki.python.org/moin/PythonSpeed/PerformanceTips)

## DSU: Decorate Sort Undecorate
{id: sort-decorate-sort-undecorate}

In Perl it is called Schwartzian transform

![](examples/perf/sort_dsu.py)
![](examples/perf/sort_dsu.out)


## Profile code
{id: profile-code}

Always profile before starting to optimize!

* [profile](http://docs.python.org/library/profile.html)


## Slow example
{id: slow-example}

{aside}
This code does some stuff which was deemed to be "too slow" by some client.
The actual content is not that interesting.
{/aside}

![](examples/advanced/slow.py)


## profile slow code
{id: profile-slow-code}
{i: profile}

![](examples/advanced/slow_profile.py)
![](examples/advanced/slow_profile.out)


## cProfile slow code
{id: cprofile-slow-code}
{i: cProfile}

![](examples/advanced/slow_cprofile.py)
![](examples/advanced/slow_cprofile.out)


## Benchmarking
{id: benchmarking}

* [benchmark](http://docs.python.org/library/timeit.html)


![](examples/advanced/benchmark.py)
![](examples/advanced/benchmark.out)


## Benchmarking subs
{id: benchmarking-subs}

![](examples/advanced/benchmark_subs.py)
![](examples/advanced/benchmark_subs.out)

## Counting words - which implementation is faster?
{id: counting-words-which-implementation-is-faster}
{i: collections}
{i: defaultdict}
{i: Counter}
{i: timeit}
{i: try}
{i: except}

* In this example we have 4 functions counting the number of appearances of words that are already in memmory in a list.
* We use `timeit` to benchmark them.
* `repeat` is the number of repetition of each string.
* `different` is the number of different string.

![](examples/dictionary/count_words_speed.py)
![](examples/dictionary/count_words_speed.out)

## for loop or reduce to add numbers?
{id: for-loop-or-reduce-to-add-numbers}
{i: for}
{i: functools}
{i: reduce}

![](examples/advanced/add_numbers.py)
![](examples/advanced/add_numbers.out)


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


## Levenshtein - editdistance
{id: use-editdistance}

![](examples/levenshtein/with_editdistance.py)


## Editdistance benchmark
{id: editdistance-benchmark}

* [editdistance](https://github.com/aflc/editdistance)

## A Tool to Generate text files
{id: generate-text-files}

![](examples/perf/generate_text_files.py)

## Count characters
{id: count-characters-in-two-lists}

![](examples/perf/count_characters.py)

![](examples/perf/prof.py)

## Memory leak
{id: memory-leak}

![](examples/perf/mymem.py)
![](examples/perf/mem_leak.py)

## Garbage collection
{id: garbage-collection}

* [gc](https://docs.python.org/library/gc.html)

![](examples/perf/mem_gc.py)

## Weak reference
{id: weak-reference}

* [weakref](https://docs.python.org/library/weakref.html)

![](examples/perf/weakmymem.py)
![](examples/perf/mem_weakref.py)

## Exercise: benchmark list-comprehension, map, for
{id: exercise-benchmark-list-comprehension-and-map}

* Create several functions that accept a list of numbers from 1 to 1000 and calculate their square:
* A function with a `for`-loop.
* A function that uses `map`.
* A function that uses list-comprehension.

* Feel free to have any other calucaltion and measure that.
* Send me the code and the results!

## Exercise: Benchmark Levenshtein
{id: exercise-benchmark-levenshtein}

* Take the implementation of the Levenshtein distance calculations and check which one is faster.

## Exercise: sort files
{id: exercise-sort-files}

Write a script that given a path to a directory will print the files sorted by date.
If you don't have one large folder, then use `os.walk` to get the path to the files of a whole directory tree.


* Write a simple solution.
* Profile.
* Use [DSU](https://code-maven.com/slides/python-programming/sort-decorate-sort-undecorate).

## Exercise: compare split words:
{id: exercise-compare-split-words}

We have three ways of splitting a string into words. Using `split`, using `re.split` and by going over it character-by-charcter.
Which one is the fastest?

![](examples/perf/split_to_words.py)

## Exercise: count words
{id: exercise-performance-of-word-coounting}

Given a file count how many times each word appears.
Have two implementations. One using two list and one using a dictionary.
Profile the code and benchmark the two solutions.

See `examples/lists/count_words_two_lists.py` and `examples/dictionary/count_words.py`




# Multiprocess
{id: multiprocess}

## Multiprocess CPU count
{id: multiprocess-cpu-count}
{i: cpu_count}

* [multiprocessing](https://docs.python.org/library/multiprocessing.html)

{aside}
The `multiprocessing` package makes it easy to run some function many times in parallel.

Running processes in parallel can reduce the overall runtime of the process. Generally one would think that the more we run in parallel
the faster the whole process will end, but creating the parallel processes has some overhead and the number of CPUs the computer has
also puts a limitation on the paralellizm that might be worth it.
{/aside}

![](examples/multiprocess/cpu_count.py)

## Multiprocess N files: Pool
{id: multiprocess-file}
{i: multiprocess}
{i: Pool}
{i: map}

{aside}
In this example we "analyze" files by counting how many characters they have, how many digits, and how many spaces.
{/aside}

Analyze N files in parallel.

![](examples/multiprocess/multiprocess_files.py)

```
$ python multiprocess_files.py 3 multiprocess_*.py
```

![](examples/multiprocess/multiprocess_files.out)

{aside}
We asked it to use 3 processes, so looking at the process ID you can see one of them worked twice.
The returned results can be any Python datastructure. A dictionary is usually a good idea.
{/aside}


## Multiprocess load
{id: multiprocess-load}
{i: multiprocess}
{i: Pool}
{i: map}

![](examples/multiprocess/multiprocess_load.py)


## Multiprocess: Pool
{id: multiprocess-pool}
{i: multiprocess}
{i: Pool}
{i: map}

`Pool(3)` creates 3 child-processes and let's them compute the values. `map`
returns the results in the same order as the input came in.

![](examples/multiprocess/multiprocess_pool.py)

```
python multiprocess_pool.py  11 3
python multiprocess_pool.py  100 5
```


## Multiprocess load async
{id: multiprocess-load-async}
{i: imap}
{i: map_async}

![](examples/multiprocess/multiprocess_pool_async.py)


## Multiprocess and logging
{id: multiprocess-and-loggin}
{i: multiprocess}
{i: logging}

Tested on Windows

![](examples/multiprocess/multiprocessing_and_logging.py)

## Exercise: Process N files in parallel
{id: exercise-process-n-files-in-parallel}

Create a script that given two number N and X will create N files (1.txt - N.txt). In each file put X rows of random ASCII characters: (digits, lower- and upper-case letters, space). (see [string](https://docs.python.org/library/string.html)) Each row should be 0-80 characters long. (random length for each row).
Using the script create a bunch of files.

Write a script that given a list of files will read all the files. For each file and count how many times each digit(!) appears and provide a combined report. First write the script in a single process way. Then convert it to be able to work with multiprocess. Submit the 3 scripts.

The report could look like this:

![](examples/multiprocess/count_digits.out]

## Exercise: Process N Excel files in parallel
{id: exercise-process-n-excel-files-in-parallel}

* Create N Excel files with 10 random numbers in the first row of each file. This should be **create_random_excel.py**.
* Write a process that reads the N Excel files and sums up the numbers in each one of them and then sums up the numbers of all the files. This should be **add_excel.py** that gets the list of Excel files on the command line.

## Exercise: Fetch URLs in parallel
{id: exercise-fetch-urls-in-parallel}

* [top-websites](https://www.similarweb.com/top-websites)
* Given a file with a list of URLs, collect the title of each site.

![](examples/parallel/urls.txt)

![](examples/parallel/fetch_urls.py)

## Exercise: Fetch URLs from one site.
{id: exercise-fetch-urls-from-one-site}

Download the [sitemap](https://code-maven.com/sitemap.xml) or the other [sitemap](the https://code-maven.com/slides/sitemap.xml) file
and fetch the first N URLs from there. Collecting the titles.

![](examples/parallel/fetch_site_urls.py)

## Solution: Process N files in parallel
{id: solution-process-n-files-in-parallel}

![](examples/multiprocess/count_digits.py]

## Solution: Fetch URLs in parallel
{id: solution-fetch-urls-in-parallel}

* First create function and use regular map.
* Deal with encoding.
* Replace continue by return, include None in results.
* It has some 2 sec overhead, but then 20 items reduced from 18 sec to 7 sec using pool of 5.

![](examples/parallel/fetch_urls_multiprocess.py)


# Parallel processing
{id: parallel}


## Types of problems
{id: types-of-problems}


* CPU intensive application - use more of the cores to reduce the wallclock time.
* IO intensive applications - don't waste the CPU and wallclock time while waiting for the IO process.
* Interactive applications - make sure they are responsive during long operations.

## Types of solutions
{id: types-of-solutions}

* Number of processes (forking on Unix or spawning)
* Number of threads (Single threaded vs Multi-threaded)
* Asynchronous, non-blocking or synchronous vs blocking (aka "normal") Cooperative Multitasking

## Tasks
{id: parallel-tasks}

* count.pl - count numbers CPU intensive
* process_csv.pl - mostly CPU intensive but also reading files
* httpget.pl - Download web pages and extract title - mostly IO intensive

## Measurements on 32 core
{id: measurement-on-32-core}

On the 32 core CPU-Optimized server on [Digital Ocean](https://www.digitalocean.com/?refcode=0d4cc75b3a74)

```
perl count.pl 0 30 10000000
    Elapsed time 7.92
perl count.pl 30 30 10000000
    Elapsed time 0.45

perl process_csv.pl 0 30
    Elapsed time 38.01
perl process_csv.pl 30 30
    Elapsed time 3.02

perl httpget.pl wikipedia.txt 0 80
    Elapsed time 12.93
perl httpget.pl wikipedia.txt 20 80
    Elapsed time 4.06
perl httpget.pl wikipedia.txt 80 80
    Elapsed time 1.11
```


## Measurements on 4 core
{id: measurement-on-4-core}


```
perl count.pl 0 12 40000000
    Elapsed time 13.57
perl count.pl -1 12 40000000
    Elapsed time 5.78
perl count.pl 2 12 40000000
    Elapsed time 6.85
perl count.pl 3 12 40000000
    Elapsed time 6.42
perl count.pl 12 12 40000000
    Elapsed time 5.79
```

```
perl process_csv.pl 0 6
    Elapsed time 14.91
perl process_csv.pl 2 6
    Elapsed time 10.25
perl process_csv.pl 3 6
    Elapsed time 8.30
perl process_csv.pl 6 6
    Elapsed time 8.71
```

```
perl httpget.pl wikipedia.txt 0 20
    Elapsed time 18.72
perl httpget.pl wikipedia.txt 10 20
    Elapsed time 4.17
```

## The Hardware
{id: the-hardware}

```
lscpu
cat /proc/cpuinfo
htop
```

## Installations
{id: parallel-installations}

```
cpanm Parallel::ForkManager
cpanm LWP::Simple
cpanm HTML::TreeBuilder::XPath

cpanm Win32::Getppid
```

Ubuntu system perl:

```
libwww-perl
libparallel-forkmanager-perl
libhtml-treebuilder-xpath-perl
```

## Fork
{id: fork}
{i: fork}

![](examples/forks/fork_skeleton_functions.pl)

## Fork with functions details
{id: fork-details}
{i: fork}

![](examples/forks/fork_skeleton_functions_details.pl)

## Fork random and seed
{id: fork-random-and-seed}
{i: rand}
{i: srand}

![](examples/forks/fork_random.pl)

## Fork without functions
{id: fork-without-functions}
{i: fork}

![](examples/forks/fork_skeleton.pl)

## Fork details
{id: fork-one}
{i: fork}

* [Win32::Getppid](https://metacpan.org/pod/Win32::Getppid)

![](examples/forks/fork.pl)


## Fork many
{id: fork-many}

![](examples/forks/fork_many.pl)

## Parent process ID
{id: parent-process-id}

![](examples/forks/parent.pl)

## pstree
{id: pstree}

```
pstree -p -a
```

## htop
{id: htop}


```
htop
```

* H
* F4  to filter

## Active non-blocking waiting with waitpid
{id: active-waiting}
{i: waitpid}
{i: POSIX}
{i: WNOHANG}

{aside}
Up till now we were usig the `wait` function to wait for a child process to terminate. It is a blocking call that will wait till any of the child processes terminates.

There are other options as well. Using the `waitpid` function you could wait for a specific child to terminate using its PID or you can have a non-blocking way to check
if there is any child-processes that has already terminated. The non-blocking wait mode allows the parent process to do other things while waiting for the child processes
to do their job.
{/aside}

* [waipid](https://metacpan.org/pod/distribution/perl/pod/perlfunc.pod#wait)

![](examples/forks/active_waiting.pl)

```
perl active_waiting.pl 0 0
perl active_waiting.pl 1 0
perl active_waiting.pl 1 1
```

## Non-blocking waiting with waitpid - multiple forks
{id: active-waiting-multiple-forks}

{aside}
In this example we create multiple child processes and wait for them with a non-blocking waitpid.
Each process will sleep for a random number of seconds imitating the randomness of the time it takes each one of them
to finish doing their job. They also generate a random exit code to imitate that some of them might have failed.
{/aside}

![](examples/forks/active_waiting_loop.pl)

```
perl active_waiting_loop.pl 1
perl active_waiting_loop.pl 5
```
## Non-blocking waiting, rerun on failure
{id: active-waiting-rerun-on-failure}

{aside}
In this example we have a list of tasks we need to do. The user can supply the number of child processes that will deal with the tasks.
Each child process generates a random number to wait to imitatet the work time and a random number as the exit code.

The parent monitors the child processes. If one of them exits with a non-zero error code the parent re-runs that job with another
child process until all the tasks are done.
{/aside}

![](examples/forks/active_waiting_tasks.pl)
![](examples/forks/active_waiting_tasks.out)


## Functions to be speed up
{id: functions-to-be-speed-up}

![](examples/forks/Task.pm)

## Counter process
{id: counter-process}

![](examples/forks/count.pl)

```
perl count.pl 0 12 40000000
```


## Forked counter process
{id: forked-counter-process}

![](examples/forks/ForkedCounter.pm)

## Prepare CSV files
{id: prepare-csv-files}

{aside}
Generate CSV data files to be used by the CSV processing task. Each file has rows with the 3rd column being increasing numbers.
The number in the last row of each file contains the seriel number of the file. That will make the sum of the numbers different and we'll be able to verify if the results come from the different files.
{/aside}

![](examples/forks/prepare_files.pl)

```
perl prepare_files.pl 12 2000000
```

## Process CSV files
{id: process-csv-files}

{aside}
We expect two parameters on the command line. The number of parallel processes to run and how many files to process.
For parallel 0 means not to use the forking mechanizm at all.
We use the number of files instead of accepting the list of files on the command line, becasue it is easier to select a subset of the files this way.
{/aside}

![](examples/forks/process_csv.pl)

```
$ perl process_csv.pl 0 1
Elapsed time 1.51

$ perl process_csv.pl 0 4
Elapsed time 5.92

$ perl process_csv.pl 2 4
Elapsed time 4.02

$ perl process_csv.pl 4 4
Elapsed time 4.01

$ perl process_csv.pl 0 10
Elapsed time 15.18

$ perl process_csv.pl 4 10
Elapsed time 9.05
```


## Use Parallel::ForkManager
{id: use-parallel-forkmanager}
{i: fork}

* [Parallel::ForkManager](https://metacpan.org/pod/Parallel::ForkManager)

![](examples/forks/forkmanager.pl)

## Return values using Parallel::ForkManager
{id: return-values-using-paralle-forkmanager}
{i: fork}

![](examples/forks/forkmanager_return_values.pl)


## Forked process CSV files
{id: forked-process-csv-file}

![](examples/forks/ForkedProcessCSV.pm)


## HTTP GET
{id: http-get-title}

![](examples/forks/httpget.pl)

## Forked HTTP requests
{id: forked-process-http-requests}

![](examples/forks/ForkedHTTP.pm)

## Exercise: Process Excel files
{id: exercise-forked-process-excel-files}

* Create N excel files, similar to the CSV files we had in the example and then process them. Both in a serial manner and in parallel.

## Exercise: Web crawler
{id: exercise-forked-web-crawler}

* Build a crawler that, given a single URL and a number N will visit N pages linked from that page. (Maybe need to also get to the links of the links etc.)
* You can use [HTML::TreeBuilder::XPath](https://metacpan.org/pod/HTML::TreeBuilder::XPath) to extract the links from the html document.
* It is probably better to allow only the main process to fork.

## MCE - Many-Core Engine
{id: many-core-engine}
{i: MCE}
{i: fork}

* [MCE](https://metacpan.org/pod/MCE)

* On Debian/Ubuntu it is called `libmce-perl`

![](examples/forks/use_mce.pl)

```
$ perl use_mce.pl 5
```

![](examples/forks/use_mce.out)

## MCE - map running in parallel
{id: mce-map}
{i: MCE}
{i: fork}
{i: map}

* [MCE::Map](https://metacpan.org/pod/MCE::Map)

{aside}
The MCE package provides a map-like function that automatically runs the different tasks in separate processes then
collects the results in the correct order.

By default it creates 4 child processes, but you can control that and a few other things by calling the init method.
{/aside}

![](examples/forks/use_mce_map.pl)
![](examples/forks/use_mce_map.out)


## MCE - map with init
{id: mce-map-with-init}

![](examples/forks/use_mce_map_init.pl)
![](examples/forks/use_mce_map_init.out)

## other modules
{id: other-modules-for-forking}

* [Parallel::Forker](https://metacpan.org/pod/Parallel::Forker) another module that could be used.
* [Proc::Queue](https://metacpan.org/pod/Proc::Queue) has not been updated since 2008




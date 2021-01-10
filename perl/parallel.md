# Parallel processing
{id: parallel}


## Tasks
{id: parallel-tasks}

```
perl count.pl 0 12 40000000
    Elapsed time 13.5732021331787
perl count.pl -1 12 40000000
    Elapsed time 5.78469800949097
perl count.pl 2 12 40000000
    Elapsed time 6.85440993309021
perl count.pl 3 12 40000000
    Elapsed time 6.4282820224762
perl count.pl 12 12 40000000
    Elapsed time 5.79987692832947
```

```
perl process_csv.pl 0 6
    Elapsed time 14.9164409637451
perl process_csv.pl 2 6
    Elapsed time 10.2596349716187
perl process_csv.pl 3 6
    Elapsed time 8.30312204360962
perl process_csv.pl 6 6
    Elapsed time 8.71829104423523
```

```
perl httpget.pl wikipedia.txt 0 20
    Elapsed time 18.723984003067
perl httpget.pl wikipedia.txt 10 20
    Elapsed time 4.17807006835938
```

## Installations
{id: parallel-installations}

```
cpanm Parallel::ForkManager
cpanm LWP::Simple
cpanm HTML::TreeBuilder::XPath

cpanm Win32::Getppid
```


## Fork
{id: fork}
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

## Use Parallel::Forkmanager
{id: use-parallel-forkmanager}

* [Parallel::ForkManager](https://metacpan.org/pod/Parallel::ForkManager)

![](examples/forks/forkmanager.pl)

## Return values using Parallel::ForkManager
{id: return-values-using-paralle-forkmanager}

![](examples/forks/forkmanager_return_values.pl)

## HTTP GET
{id: http-get-title}

![](examples/forks/httpget.pl)




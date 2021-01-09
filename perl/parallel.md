# Parallel processing
{id: parallel-processing}

## Tasks
{id: parallel-tasks}

```
perl count.pl 0 12 40000000
perl count.pl 2 12 40000000
```


## Functions to be speed up
{id: functions-to-be-speed-up}

![](examples/forks/Task.pm)

## Counter process
{id: counter-process}

![](examples/forks/count.pl)

```
perl count.pl 0 12 40000000
```

## Fork
{id: fork}

![](examples/forks/fork.pl)

## Fork many
{id: fork-many}

![](examples/forks/fork_many.pl)

## Parent process ID
{id: parent-process-id}

![](examples/forks/parent.pl)

## Forked counter process
{id: forked-counter-process}

![](examples/forks/ForkedCounter.pm)

## Prepare CSV files
{id: prepare-csv-files}

![](examples/forks/prepare_files.pl)

## Process CSV files
{id: process-csv-files}

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




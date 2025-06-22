# subprocess
{id: subprocess}


## External CLI tool to demo subprocess
{id: external-cli-tool-to-demo-subprocess}
{i: subprocess}
{i: call}
{i: execute}

{aside}
The process.py is a simple script we are going to use to demonstrate how an external program can be executed from within Python.
It is a Python program, but you could do the exact same thing with any command-line application written in any language.
We use this Python script as an example because we know you already have Python on your computer.
{/aside}

The external command:

![](examples/process/process.py)

Try it on the command line: `python process.py 3 7`

## Run with os.system
{id: run-with-os-system}

![](examples/process/os_system.py)
![](examples/process/os_system.out)

## Run external process let STDOUT and STDERR through
{id: run-external-process-and-let-stdout-and-stderr-through}

![](examples/process/run_command.py)
![](examples/process/run_command.out)

## Run external process and capture STDOUT and STDERR separately
{id: run-external-process-and-capture-stdout-and-stderr-separately}

![](examples/process/run_command_collect_output.py)
![](examples/process/run_command_collect_output.out)

## Run external process and capture STDOUT and STDERR merged together
{id: run-external-process-and-capture-stdout-and-stderr-merged-together}

![](examples/process/run_command_combine_stderr_and_stdout.py)
![](examples/process/run_command_combine_stderr_and_stdout.out)

In this case stderr will always be `None`.


## subprocess in the background
{id: subprocess-background}

{aside}
In the previous examples we ran the external command and then waited till it finishes before doing anything else.

In some cases you might prefer to do something else while you are waiting - effectively running the process in the background.
This also makes it easy to enforce a time-limit on the process. If it does not finish within a given amount of time (timeout)
we raise an exception.

In this example we still collect the standard output and the standard error at the end of the process.
{/aside}

![](examples/process/run_process_polling.py)
![](examples/process/run_process_polling.out)


## subprocess collect output while external program is running
{id: subprocess-collect-output-while-external-program-is-running}

{aside}
For this to work properly the external program might need to set the output to unbuffered.
In Python by default prining to STDERR is unbuffered, but we had to pass `flush=True` to the print
function to make it unbuffered for STDOUT as well.
{/aside}

![](examples/process/run_command_collect_while_running.py)
![](examples/process/run_command_collect_while_running.out)

## Exercise: Processes
{id: exercise-processes}

Given the following "external application":

![](examples/process/myrandom.py)

It could be run with a command like this to create the a.txt file:

```
python examples/process/myrandom.py a.txt 3 1
```

Or like this, to raise an exception before creating the b.txt file:

```
python examples/process/myrandom.py b.txt 3 1 "bad thing"
```

Or it could be used like this:

![](examples/process/use_myrandom.py)

Write a program that will do "some work" that can be run in parallel
and collect the data. Make the code work in a single process by default
and allow the user to pass a number that will be the number of child processes
to be used. When the child process exits it should save the results in
a file and the parent process should read them in.


The "some work" can be accessing 10-20 machines using "ssh machine uptime"
and creating a report from the results.


It can be fetching 10-20 URLs and reporting the size of each page.


It can be any other network intensive task.


Measure the time in both cases

## Subprocess TBD
{id: subprocess-other}

Some partially ready examples

![](examples/process/slow_starting_server.py)
![](examples/process/wait_do_and_stop.py)
![](examples/process/run_multiple_commands.py)

# Exercise: Processes


Given the following "external application":

{% embed include file="src/examples/process/myrandom.py" %}

It could be run with a command like this to create the a.txt file:

```
python examples/process/myrandom.py a.txt 3 1
```

Or like this, to raise an exception before creating the b.txt file:

```
python examples/process/myrandom.py b.txt 3 1 "bad thing"
```

Or it could be used like this:

{% embed include file="src/examples/process/use_myrandom.py" %}

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



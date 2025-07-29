# Context managers (with statement)
{id: context-manager}

## Why use context managers?
{id: context-manager-why}

In certain operations you might want to ensure that when the operation is done there will be an opportunity to clean up
after it. Even if decided to end the operation early or if there is an exception in the middle of the operation.

In the following pseudo-code example you can see that `cleanup` must be called both at the end and before the `early-end`, but
that still leaves the bad-code that raises exception avoiding the cleanup. That forces us to wrap the whole section in a try-block.

```
def sample():
    start
    do
    do
    do
    do
    cleanup
```

What is we have some conditions for early termination?

```
def sample():
    start
    do
    do
    if we are done early:
        cleanup
        return # early-end
    do
    do
    cleanup
```

What if we might have an exception in the code?

```
def sample():
    start
    try:
        do
        do
        if we are done early:
            cleanup
            return early-end
        do
        bad-code    (raises exception)
        do
        cleanup
    finally:
        cleanup
```

It is a lot of unnecessary code duplication and we can easily forget to add it in every location where we early-end our code.

## Using Context Manager
{id: context-manager-how}

```
with cm_for_sample():
    start
    do
    do
    if we are done early:
        return early-end
    do
    bad-code    (raises exception)
    do
```

* `cleanup` happens automatically, it is defined inside the `cm_for_sample`

## Context Manager examples
{id: context-manager-examples}

A few examples where context managers can be useful:

* Opening a file - close it once we are done with it so we don't leak file descriptors.
* Changing directory - change back when we are done.
* Create temporary directory - remove when we are done.
* Open connection to database - close connection.
* Open SSH connection - close connection.

* More information about [context managers](https://jeffknupp.com/blog/2016/03/07/python-with-context-managers/)

## cd in a function
{id: cd-in-function}
{i: getcwd}
{i: chdir}

{aside}
In this example we have a function in which we change to a directory and then when we are done we change back to the original directory.
For this to work first we save the current working directory using the `os.getcwd` call. Unfortunatelly in the middle of the code there
is a conditional call to `return`. If that condition is `True` we won't change back to the original directory. We could fix this by
calling `os.chdir(start_dir)` just before calling `return`. However this would still not solve the problem if there is an exception
in the function.
{/aside}

![](examples/context/no_context_cd.py)

![](examples/context/no_context_cd_tmp.out)

![](examples/context/no_context_cd_opt.out)

* In the second example `return` was called and thus we stayed on the /opt directory.:w



## open in function
{id: open-in-function}

{aside}
This is not the recommended way to open a file, but this is how it was done before the introduction of the `with` context manager.
Here we have the same issue. We have a conditional call to `return` where we forgot to close the file.
{/aside}

![](examples/context/no_context_fh.py)


## open in for loop
{id: open-in-for-loop}
{i: stat}
{i: os.stat}

{aside}
Calling `write` does not immediately write to disk. The Operating System provides buffering as an optimization
to avoid frequent access to the disk. In this case it means the file has not been saved before we already check its size.
{/aside}

![](examples/context/save.py)


## open in function using with
{id: open-in-function-with}

{aside}
If we open the file in the recommended way using the `with` statement then we can be sure that the `close` method
of the `fh` object will be called when we leave the context of the `with` statement.
{/aside}

![](examples/context/with_fh.py)


## Plain context manager
{id: plain-context-manager}

![](examples/context/my_plain_context.py)
![](examples/context/my_plain_context.out)


## Param context manager
{id: param-context-manager}

![](examples/context/my_param_context.py)
![](examples/context/my_param_context.out)


## Context manager that returns a value
{id: return-context-manager}

![](examples/context/my_tempdir.py)

![](examples/context/use_my_tempdir.py)
![](examples/context/use_my_tempdir.out)

## Use my tempdir - return
{id: use-my-tempdir-return}

![](examples/context/use_my_tempdir_return.py)
![](examples/context/use_my_tempdir_return.out)

## Use my tempdir - exception
{id: use-my-tempdir-exception}

![](examples/context/use_my_tempdir_exception.py)
![](examples/context/use_my_tempdir_exception.out)

## cwd context manager
{id: cwd-context-manager}

![](examples/context/mycwd.py)
![](examples/context/context_cd.py)

```
$ python context_cd.py /tmp
/home/gabor/work/slides/python/examples/context
/home/gabor/work/slides/python/examples/context

$ python context_cd.py /opt
/home/gabor/work/slides/python/examples/context
/home/gabor/work/slides/python/examples/context
```


## tempdir context manager
{id: tempdir-context-manager}
{i: contextlib}
{i: contextmanager}
{i: tempfile}
{i: mkdtemp}

![](examples/context/mytmpdir.py)
![](examples/context/use_mytmpdir.py)
![](examples/context/use_mytmpdir.out)

## Context manager with class
{id: with-context-manager}
{i: __enter__}
{i: __exit__}


![](examples/context/context-manager.py)

## Context managers with class
{id: with-context-managers}
{i: __enter__}
{i: __exit__}


Even if there was en exception in the middle of the process,
the __exit__ methods of each object will be called.

![](examples/context/context-managers.py)
![](examples/context/context-managers.out)


## Context manager: with for file
{id: with}
{i: with}
![](examples/context/with_file.py)


## With - context managers
{id: with-example}
{i: with}
![](examples/classes/with_example.py)



## Exercise: Context manager
{id: exercise-context}


Create a few CSV file likes these:


![](examples/context/a.csv)
![](examples/context/b.csv)
![](examples/context/c.csv)


Merge them horizontally to get this:


![](examples/context/out.csv)

* Do it without your own context manager
* Create a context manager called myopen that accepts N filenames. It opens the first one to write and the other N-1 to read


```
with myopen(outfile, infile1, infile2, infile3) as out, ins:
    ...
```

## Exercise: Tempdir on Windows
{id: exercise-tempdir-on-windows}

Make the tempdir context manager example work on windows as well. Probably need to cd out of the directory.

## Solution: Context manager
{id: solution-context}
![](examples/context/merge.py)




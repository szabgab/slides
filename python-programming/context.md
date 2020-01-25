# Context managers (with statement)
{id: context-manager}

## Why use context managers?
{id: context-manager-why}

In certain operations you might want to ensure that when the operation is done there will be an opportunity to clean up
after it. Even if decided to end the operation early or if there is an exception in the middle of the operation.

In the following pseudo-code example you can see that `cleanup` must be called both at the end and before the `early-end`, but
that still leaves the bad-code that raises exception avoiding the cleanup. That forces us to wrap the whole section in a try-block.

```
start
do
do
do
do
cleanup
```

What is we have some conditions for early termination?

```
start
do
do
if we are done early:
   cleanup
   early-end
do
do
cleanup
```

What if we might have an exception in the code?

```
start
try:
   do
   do
   if we are done early:
      cleanup
      early-end
   do
   bad-code    (raises exception)
   do
   cleanup
finally:
   cleanup
```

It is a lot of unnecessary code duplication and we can easily forget to add it in every location where we early-end our code.

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
calling `os.chdir(start_dir)` just before callind `return`. However this would still not solve the problem if there is an exception
in the function.
{/aside}

![](examples/advanced/no_context_cd.py)

```
$ python no_context_cd.py /tmp/
/home/gabor/work/slides/python/examples/advanced
/home/gabor/work/slides/python/examples/advanced

$ python no_context_cd.py /opt/
/home/gabor/work/slides/python/examples/advanced
/opt
```

## open in function
{id: open-in-function}

{aside}
This is not the recommended way to open a file, but this is how it was done before the introduction of the `with` context manager.
Here we have the same issue. We have a conditional call to `return` where we forgot to close the file.
{/aside}


![](examples/advanced/no_context_fh.py)

## open in for loop
{id: open-in-for-loop}

![](examples/context/save.py)

## open in function using with
{id: open-in-function-with}

{aside}
If we open the file in the recommended way using the `with` statement then we can be sure that the `close` method
of the `fh` object will be called when we leave the context of the `with` statement.
{/aside}

![](examples/advanced/with_fh.py)


## Plain context manager
{id: plain-context-manager}
![](examples/advanced/my_plain_context.py)
![](examples/advanced/my_plain_context.out)


## Param context manager
{id: param-context-manager}
![](examples/advanced/my_param_context.py)
![](examples/advanced/my_param_context.out)


## Context manager that returns a value
{id: return-context-manager}
![](examples/advanced/my_tempdir.py)

![](examples/advanced/use_my_tempdir.py)
![](examples/advanced/use_my_tempdir.out)

## Use my tempdir - return
{id: use-my-tempdir-return}

![](examples/advanced/use_my_tempdir_return.py)
![](examples/advanced/use_my_tempdir_return.out)

## Use my tempdir - exception
{id: use-my-tempdir-exception}

![](examples/advanced/use_my_tempdir_exception.py)
![](examples/advanced/use_my_tempdir_exception.out)

## cwd context manager
{id: cwd-context-manager}
![](examples/advanced/mycwd.py)
![](examples/advanced/context_cd.py)

```
$ python context_cd.py /tmp
/home/gabor/work/slides/python/examples/advanced
/home/gabor/work/slides/python/examples/advanced

$ python context_cd.py /opt
/home/gabor/work/slides/python/examples/advanced
/home/gabor/work/slides/python/examples/advanced
```


## tempdir context manager
{id: tempdir-context-manager}
![](examples/advanced/mytmpdir.py)
![](examples/advanced/use_mytmpdir.py)
![](examples/advanced/use_mytmpdir.out)


## Context managers: with
{id: with-context-managers}
{i: __enter__}
{i: __exit__}


Even if there was en exception in the middle of the process,
the __exit__ methods of each object will be called.


![](examples/advanced/context-managers.py)
![](examples/advanced/context-managers.out)


## Context manager: with for file
{id: with}
{i: with}
![](examples/advanced/with_file.py)


## With - context managers
{id: with-example}
{i: with}
![](examples/classes/with_example.py)



## Exercise: Context manager
{id: exercise-context}


Create a few CSV file likes these:


![](examples/advanced/a.csv)
![](examples/advanced/b.csv)
![](examples/advanced/c.csv)


Merge them horizontally to get this:


![](examples/advanced/out.csv)

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
![](examples/advanced/merge.py)




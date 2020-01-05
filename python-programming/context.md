# Context managers (with statement)
{id: context-manager}

## Why context manager
{id: context-manager-why}

* [with context manager](https://jeffknupp.com/blog/2016/03/07/python-with-context-managers/)



## cd in function
{id: cd-in-function}
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
![](examples/advanced/no_context_fh.py)

## open in function using with
{id: open-in-function-with}

![](examples/advanced/with_fh.py)


## Plain context manager
{id: plain-context-manager}
![](examples/advanced/my_plain_context.py)
![](examples/advanced/my_plain_context.out)


## Param context manager
{id: param-context-manager}
![](examples/advanced/my_param_context.py)
![](examples/advanced/my_param_context.out)


## Return context manager
{id: return-context-manager}
![](examples/advanced/my_tempdir.py)

![](examples/advanced/use_my_tempdir.py)
![](examples/advanced/use_my_tempdir.out)

![](examples/advanced/use_my_tempdir_return.py)
![](examples/advanced/use_my_tempdir_return.out)

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


## Solution: Context manager
{id: solution-context}
![](examples/advanced/merge.py)




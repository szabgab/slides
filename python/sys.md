# sys
{id: sys}

## sys module
{id: sys-module}
{i: sys}
{i: argv}
{i: executable}
{i: path}
{i: version_info}

![](examples/sys/mysys.py)
![](examples/sys/mysys.out)

Later we'll see also the `platform` module for more details of the Operating System.


## Writing to standard error (stderr)
{id: writing-to-standard-error}
{i: stdout}
{i: stderr}
{i: write}

![](examples/sys/stderr.py)


Redirection (Works on Linux/Mac/Windows):

```
python stderr.py > out.txt  2> err.txt
python stderr.py > out.txt 2>&1

python stderr.py 2> /dev/null            # On Linux and OSX
python stderr.py 2> nul                  # On Windows
```



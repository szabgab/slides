# Python standard modules (standard packages)
{id: standard-modules}

## Some Standard packages
{id: some-standard-packages}

* [sys](http://docs.python.org/library/sys.html) - System specific
* [os](http://docs.python.org/library/os.html) - Operating System
* [stat](http://docs.python.org/library/stat.html) - Inode table
* [shutil](http://docs.python.org/library/shutil.html) - File Operations
* [glob](http://docs.python.org/library/glob.html) - Unix style pathname expansion
* [subprocess](http://docs.python.org/library/subprocess.html) - Processes


* [argparse](http://docs.python.org/library/argparse.html) - Command Line Arguments
* [re](http://docs.python.org/library/re.html) - Regexes
* [math](http://docs.python.org/library/math.html) - Mathematics
* [time](http://docs.python.org/library/time.html) - Timestamp and friends
* [datetime](http://docs.python.org/library/datetime.html) - Time management
* [random](http://docs.python.org/library/random.html) - Random numbers


## sys
{id: sys}
{i: sys}
{i: argv}
{i: executable}
{i: path}
{i: version_info}

![](examples/sys/mysys.py)

```
['examples/sys/mysys.py']

/usr/bin/python

['/Users/gabor/work/training/python/examples/sys',
 '/Users/gabor/python/lib/python2.7/site-packages/crypto-1.1.0-py2.7.egg',
 ...,
 '/Users/gabor/python',
 '/Users/gabor/python/lib/python2.7/site-packages',
 ...]
```


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

## Current directory (getcwd, pwd, chdir)
{id: pwd-current-working-directory}
{i: getcwd}
{i: pwd}
{i: chdir}
![](examples/os/cwd.py)


## OS dir (mkdir, makedirs, remove, rmdir)
{id: os-dir}
{i: mkdir}
{i: makedirs}
{i: remove}
{i: unlink}
{i: rmdir}
{i: removedirs}
{i: rmtree}

![](examples/os/mkdir.py)


## python which OS are we running on (os, platform)
{id: which-os-are-we-running-on}
{i: platform}
{i: os}

![](examples/os/which_os.py)


## Get process ID
{id: os-pid-process-id}
{i: getpid}
{i: getppid}

* Works on all 3 Operating systems

![](examples/os/getpid.py)

```
93518
92859
```

This is on Linux/OSX

```
echo $$
```


## OS path
{id: os-path}
{i: path}
{i: abspath}
{i: exists}
{i: basename}
{i: dirname}

![](examples/os/path.py)

## Traverse directory tree - list directories recursively
{id: travers-directory-tree}
{i: walk}
{i: os.walk}

![](examples/os/traverse_tree.py)


## os.path.join
{id: os-path-join}
{i: os.path.join}
{i: join}

![](examples/os/path_join.py)


## Directory listing
{id: directory-listing}
{i: dir}
{i: listdir}
{i: path}
{i: os.listdir}

![](examples/os/dir.py)

## expanduser - handle tilde ~ the home directory of the user
{id: expanduser}
{i: expanduser}
{i: ~}
{i: os.path.expanduser}

![](examples/os/expanduser.py)

## Listing specific files using glob
{id: listing-files-using-glob}
{i: glob}
{i: glob.glob}

![](examples/os/ls.py)

## External command with system
{id: external-command-with-system}
{i: os.system}
{i: system}

![](examples/os/os_system.py)

If you wanted to list the content of a directory in an os independent way you'd use `os.listdir('.')`
or you could use the `glob.glob("*.py")` function to have a subset of files.


## subprocess
{id: subprocess}
{i: subprocess}
{i: call}
{i: execute}

Run external command and capture the output

![](examples/process/slow.py)
![](examples/process/run_command.py)

In this example p is an instance of the subprocess.PIPE class. The command is executed when the object is created.


## subprocess in the background
{id: subprocess-background}

![](examples/process/run_slow.py)


## Accessing the system environment variables from Python
{id: environment-variables}
{i: os.environ}

![](examples/os/environment.py)

{aside}

os.environ is a dictionary where the keys are the environment variables and the values are, well, the values.
{/aside}


## Set env and run command
{id: set-env-and-run-command}

![](examples/os/set_env.py)

{aside}

We can change the environment variables and that change will be visible in subprocesses,
but once we exit from ou Python program, the change will not persist.
{/aside}

## shutil
{id: shutil}
{i: shutil}
{i: cp}
{i: copy}
{i: copytree}
{i: move}
{i: rmtree}

```
import shutil

shutil.copy(source, dest)
shutil.copytree(source, dest)
shutil.move(source, dest)
shutil.rmtree(path)
```

## time
{id: time}
{i: time}
{i: timezone}
{i: daylight}
{i: gmtime}
{i: strftime}

![](examples/other/mytime.py)

## sleep in Python
{id: sleep-in-python}
{i: sleep}

![](examples/os/sleep.py)

```
hello 1475217162.472256
world 1475217165.973437
Elapsed time:3.501181125640869
```

## timer
{id: timer}

More time-related examples.

![](examples/other/timer.py)


## Current date and time datetime now
{id: datetime-now}
{i: datetime}
{i: strftime}

![](examples/sys/datetime_now.py)


## Converting string to datetime
{id: converting-string-to-datetime}
{i: strptime}

![](examples/sys/converting_string_to_datetime.py)


## datetime arithmeticis
{id: datetime-arithmetics}
{i: timedelta}

![](examples/sys/datetime_arithmetics.py)


## Rounding datetime object to nearest second
{id: rounding-datetime}

![](examples/sys/datetime_rounding.py)





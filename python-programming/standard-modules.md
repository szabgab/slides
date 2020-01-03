# Python standard modules
{id: python-standard-modules}

## Some Standard modules
{id: some-standard-modules}

* [sys](http://docs.python.org/library/sys.html) - System specific
* [os](http://docs.python.org/library/os.html) - Operating System
* [stat](http://docs.python.org/library/stat.html) - inode table
* [shutil](http://docs.python.org/library/shutil.html) - File Operations
* [glob](http://docs.python.org/library/glob.html) - Unix style pathname expansion
* [subprocess](http://docs.python.org/library/subprocess.html) - Processes


* [argparse](http://docs.python.org/library/argparse.html) - Command Line Arguments
* [re](http://docs.python.org/library/re.html) - Regexes
* [math](http://docs.python.org/library/math.html) - Mathematics
* [time](http://docs.python.org/library/time.html) - timestamp and friends
* [datetime](http://docs.python.org/library/datetime.html) - time management
* [random](http://docs.python.org/library/random.html) - Random numbers



## sys
{id: sys}
{i: sys}
{i: argv}
{i: executable}
{i: path}
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


Redirection:

```
some_program > out.txt  2> err.txt
some_program 2> /dev/null
python stderr.py > out.txt 2>&1
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

```
os.mkdir(path_to_new_dir)
os.makedirs(path_to_new_dir)

os.remove()      remove a file
os.unlink()      (the same)

os.rmdir()        single empty directory
os.removedirs()   empty subdirectories as well
shutil.rmtree()   rm -rf
```



## python which OS are we running on (os, platform)
{id: which-os-are-we-running-on}
{i: platform}
{i: os}
![](examples/os/which_os.py)


## Get process ID
{id: os-pid-process-id}
{i: getpid}
{i: getppid}
![](examples/os/getpid.py)

```
93518
92859
```

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

```
import os

os.path.basename(path_to_thing)
os.path.dirname(path_to_thing)
os.path.abspath(path_to_file)

os.path.exists(path_to_file)
os.path.isdir(path_to_thing)

os.path.expanduser('~')
```


## os.path.join
{id: os-path-join}
![](examples/os/path_join.py)


## Directory listing
{id: directory-listing}
{i: dir}
{i: listdir}
{i: path}
![](examples/os/dir.py)


## expanduser - handle tilde ~
{id: expanduser}
{i: expanduser}
{i: ~}
![](examples/os/expanduser.py)


## External command with system
{id: external-command-with-system}
![](examples/os/os_system.py)


If you wanted to list the content of a directory in an os independent way you'd use <command>os.listdir('.')</command>
or you could use the <command>glob.glob("*.py")</command> function to have a subset of files.




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


## Signals and Python
{id: signals}
{i: kill}

* [man 7 signal](http://man7.org/linux/man-pages/man7/signal.7.html) (on Linux)
* Unix: kill PID, kill -9 PID, Ctrl-C, Ctrl-Z
* os.kill
* [signal](https://docs.python.org/3/library/signal.html)



## Sending Signal
{id: sending-signal}
{i: kill}
![](examples/signals/send_signal.py)

```
before
User defined signal 1: 30
```


## Catching Signal
{id: catching-signal}
![](examples/signals/catch_signal.py)

```
before
('Signal handler called with signal', 30)
after
```


## Catching Ctrl-C on Unix
{id: catching-ctrl-c-on-unix}
![](examples/signals/ctrl_c.py)

```
$  python ctrl_c.py
Username:^CTraceback (most recent call last):
  File "ctrl_c.py", line 3, in &lt;module&gt;
    username = input('Username:')
KeyboardInterrupt
```
![](examples/signals/catch_ctrl_c.py)

* Cannot stop using Ctrl-C !
* Ctrl-Z and then kill %1
* kill PID



## Catching Ctrl-C on Unix confirm
{id: catching-ctrl-c-on-unix-confirm}
![](examples/signals/catch_ctrl_c_confirm.py)


## Alarm signal and timeouts
{id: alarm-signal}
![](examples/signals/alarm.py)


## Exercise: Catching Ctrl-C on Unix 2nd time
{id: exercise-catching-ctrl-c-on-unix-count}

* When Ctrl-C is pressed display: "In order to really kill the application press Ctrl-C again" and keep running. If the user presses Ctrl-C again, then let id die.
* Improve the previous that if 5 sec within the first Ctrl-C there is no 2nd Ctrl-C then any further Ctrl-C will trigger the above message again.



## Exercise: Signals
{id: exercise-signals}

* What signal is sent when you run **kill PID**?
* Write a script that will disable the **kill PID** for your process. How can you kill it then?
* What signal is sent when we press Ctrl-Z ?



## Ctrl-z
{id: ctrl-z}
![](examples/signals/kill_15.py)

```
kill PID
```
![](examples/signals/catch_kill_15.py)






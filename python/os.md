# os
{id: os}

## python which OS are we running on (os, platform)
{id: which-os-are-we-running-on}
{i: platform}
{i: os}

* [os](http://docs.python.org/library/os.html)
* [platform](http://docs.python.org/library/platform.html)

![](examples/os/which_os.py)
![](examples/os/which_os_linux.out)
![](examples/os/which_os_mac.out)


## Current directory (getcwd, pwd, chdir)
{id: pwd-current-working-directory}
{i: getcwd}
{i: pwd}
{i: chdir}

![](examples/os/cwd.py)

Linux, OSX:

```
$ pwd
```

Windows: (cd without parameters prints the current working directory)

```
> cd
```

## OS path
{id: os-path}
{i: path}
{i: abspath}
{i: exists}
{i: basename}
{i: dirname}

![](examples/os/path.py)

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

## Directory listing using glob
{id: listing-files-using-glob}
{i: glob}
{i: glob.glob}

![](examples/os/ls.py)

## Traverse directory tree - list directories recursively
{id: travers-directory-tree}
{i: walk}
{i: os.walk}

![](examples/os/traverse_tree.py)


## OS dir (mkdir, makedirs, remove, rmdir)
{id: os-dir}
{i: mkdir}
{i: makedirs}
{i: remove}
{i: unlink}
{i: rmdir}
{i: removedirs}
{i: rmtree}
{i: shutil}

* `mkdir` is like `mkdir` in Linux and Windows
* `makedirs` is like `mkdir -p` in Linux
* `remove` and `unlink` are like `rm -f` in Linux or `del` in Windows
* `rmdir` is like `rmdir`


![](examples/os/mkdir.py)

## expanduser - handle tilde ~ the home directory of the user
{id: expanduser}
{i: expanduser}
{i: ~}
{i: os.path.expanduser}

![](examples/os/expanduser.py)


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

## External command with system
{id: external-command-with-system}
{i: os.system}
{i: system}

![](examples/os/os_system.py)

If you wanted to list the content of a directory in an os independent way you'd use `os.listdir('.')`
or you could use the `glob.glob("*.py")` function to have a subset of files.


## Accessing the system environment variables from Python
{id: environment-variables}
{i: os.environ}

![](examples/os/environment.py)

{aside}
`os.environ` is a dictionary where the keys are the environment variables and the values are, well, the values.
{/aside}


## Set env and run command
{id: set-env-and-run-command}

![](examples/os/set_env.py)

{aside}
We can change the environment variables and that change will be visible in subprocesses,
but once we exit from ou Python program, the change will not persist.
{/aside}



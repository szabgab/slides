# Virtualenv

* virtualenv

On Linux/macOS:

```
$ cd project_dir
$ virtualenv -p python3 venv
$ source venv/bin/activate
$ ...
$ deactivate
```

On Windows:

```
venv\Scripts\activate.bat
...
deactivate
```

The `virtualenv` command will create a copy of python in the given directory inside the current directory.
In the above example it will create the copy in the 'venv' directory inside the 'project_dir'.
After source-ing the 'activate' file the PATH will include the local python with a local version of **pip**.
This requires bash or zsh.

See also the [Python guide](http://docs.python-guide.org/en/latest/dev/virtualenvs/).



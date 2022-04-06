# PyPi - Python Package Index
{id: python-package-index}

## What is PyPi?
{id: pypi}

* [pypi](http://pypi.python.org/)

## pip
{id: pip}
{i: pip}

```
$ pip install package_name
```

## Configure pip on Windows to avoid SSL issues
{id: configure-pip-on-windows}


On the command line:

```
pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org  PACKAGE_NAME
```

Run the following command to get the list of configuration files:

```
pip config -v list
```

You will see something like this: (your username instead of FooBar)

```
For variant 'global', will try loading 'C:\ProgramData\pip\pip.ini'
For variant 'user', will try loading 'C:\Users\FooBar\pip\pip.ini'
For variant 'user', will try loading 'D:\Data\Users\FooBar\AppData\Roaming\pip\pip.ini'
For variant 'site', will try loading 'C:\Users\FooBar\AppData\Local\Programs\Python\Python310\pip.ini'
```

Create the first `pip.ini` file with the following content:

```
[global]
trusted-host = pypi.org files.pythonhosted.org pypi.python.org
```

If you run the `pip config -v list` again, you'll see an additional line on the output:
 
```
global.trusted-host='pypi.org, files.pythonhosted.org ,pypi.python.org'
```

`pip` will now disregard the SSL issues.

## Upgrade pip
{id: upgrade-pip}

* `pip install --upgrade pip` Will probably not work on Windows because file is in use...

## Upgrade PIP on Windows
{id: upgrade-pip-on-windows}

```
py -m pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org --upgrade pip
```


## PYTHONPATH
{id: pythonpath}

```
export PYTHONPATH=~/python
```

## Virtualenv
{id: virtualenv}
{i: virtualenv}

```
$ pip install virtualenv

$ cd project_dir
$ virtualenv venv
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

{aside}
The `virtualenv` command will create a copy of python in the given directory inside the current directory.
In the above example it will create the copy in the 'venv' directory inside the 'project_dir'.
After source-ing the 'activate' file the PATH will include the local python with a local version of **pip**.
This requires bash or zsh.
{/aside}

{aside}
See also the [Python guide](http://docs.python-guide.org/en/latest/dev/virtualenvs/).
{/aside}


## Virtualenv for Python 3
{id: virtualev-python3}

```
virtualenv -p python3 venv3
source venv3/bin/activate
...
deactivate
```


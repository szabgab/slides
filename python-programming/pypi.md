# PyPi - Python Package Index
{id: python-package-index}

## What is PyPi?
{id: pypi}


<a href="http://pypi.python.org/">pypi</a>




## Easy Install
{id: easy-install}


<a href="http://pypi.python.org/pypi/setuptools">setuptools</a>



```
$ easy_install module_name
```


## pip
{id: pip}
{i: pip}

```
$ pip install package_name
```


## Upgrade pip
{id: upgrade-pip}

* **pip install --upgrade pip** Will probably not work on Windows because file is in use...
* **easy_install pip** Will work on Windows as well.



## PYTHONPATH
{id: pythonpath}

```
export PYTHONPATH=~/python
easy_install -d ~/python Genshi
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
venv\Source\activate.bat
```

{aside}

The **virtualenv** command will create a copy of python in the given directory inside the current directory.
In the above example it will create the copy in the 'venv' directory inside the 'project_dir'.
After source-ing the 'activate' file the PATH will include the local python with a local version of **pip**
and **easy_install**. This requires bash or zsh.
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





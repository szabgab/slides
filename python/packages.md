# Python Packages
{id: python-pacakges}


## Why Create package
{id: why-create-package}

{aside}
As a module gets larger and larger it will be more and more difficult to maintain.

It might be eaier if we split it up into multiple files and put those files inside
a directory. A 'package' is just that. A bunch of Python modules that belong together
and are placed in a directory hierarchy. In order to tell Python that you really
mean these files to be a package one must add a file called __init__.py in
each directory of the project. In the most simple case the file can be empty.
{/aside}

* Code reuse
* Separation of concerns
* Easier distribution


## Create package
{id: create-package}
{i: __init__.py}

```
mymath/
    __init__.py
    calc.py
    ...
    internal_use.py
```

![](examples/package/1/mymath/calc.py)
![](examples/package/1/mymath/__init__.py)


## Internal usage
{id: internal-usage}

![](examples/package/1/mymath/internal_use.py)


```
cd examples/package
python 1/mymath/internal_use.py
```

## use module in package - relative path
{id: use-package-module}

![](examples/package/use_project/proj1_1.py)
![](examples/package/use_project/proj1_1.out)


## use package (does not work)
{id: use-package}

![](examples/package/use_project/proj1_2.py)
![](examples/package/use_project/proj1_2.out)

If we import the main package name, it does not have access to the module inside.



## package importing (and exporting) module
{id: package-importing-module}
{i: __init__.py}

Put import (and thus re-export) in __init__.py

![](examples/package/2/mymath/calc.py)
![](examples/package/2/mymath/__init__.py)


## use package (module) with import
{id: use-package-module-with-import}

Still works...

![](examples/package/use_project/proj2_1.py)


## use package with import
{id: use-package-with-import}

Now we can import the module from the package and use that.

![](examples/package/use_project/proj2_2.py)



## Creating an installable Python package
{id: package-basics}

The directory layout of a package:


```
├── mymath
│   ├── calc.py
│   └── __init__.py
└── setup.py
```
![](examples/package/2/setup.py)



## Create tar.gz file
{id: package-sdist}

```
$ python setup.py sdist
```

* mymath.egg-info/
* dist/mymath-0.1.tar.gz



```
running sdist
running egg_info
creating mymath.egg-info
writing mymath.egg-info/PKG-INFO
writing top-level names to mymath.egg-info/top_level.txt
writing dependency_links to mymath.egg-info/dependency_links.txt
writing manifest file 'mymath.egg-info/SOURCES.txt'
reading manifest file 'mymath.egg-info/SOURCES.txt'
writing manifest file 'mymath.egg-info/SOURCES.txt'
warning: sdist: standard file not found: should have one of README, README.txt

creating mymath-0.1
creating mymath-0.1/mymath
creating mymath-0.1/mymath.egg-info
making hard links in mymath-0.1...
hard linking setup.py -> mymath-0.1
hard linking mymath/__init__.py -> mymath-0.1/mymath
hard linking mymath.egg-info/PKG-INFO -> mymath-0.1/mymath.egg-info
hard linking mymath.egg-info/SOURCES.txt -> mymath-0.1/mymath.egg-info
hard linking mymath.egg-info/dependency_links.txt -> mymath-0.1/mymath.egg-info
hard linking mymath.egg-info/not-zip-safe -> mymath-0.1/mymath.egg-info
hard linking mymath.egg-info/top_level.txt -> mymath-0.1/mymath.egg-info
Writing mymath-0.1/setup.cfg
creating dist
Creating tar archive
removing 'mymath-0.1' (and everything under it)
```


## Install Package
{id: package-install}
{i: pip}
{i: easy_install}


```
$ pip install dist/mymath-0.1.tar.gz
```

```
$ easy_install --prefix ~/python/  dist/mymath-0.1.tar.gz
```

```
$ python setup.py install --prefix ~/python/
```

Upload to [PyPi](https://pypi.python.org/) or distribute to your users.


## Dependencies
{id: package-dependencies}

```
requires=[
    'lawyerup',
],
```

To list them


```
$ python setup.py --requires
```


In the setup.py file we only need to change the version number and we
can release a new version of the package.





## Add README file
{id: package-other-file}

```
.
├── bin
│   ├── runmymath.bat
│   └── runmymath.py
├── MANIFEST.in
├── mymath
│   └── test
│       ├── __init__.py
│       ├── test_all.py
│       └── test_calc.py
├── README.rst
└── setup.py
```
![](examples/package/3/README.rst)
![](examples/package/3/MANIFEST.in)


## Add README file (setup.py)
{id: package-add-readme}

In the setup.py add the following function:


```
def readme():
    with open('README.rst') as f:
        return f.read()
```


and in the setup() call include the following parameter:



```
      long_description=readme(),
```

This will display the README file when called at


```
$ python setup.py --long-description
```



## Include executables
{id: package-executables}

```
root/
  setup.py
  README.rst
  MANIFEST.in
  bin/
    runmymath.py
    runmymath.bat
  mymath/
    __init__.py
    calc.py
```
![](examples/package/3/bin/runmymath.py)
![](examples/package/3/bin/runmymath.bat)

setup.py will need to get


```
    scripts=['bin/runmymath.py', 'bin/runmymath.bat'],
```



## Add tests
{id: add-tests}
{i: unittest}
{i: discover}

```
    root/
      setup.py
      README.rst
      MANIFEST.in
      bin/
        runmymath.py
        runmymath.bat
      mymath/
        __init__.py
        calc.py
        test/
          __init__.py
          test_all.py
          test_calc.py
```
![](examples/package/3/mymath/test/__init__.py)

```
python mymath/test/test_calc.py
python mymath/test/test_all.py
```

```
python -m unittest discover
```



## Add tests calc
{id: add-tests-calc}
![](examples/package/3/mymath/test/test_calc.py)


## Add tests all
{id: add-tests-all}
![](examples/package/3/mymath/test/test_all.py)


## setup.py
{id: package-setup2}

![](examples/package/3/setup.py)


## Run tests and create package
{id: run-test-and-create-package}

```
python setup.py test
python setup.py sdist
```

## Exercise: package
{id: exercise-package}

* Go to [Pypi](https://pypi.org/), find some interesting module and install it in a non-standard location (or in a virtualenv)
* Check if it was installed (try to import it in a python script).
* Take one of the previously created modules, and create a package for it.
* Install this new package in a non-standard location.
* Check if it works from some other place in your file-system.

* Take the mymath package, add another method, add tests and create the distubtable zip file.

## Exercise: create executable
{id: exercise-create-executable}

* Go over some of the examples in the course and package that.
* Package a script using some of your favorite modules.



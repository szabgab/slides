# Distribution of Python code
{id: distribution}

## Distribution demo 1
{id: demo1}

![](examples/distribution/demo1/demo1.py)
![](examples/distribution/demo1/setup.py)


* Install from the current folder

```
pip install .
```

* Use it on the command line: (try it in a different folder!)

```
python -m demo1

/home/gabor/venv3/lib/python3.10/site-packages/demo1.py
```

* Use it in the interactive shell

```
python
>>> import demo1
>>> demo1.whoami()
```

* Uninstall (without asking questions)

```
pip uninstall demo1 --yes
```

![](examples/distribution/demo1/.gitignore)

## Distribution demo 2
{id: demo2}

* The name of the package (demo2a in setup.py) and the name of the module (the filename demo2b.py ) don't neet to be the same.
* The name of the folder (demo2)

![](examples/distribution/demo2/demo2b.py)
![](examples/distribution/demo2/setup.py)


* Install:

```
pip install .
```

* Use the name of the module

```
python -m demo2b
```

* Uninstall using the package name

```
pip uninstall demo2a --yes
```

## Distribution demo 3
{id: demo3}

One package with multiple python files

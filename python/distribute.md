# Distribute Python application as an exe
{id: distribute}

## Packaging applications (creating executable binaries)
{id: packaging-applications}
{i: py2exe}
{i: Freeze}
{i: py2app}
{i: cx_Freeze}
{i: PyInstaller}

* [py2exe](http://www.py2exe.org/) on Windows (discontinued)
* [Freeze](https://wiki.python.org/moin/Freeze) on Linux
* [py2app](https://py2app.readthedocs.io/en/latest/) on Mac
* [cx_Freeze](http://cx-freeze.sourceforge.net/) cross-platform
* [PyInstaller](http://www.pyinstaller.org/) cross-platform
* [Auto Py To Exe](https://nitratine.net/blog/post/auto-py-to-exe/)


## Using PyInstaller
{id: pyinstaller}

![](examples/package/hello_world.py)

```
pip install pyinstaller
pyinstaller myscript.py
pyinstaller --onefile hello_world.py
```

* See the results in dist/

## Other PyInstaller examples
{id: pyinstaller-and-sys}

Use this to see where does the packaged version of our code look for modules:

![](examples/package/syspath.py)


Use this to see how to pass command line parameters to the packaged exe:

![](examples/package/cli.py)


## Other
{id: pyinstaller-other}

```
pyinstaller --onefile --windowed myscript.py
```

## Py2app for Mac
{id: py2app}

```
pip install py2app
py2applet examples/other/hello.py
```



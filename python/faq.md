# FAQ
{id: python-faq}


## How not to name example scirpts?
{id: file-naming-advice}


Don't - by mistake - call one of your files the same as a module you will be loading.
For example `random.py` is a bad idea if you will `import random`.
Your code will try to locate random.py to load, but will find itself and not the one that comes with Python.


Python will also create a random.pyc file - a compiled file - and it will take time till you recall this
and delete that too.
Till then the whole thing will seem to be broken.

## Platform independent code
{id: platform-independent-code}

In general Python is platform independent, but still needs some care to make sure
you don't step on some aspects of Operating System or the file system that works differently
on other OS-es.

* Filenames are case sensitive on some OS-es (e.g. Windows). They used to be restricted to 8.3. Make sure you are within the restriction of every OS you might want to use.
* Directory path: (slash or backslash or something else?) use the os.path methods.
* os.path.expanduser('~') works on both Linux and Windows, but the root of a Linux/Unix file system starts with a slash (/) and on Windows it is c:\ and d:\ etc.
* On Linux/Unix you have user 'root' and on Windows 'Administrator'
* File permissions are different on Linux and Windows.
* Stay away from OS specific calls, but as a last resort use os.name or sys.platform to figure out which os is this. os.name is 'posix' on Linux and 'nt' on Windows.
* For GUI use wxWindows that has a native look on Windows and Gnome look on Linux.
* Pay attention to any 32/64 bit issues. Big/Little Endian issues.
* Some modules might be OS specific. Check the documentation.
* Pay attention to the use of os.system and subsystem modules.


## How to profile a python code to find causes of slowness?
{id: profile}

Use one of these modules:


* cProfile is in C. It is faster and preferable.
* profile


## pdb = Python Debugger
{id: pdb-debugger}
{i: pdb}

Include the following code in your script at any point, and run the script as you'd do normally.
It will stop at the given point and enter the debugger.



```
import pdb; pdb.set_trace()
```

[pdb](http://docs.python.org/library/pdb.html)



## Avoid Redefining functions
{id: avoid-redefining-functions}

Can I tell python to stop compilation when someone is redefining a function?
Or at least give me a warning?

Use `pylint` for that

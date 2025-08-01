# How not to name example scirpts?

Don't - by mistake - call one of your files the same as a module you will be loading.
For example `random.py` is a bad idea if you will `import random`.
Your code will try to locate random.py to load, but will find itself and not the one that comes with Python.


Python will also create a random.pyc file - a compiled file - and it will take time till you recall this
and delete that too.
Till then the whole thing will seem to be broken.



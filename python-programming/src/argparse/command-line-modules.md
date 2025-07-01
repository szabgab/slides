# Modules to handle the command line


* argparse

You would like to allow the user to pass arguments on the command line. For example:


```
myprog.py server_name name True True

myprog.py --machine server_name --test name --verbose --debug
myprog.py -v -d
myprog.py -vd
myprog.py -dv
myprog.py -v -d -m server_name
myprog.py -vdm server_name
myprog.py file1 file2 file3
myprog.py file1 file2 file3
myprog.py --machine server_name --debug file1 file2 file3
myprog.py file1 file2 file3 --machine server_name --debug
```

* [sys.argv](http://docs.python.org/library/sys.html)  manual parsing?
* [argparse](http://docs.python.org/library/argparse.html)



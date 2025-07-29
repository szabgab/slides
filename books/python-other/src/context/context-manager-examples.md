# Context Manager examples

A few examples where context managers can be useful:

* Opening a file - close it once we are done with it so we don't leak file descriptors.
* Changing directory - change back when we are done.
* Create temporary directory - remove when we are done.
* Open connection to database - close connection.
* Open SSH connection - close connection.

* More information about [context managers](https://jeffknupp.com/blog/2016/03/07/python-with-context-managers/)



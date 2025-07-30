# Why Create package

As a module gets larger and larger it will be more and more difficult to maintain.

It might be eaier if we split it up into multiple files and put those files inside
a directory. A 'package' is just that. A bunch of Python modules that belong together
and are placed in a directory hierarchy. In order to tell Python that you really
mean these files to be a package one must add a file called __init__.py in
each directory of the project. In the most simple case the file can be empty.


* Code reuse
* Separation of concerns
* Easier distribution


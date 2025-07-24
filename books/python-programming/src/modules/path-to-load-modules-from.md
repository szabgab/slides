# path to load modules from - The module search path


* PYTHONPATH
* .pth


There are several steps Python does when it searches for the location of a file to be imported, but the most important
one is what we see on the next page in sys.path.


1. The directory where the main script is located.
1. The directories listed in PYTHONPATH environment variable.
1. Directories of standard libraries.
1. Directories listed in .pth files.
1. The site-packages home of third-party extensions.





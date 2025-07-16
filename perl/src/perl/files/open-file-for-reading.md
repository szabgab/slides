# Opening file for reading

* open

```
While working over most of the operating systems today, no program can
access a file directly. This is in order to allow the Operating System
to apply user rights.

Before you can read from a file you have to ask the Operating System to "open"
it for you. When opening a file you provide a variable that will become your
handle to the opened file. It is called a filehandle.
```
{% embed include file="src/examples/files-perl/open_file.pl" %}


[Open and read from text files](https://perlmaven.com/open-and-read-from-files)




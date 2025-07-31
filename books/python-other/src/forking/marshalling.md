# Marshalling / Serialization

Marshalling (or serialization) is the operation when we take an arbitrary
data structure and convert it into a string in a way that we can convert
the string back to the same data structure.

Marshalling can be used to save data persistent between execution of the same
script, to transfer data between processes, or even between machines.
In some cases it can be used to communicate between two processes written in
different programming languages.

The [marshal](http://docs.python.org/library/marshal.html) module
provides such features but it is not recommended as it was built
for internal object serialization for python.

The [pickle](http://docs.python.org/library/pickle.html) module was designed for this task.

The [json](https://docs.python.org/library/json.html) module can be used too.





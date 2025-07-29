# open in function


This is not the recommended way to open a file, but this is how it was done before the introduction of the `with` context manager.
Here we have the same issue. We have a conditional call to `return` where we forgot to close the file.


{% embed include file="src/examples/context/no_context_fh.py" %}



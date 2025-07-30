# Inspect

The [inspect](http://docs.python.org/library/inspect.html) module provides introspection to Python runtime.
`inspect.stack` returns the stack-trace. Element 0 is the deepes (where we called inspect stack).
Each level has several values. A represantation of the frame, filename, linenumber, subroutine-name.


{% embed include file="src/examples/advanced-functions/caller.py" %}


python caller.py 1


{% embed include file="src/examples/advanced-functions/caller_1.out" %}



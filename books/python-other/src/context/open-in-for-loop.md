# open in for loop

* stat
* os.stat


Calling `write` does not immediately write to disk. The Operating System provides buffering as an optimization
to avoid frequent access to the disk. In this case it means the file has not been saved before we already check its size.


{% embed include file="src/examples/context/save.py" %}




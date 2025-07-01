# Module to open files and calculate something



Of course in the previous example, it would be probably
much easier if we just checked if the number was 0,
before trying to divide with it. There are many other cases
when this is not possible. For example it is impossible to
check if open a file will succeed, without actually trying
to open the file.




In this example we open the file, read the first line which
is a number and use that for division.




When the open() fails, Python throws an FileNotFoundError exception.

{% embed include file="src/examples/exceptions/module.py" %}




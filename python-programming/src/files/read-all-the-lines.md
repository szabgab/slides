# Read all the lines into a list


* readlines


There are rare cases when you need the whole content of a file in the memory and you cannot process it line by line.
In those rare cases we have several options. `readlines` will read the whole content into a list converting each line
from the file to be an element in the list.

Beware though, if the file is too big, it might not fit in the free memory of the computer.


{% embed include file="src/examples/files/read_full_file.py" %}

**Output:**

{% embed include file="src/examples/files/read_full_file.out" %}



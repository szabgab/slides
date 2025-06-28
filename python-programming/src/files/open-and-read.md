# Open and read file (easy but not recommended)



In some code you will encounter the following way of opening files.
This was used before "with" was added to the language.
It is not a recommended way of opening a file as you might easily forget
to call "close" and that might cause trouble. For example you might loose data.
Don't do that.

I am showing this as the first example, because it is easuer to understand.


{% embed include file="src/examples/files/open_and_read.py" %}



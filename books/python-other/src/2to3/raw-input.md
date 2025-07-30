# input and raw_input

* raw_input
* input


`raw_input()` was renamed to `input()`

In Python 2 `raw_input()` returned the raw string. input(), on the other hand ran eval(raw_input())
which meant it tried to execute the input string as a piece of Python code. This was dangerous and was not really used.


In Python 3 raw_input() is gone. input() behaves as the old raw_input() returning the raw string. If you would like to get the old,
and dangerous, behavior of input() you can call eval(input()).




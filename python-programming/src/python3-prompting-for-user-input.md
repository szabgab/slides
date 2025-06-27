# Prompting for user input in Python 3


* input
* prompt
* STDIN


In Python 3 the **raw_input()** function was replaced by the **input()** function.


{% embed include file="src/examples/basics/prompt3.py" %}

What happens if you run this using Python 2 ?

```
/usr/bin/python2 prompt3.py
```

* What happens if we type in "Foo Bar"

{% embed include file="src/examples/basics/prompt3_1.err" %}

* What happens if we type in just "Foo" - no spaces:

{% embed include file="src/examples/basics/prompt3_2.err" %}

* The next example shows a way to exploit the `input` function in Python 2 to delete the currently running script. You know, just for fun.

{% embed include file="src/examples/basics/prompt3_3.err" %}



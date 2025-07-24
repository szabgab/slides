# Test blocks (use subtest instead)

* {}}


Create small blocks of tests



When writing a test script you often write similar pieces of code that do
unrelated tests. You can reuse the same variables throughout the test script
but that means that in case of a bug in the test script the various parts might
have effects on each other.

You can also invent new names for the variables but there are only so many names
you can reasonably use for the same kind of data.

The best solution probably is to put the individual pieces into anonymous blocks.
That serves several purposes. First of all it makes clear to both the writer of the
code and the reader that the blocks are mostly independent.
It also ensures that the variables used in one block won't interfere with the variables
in the other block. You'll even have to define these variables in both blocks.


{% embed include file="src/examples/test-perl/t/blocks.t" %}



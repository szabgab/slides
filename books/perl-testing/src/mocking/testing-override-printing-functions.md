# Override printing functions (mocking)

* redefine


Sometimes there are functions that print directly to the screen.

The program could be tested as an external application or we can redirect the
STDOUT to a scalar variable in the memory of perl but  it might be cleaner
to replace the display function, capture the data in a variable
and then check that variable.


{% embed include file="src/examples/test-perl/t/display.t" %}




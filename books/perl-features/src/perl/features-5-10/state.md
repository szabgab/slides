# state variable

* state
* static


In Perl 5.10 the state keyword was added that allows us to create a static variable. When we declare such variable in a function the declaration and the initialization
takes places only once no matter how many times the function is called. Instead of being initialized every time we enter the function like a variable declared with `my` would
do, `state` variables are initialized only once and then they remember their value for the subsequent calls to the same function.


{% embed include file="src/examples/feature/state.pl" %}
{% embed include file="src/examples/feature/state.out" %}




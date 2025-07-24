# Scope of variables

* scope


Let's see an example where we create an array and a reference
to it in some arbitrary {} scope. The array is defined within
the scope while the variable holding the reference is defined
outside the scope.


{% embed include file="src/examples/references/scope_of_variables.pl" %}
{% embed include file="src/examples/references/reference_counting.pl" %}


After the closing } @names went out of scope already
but $names_ref still lets us access the values.

As $names_ref still holds the reference to the location
of the original array in the memory perl keeps the content
of the array intact.



# Integer assignment is copying (not pointer)

Normally, that is without the use of pointers if we assign a variable that contains a number, we create a copy of the value in
a new place in the memory. Then if we change the value of the original variable (in this case if we increment it by one),
then only the content of that variable changes.

The same happens if we change the new variable (in this case assigning 3 to it), only the content of that variable changes.

Normally this is what you want in regular assignment.


{% embed include file="src/examples/no-pointer/no_pointer.go" %}
{% embed include file="src/examples/no-pointer/no_pointer.out" %}



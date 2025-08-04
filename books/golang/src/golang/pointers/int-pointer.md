# Pointer to integer

* &
* *


We can use the & prefix during the assignment that means: take the pointer to this variable and copy the pointer.
This means that the new variable (b in our case) will point to the same place in memory where the value of the original
variable is. The content was not copied.

If at this point you print out the content of the new variable, you'll see the hexadecimal value of the pointer.
In order to print out the real value you need to prefix the variable by a *.

If you now change the original variable, you'll see both are incremented.
If you change the new variable (you'll have to use the * prefix for this)  both are incremented.

Maybe it is better to say that there is only one value jut two ways to access it.

I think you would rarely do this in such code, but it is important to understand the concept for when
we will want to pass a variable by reference to a function.


* `&amp;` get pointer to
* `*` get value behind pointer

{% embed include file="src/examples/int-pointer/int_pointer.go" %}
{% embed include file="src/examples/int-pointer/int_pointer.out" %}



# Variable declaration (var)

* var
* :=


* There are 3 ways to declare variables in Go


The first one, the one that we have already seen uses the `:=` operator. It declares a variable and immediately assigns a value to it. The type of the variable is deducted from the value assigned to it.



The second in our example uses the `var` keyword and explicitely sets the type. `var b int32 = 2` This is used when we would like to fine-tune the type of the variable.




In the third example `var a int16` we declare the variable but we don't assign any value to it yet. This is used when need don't know the initial value when we declare the variable. This can happen, for example, when we are looking for some value in a loop, and we would like the result to be available outside of the loop. This is related to the scoping of variables that we'll discuss later.


{% embed include file="src/examples/variables/variables.go" %}
{% embed include file="src/examples/variables/variables.out" %}




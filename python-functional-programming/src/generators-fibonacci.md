# Fibonacci - generator

{% embed include file="src/examples/generators/fibonacci_generator.py" %}

**Output:**

{% embed include file="src/examples/generators/fibonacci_generator.out" %}

When we enter the for loop the fibonacci() function is called and returns a generator object.
Then `next` is called on this generator object which executes the content of the function up to the call of `yield`
and return the value. Then ever time the for-loop calls `next` the function continues running till it reaches `yield`
again or till it reaches the end of the function. (Which will never happen in this case.)



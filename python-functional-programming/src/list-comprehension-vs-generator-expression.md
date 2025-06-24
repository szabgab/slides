# List comprehension vs Generator Expression - less memory

Let's use a bigger range of numbers and create the corresponding list and generator. Then check the size of both of them.
You can see the list is much bigger. That's becuse the list already contains all the elements, while the generator contains
only the promise to give you all the elements.

As we could see in the previous example, this is not an empty promise, you can indeed iterate over the elements of a generator
just as you can iterate over the elements of a list.

However, you cannot access an arbitrary element of a generator because the generator is not **subscriptable**.


{% embed include file="src/examples/generators/generator_expression.py" %}

**Output:**

{% embed include file="src/examples/generators/generator_expression.out" %}

[List Comprehension vs Generator Expressions](https://code-maven.com/list-comprehension-vs-generator-expression)



getsizeof

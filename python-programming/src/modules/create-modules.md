# Create modules


A module is just a Python file with a set of functions that us usually not used by itself. For example the "my_calculator.py".


{% embed include file="src/examples/modules/my_calculator.py" %}


A user made module is loaded exactly the same way as the built-in module.
The functions defined in the module are used as if they were methods with the dot-notation.


{% embed include file="src/examples/modules/add.py" %}



We can import specific functions to the current name space (symbol table) and then we don't need to prefix it with the name of
the file every time we use it. This might be shorter writing, but if we import the same function name from two different
modules then they will overwrite each other. So I usually prefer loading the module as in the previous example.


{% embed include file="src/examples/modules/add_from.py" %}

* Using with an alias

{% embed include file="src/examples/modules/add_as.py" %}



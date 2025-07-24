# Runtime loading of modules



The import statements in Python are executed at the point where they are located in the code.
If you have some code before the import statement (print Start running) it will be executed before the importing starts.

During the importing any code that is outside of functions and classes in the imported module is executed. (print Loading mygreet).

Then you can call functions from the module (print Hello World).

Or call code that is in the importing program (print DONE).


{% embed include file="src/examples/modules/mygreet.py" %}
{% embed include file="src/examples/modules/load_mygreet.py" %}
{% embed include file="src/examples/modules/runtime_loading.py" %}




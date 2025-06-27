# A main function


* main
* def


You could write your code in the main body of your Python file, but using functions
and passing arguments to it will make your code easier to maintain and understand.
Therefore I recommend that you always write every script with a function called "main".

* Function definition starts with the **def** keyword, followed by the name of the new function ("main" in this case), followed by the list of **parameters in parentheses** (nothing in this case).
* The content or body of the function is then **indented** to the right.
* The function definition ends when the indentation stops.

If you execute this file you might be surprised that nothing happens. This is so because we only **defined** the function, we never used it. We'll do that next.


{% embed include file="src/examples/basics/hello_world_main.py" %}

This won't run as the main function is declared, but it is never called (invoked).


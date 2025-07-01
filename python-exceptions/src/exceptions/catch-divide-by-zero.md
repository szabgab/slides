# Catch ZeroDivisionError exception

* except
* ZeroDivisionError


For that, we'll wrap the critical part of the code in a "try" block.
After the "try" block we need to provide a list of exception that are
caught by this try-block.



You could say something like
"Try this code and let all the exceptions propagate, except of the ones I listed".




As we saw in the previous example, the specific error is called ZeroDivisionError.




If the specified exception occurs within the try: block, instead of the script ending,
only the try block end and the except: block is executed.


{% embed include file="src/examples/exceptions/divide_by_zero_catch.py" %}




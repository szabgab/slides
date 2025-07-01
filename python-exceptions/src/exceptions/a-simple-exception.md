# A simple exception

* ZeroDivisionError



When something goes wrong, Python throws (raises) an exception. For example,
trying to divide a number by 0 won't work. If the exception is not
handled, it will end the execution.




In some programming languages we use the expression "throwing an exception" in other languages the expression is "raising an exception".
I use the two expressions interchangeably.




In the next simple example, Python will print the string before the division,
then it will throw an exception, printing it to the standard error that is
the screen by default. Then the script stops working and the
string "after" is not printed.


{% embed include file="src/examples/exceptions/divide_by_zero.py" %}



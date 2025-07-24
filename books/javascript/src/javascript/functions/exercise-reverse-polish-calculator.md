# Exercise: Reverse Polish Calculator

A regular "inline" calcularo accespts the operator between two operands:
2 + 3. If we have more operators and operands such a 2 + 3 * 7, we (and the computer)
need to know the precedence of the operators.



In a Polish calculator we would write the operator before the operands: + 2 3.
In a Reverse Polish Calculator we would write the operator after the operands: 2 3 +
or 2 3 7 * +. Once we wrote down an expression the order of computation is clear.
(First apply * to 3 and 7 and the apply + to the result and 2)



In this exercise you are requeted to implement a Reverse Polish Calculator that can handle
+, -, *, /, and that will remove and display the last value when an = character is entered.



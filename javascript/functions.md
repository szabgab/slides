# JavaScript functions
{id: javascript-functions}

## Function statements
{id: functions}
{i: function}
![](examples/functions/add.js)


## Function expressions (Anonymous functions)
{id: anonymous-functions}
![](examples/functions/anonymous_functions.js)


## Unknown number of function arguments
{id: function-arguments}
{i: arguments}
![](examples/functions/sum.js)


## Assign function
{id: assign-functions}
![](examples/functions/assign_functions.js)

{aside}

We can assign the name of a function to a variable. Now we have the same function
with two names. We can call both using the function_name() notation.
We can even print the source code of the function in either of the variables.
{/aside}


## Passing functions as parameter of another function
{id: passing-function-as-parameter}
![](examples/functions/passing_function.js)



## Recursive function
{id: recursive-function}
![](examples/functions/factorial.js)


## Dispatch table
{id: dispatch-table}
![](examples/functions/dispatch_table.js)


## Variable scope
{id: variable-scope}
{i: scope}
![](examples/functions/scope.js)

{aside}

There is global scope and there is local scope inside functions.
{/aside}


## Scope in if block
{id: scope-in-if-block}
![](examples/functions/scope_in_if.js)

{aside}

if-blocks, don't create local scopes.
{/aside}


## Variable in for loop
{id: variable-in-for-loop}
![](examples/functions/variable_in_for_loop.js)

{aside}

for-oops, don't create local scopes.
{/aside}


## Immediate Execution using ()
{id: immediate-execution}
{i: ()}
![](examples/functions/execute.js)


## Immediate Execution with parameters using ()
{id: immediate-execution-params}
{i: ()}
![](examples/functions/execute_params.js)


## Private Global Scope
{id: private-global-scope}

![](examples/functions/private_scope.js)


## Exercise: Reverse Polish Calculator
{id: exercise-reverse-polish-calculator}

A regular "inline" calcularo accespts the operator between two operands:
2 + 3. If we have more operators and operands such a 2 + 3 * 7, we (and the computer)
need to know the precedence of the operators.



In a Polish calculator we would write the operator before the operands: + 2 3.
In a Reverse Polish Calculator we would write the operator after the operands: 2 3 +
or 2 3 7 * +. Once we wrote down an expression the order of computation is clear.
(First apply * to 3 and 7 and the apply + to the result and 2)



In this exercise you are requeted to implement a Reverse Polish Calculator that can handle
+, -, *, /, and that will remove and display the last value when an = character is entered.




## Reverse Polish Calculator in JavaScript
{id: reverse-polish-calculator}

![](examples/functions/reverse_polish_calculator.js)

## Order
{id: function-order}

![](examples/functions/order.js)

![](examples/functions/fibonacci.js)


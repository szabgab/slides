# Bad Parts

Based on Appendix B of  "JavaScript: The Good Parts"


1. == and !=  are bad. Always use === and !==
1. with statement - avoid it
1. eval - can be dangerous. Don't use it.
1. continue - Douglas Crockford recommends to avoid it as you can write code without it.
1. switch - Always break. Don't let it fall through.
1. Block-less statement - always use {} after 'if'.
1. ++ -- - Douglas Crockford recommends to avoid them. I think there are places where they can be used without problems.
1. Bitwise operators - usually there is no need for them in JavaScript.
1. Function statement vs Function expressions
1. Typed Wrappers - avoid new Boolean, new Number, new String, new Array, new Object
1. new - name constructor functions with leading capital letter, or even better: avoid using 'new'.
1. void - avoid it

{% embed include file="src/examples/js/function_statement.js" %}
{% embed include file="src/examples/js/function_expression.js" %}


A good way to enforce that everything is private is to wrap the whole
code in an anonymous function expression, and execute it upon parsing it.


{% embed include file="src/examples/js/global_function_expression.js" %}


The official ECMAScript grammar states, that if the first word is 'function'
then it is part of a function statement, but this is a function expression.
That why we add a pair of () around the function.




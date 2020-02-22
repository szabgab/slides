# JavaScript Appendix
{id: appendix}


## Resources
{id: javascript-resources}

* JavaScript and DHTML Cookbook By Danny Goodman
* JavaScript: The Definitive Guide, Fourth Edition By David Flanagan
* [Eloquent JavaScript](http://eloquentjavascript.net/)
* [Mozilla Developer Network](https://developer.mozilla.org/)
* [JS Fiddle](http://jsfiddle.net/)
* [Daily JS](http://dailyjs.com/)
* [JavaScript Equality Table](https://dorey.github.io/JavaScript-Equality-Table/)
* [CodePen](http://codepen.io/pen/)



## JavaScript Videos
{id: javascript-videos}

* [Doug Crockford: JavaScript: The Good Parts](https://www.youtube.com/watch?v=hQVTIJBZook) (2009)
* [Douglas Crockford: The Better Parts - Nordic.js](https://www.youtube.com/watch?v=PSGEjv3Tqo0) (2014)
* [Crockford on JavaScript - Episode IV: The Metamorphosis of Ajax](https://www.youtube.com/watch?v=Fv9qT9joc0M) (2011)



Other



* [Douglas Crockford: Which way is forward](https://www.youtube.com/watch?v=6eOhyEKUJko) (2013)
* [avaScript You Need to Know for a Job](http://insights.dice.com/2015/06/04/javascript-you-need-to-know-for-a-job/)
* [Constructors Considered Mildly Confusing](http://zeekat.nl/articles/constructors-considered-mildly-confusing.html)




## JavaScript Tools
{id: javascript-tools}

* [JSLint](http://www.jslint.com/) Find common coding problems in JavaScript
* [JSLint Errors](https://jslinterrors.com/) a site to explain the errors of JSLint and to give suggestions how to fix them.



## Reserved words in JavaScript
{id: reserved-words}


abstract boolean break byte case catch char class const continue
debugger default delete do double else enum export extends false final
finally float for
function goto if implements import in instanceof int interface long native new null
package private protected public return short static super switch synchronized this
throw throws transient true try typeof var volatile void while with






## Awful parts
{id: awful-parts}

Based on Appendix A of  "JavaScript: The Good Parts"


1. Global variables - (window.fname = 'Foo'; fname = 'Foo'; var fname = 'Foo';), declare variables using 'var' inside functions
1. Scope only functions create local scope. Declare variable at the top of the functions.
1. Semicolon insertion.
1. Reserved words. var case = 23;  SyntaxError: missing variable name
1. Unicode: JavaScript characters are 16 bit (either UCS-2 or UTF-16. Most of them use UTF-16)
1. typeof returning 'object' for null and array as well. typeof /a/ can be either 'object' or 'function' depending on browser.
1. parseInt (leading 0 might make the number base-8 in some browsers. User radix to ensure base)
1. + can (numeric) add or concatenate strings. It works as 'add' only if both operands are numbers.
1. Floating point - is not perfect representation. Use integers.
1. NaN - NaN === NaN // false; NaN !== NaN // true;  isNaN()
1. Phony Arrays
1. Falsy values
1. hasOwnProperty is not truely reliable as it is a method that can be replaced.
1. Objects are never truly empty like a hash in Perl or a dictionary in Python.

![](examples/js/semicolon.html)
![](examples/js/reserved_words.html)
![](examples/js/is_object.html)
![](examples/js/is_array.html)
![](examples/js/parseint.html)


## Bad Parts
{id: bad-parts}

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

![](examples/js/function_statement.js)
![](examples/js/function_expression.js)


A good way to enforce that everything is private is to wrap the whole
code in an anonymous function expression, and execute it upon parsing it.


![](examples/js/global_function_expression.js)


The official ECMAScript grammar states, that if the first word is 'function'
then it is part of a function statement, but this is a function expression.
That why we add a pair of () around the function.




## JSLint
{id: jslint}

Based on Appendix C of  "JavaScript: The Good Parts"


1. Declare all the variables using 'var'. Use /*global to declare what can be global.
1. Members - JSLint will list all the used members.
1. Options to JSLint
1. Semicolons
1. Line Breaking
1. Comma - don't use it as operator
1. Required Blocks
1. Expression Statements
1. for x in y - object.hasOwnProperty
1. switch
1. var
1. with
1. ...



## Deep copy
{id: deep-copy}
{i: JSON}
![](examples/arrays/deep_copy.js)


## Invocation patterns
{id: invocation-patterns}
{i: this}

* Method invocation   (this is bound to the object)
* Function invocation (this is bound to the global object)
* Constructor invocation
* Apply invocation  (this is bound to what we passed to it)



## Apply
{id: apply}
{i: apply}
![](examples/functions/apply.js)






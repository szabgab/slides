# Awful parts

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

{% embed include file="src/examples/js/semicolon.html" %}
{% embed include file="src/examples/js/reserved_words.html" %}
{% embed include file="src/examples/js/is_object.html" %}
{% embed include file="src/examples/js/is_array.html" %}
{% embed include file="src/examples/js/parseint.html" %}




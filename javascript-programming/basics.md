# JavaScript basics
{id: basics}

## Numerical Operators
{id: numerical-operators}
{i: +}
{i: -}
{i: *}
{i: %}
{i: ++}
{i: --}
{i: +=}

* autoincrement ++, autodecrement --
* shorthand +=, /=, *=, -=

![](examples/js/numerical_operators.js)


## String operations
{id: string}
{i: trim}
{i: length}
{i: charAt}
{i: \t}
{i: \n}
{i: \\}
![](examples/js/strings.js)

* length is an attribute
* trim() is a method


```
\t - tab
\n - newline
\" - to escape a quote
\\ - to escpae a backslash
```

Note: + acts both on numbers and on strings



## String index and slice
{id: string-index}
{i: length}
{i: slice}
{i: charAt}
![](examples/js/string_characters.js)


## indexOf, lastIndexOf
{id: indexof}
{i: indexOf}
{i: lastIndexOf}
![](examples/js/index.js)


## substr, slice, and substring
{id: substring}
{i: substring}
{i: substr}

* substr - (from, length?)
* slice - (from, to?)
* substring - (from, to?)  (Use slice instead!)

![](examples/js/substring.js)


## Concatenate strings
{id: concatenate-strings}
{i: +}
{i: concat}
![](examples/js/concatenate.js)


## Replace substring
{id: replace-substring}
{i: replace}
![](examples/js/replace.js)

We'll see a more powerful version of this in the chapter about Regular expressions.



## Mixing numbers and strings
{id: mixing-numbers-and-strings}
{i: +}
![](examples/js/mixing.js)

In a nutshell: Don't do that!



## Converting between numbers and strings
{id: converting-numbers-and-strings}
{i: parseInt}
{i: parseFloat}
{i: Number}
{i: toString}
{i: String}
![](examples/js/converting.js)


## Convert octal, hexa
{id: convert-octal-hexa-to-decimal}
{i: parseInt}

* octal
* hex

![](examples/js/convert_with_base.js)


## Converting decimal to hexa
{id: converting-decimal-to-hexa}
{i: toString}
{i: toUpperCase}
![](examples/js/hexa.js)


## Browser IO (HTML)
{id: browser-io-html}
![](examples/js/browser-io.html)


## Browser IO (JavaScript)
{id: browser-io-javascript}
![](examples/js/browser-io.js)


## Exercise: Hello World on pressing button
{id: exercise-hello-world}


Create an HTML page with a button on it. When the user presses the button
display the text. "Hello World"




## Solution: Hello World on pressing button
{id: solution-hello-world}
![](examples/js/hello_world.html)
![](examples/js/hello_world.js)


## Exercise: Add two numbers
{id: exercise-add-two-numbers}


Create a web form that has two input fields and a button. The user can type js
two numbers and when she clicks on a button, the page will show the sum of the numbers.





## Solution: Add two numbers
{id: solution-add-two-numbers}
![](examples/js/add_numbers.html)
![](examples/js/add_numbers.js)


## Variable definition
{id: variable-definition}
![](examples/js/var_definition.js)




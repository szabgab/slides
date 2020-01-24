# JavaScript
{id: javascript}

## JS Bin
{id: jsbin}


[jsbin](http://jsbin.com/)


## Node.js
{id: nodejs}


Download [Node.js](http://nodejs.org/).
Run as `node`. Ctrl-C (twice) to quit.


On Ubuntu I had to install the `nodejs` package and the command is called
`nodejs` as there was already command called node.

On Mac first install [Homebrew](http://mxcl.github.io/homebrew/) and then `brew install node`.

{aside}
Maybe you'll need to use the Git bash shell...
{/aside}

```
> .help
> .exit

> .break
```

Some JavaScript using the Node.js REPL


Variables and numbers


```
> a = 23
23
> b = 19
19
> a+b
42
```

The behaviour of + depends on the operands. If even one of them is a sting,
+ will concatenate them as string. Use parseInt() to convert a string to an integer.


```
> c = "1"
> a+c
'231'
> a+parseInt(c)
24
```


## String to float conversion
{id: string-to-float-conversion}
{i: parseFloat}

use parseFloat


```
> c = "1.2"
> a+c
'231.2'
> a+parseInt(c)
24
> a+parseFloat(c)
24.2
```


Number(v) is like parseFloat.
Except that Number('4x') returns NaN
and parseInt('4x') and parseFloat('4x') both return 4.




## Number to string conversion
{id: number-to-string-conversion}
{i: toString}

What if you have a number but would like to use it as a sting?


```
> 1+2
3
> 1+String(2)
12
> a = 1
> b = 2
> a + b
3
> b.toString()
> a + b
'12'
```


## Hello World
{id: javascript-hello-world}
![](examples/javascript/hello_world.js)

To run, type **node example/javascript/hello_world.js**



## Comments
{id: javascript-comments}
![](examples/javascript/comments.js)


## Variable
{id: javascript-variable}
{i: var}
![](examples/javascript/hello_world_var.js)


## JavaScript strings
{id: javascript-strings}
![](examples/javascript/strings.js)


## Boolean values
{id: javascript-boolean}

```
true
false
Boolean( 2 > 3 )

These are false:
false, null, undefined
"" (the empty string)
0, NaN
```


## Global Scope
{id: global-scope}

![](examples/javascript/global_scope.js)

Having `var` in the body of the code, in the global scope does not matter.
It is the same variable all over, but having it inside a function will restrict
the scope of that variable.

![](examples/javascript/global_scope_var.js)


## Local Scope
{id: local-scope}

![](examples/javascript/local_scope_var.js)
![](examples/javascript/local_scope_var_var.js)


## Objects
{id: javascrip-objects}

![](examples/javascript/objects.js)


## Objects - more
{id: javascrip-objects-more}

![](examples/javascript/objects_more.js)


## Objects - deep
{id: javascrip-objects-deep}

![](examples/javascript/objects_deep.js)


## Arrays
{id: javascrip-array}

![](examples/javascript/array.js)


## Javascript Core types
{id: javascript-core-types}

* Numbers
* Strings
* Booleans
* null
* undefined
* Objects




## Type of variable
{id: typeof}
![](examples/javascript/typeof.js)


## Functions
{id: javascript-function}
![](examples/javascript/function.js)


## Function in var
{id: javascript-function-in-var}
![](examples/javascript/function_in_var.js)


## Function in object
{id: javascript-function-in-object}
![](examples/javascript/function_in_object.js)


## random
{id: javascript-random}


Math.random() returns a floating point number between 0 and 1.
parseInt(Math.random()*6+1) is throwing a dice.




## while
{id: javascript-while}
![](examples/javascript/while.js)


## if else if
{id: javascript-if-else-if}
![](examples/javascript/if_else_if.js)





# Introduction to JavaScript
{id: intro}

## History of JavaScript
{id: history-javascript}

* Brendan Eich developed at Netscape - it was called Mocha
* 1995 - Released as LiveScript
* 1995 - Renamed to JavaScript (to ride on the popularity of Java)
* 1996 - Microsoft JScript
* 1997 - First edition of ECMAScript standard (European Computer Manufacturers Association)
* 1998 - Second edition
* 1999 - Third edition
* 4th edition never completed
* 2009 - 5th edition
* 2011 - 5.1 edition   (part of "HTML5")
* 2015 - 6th edition (ECMAScript6 or ECMAScript 2015)



## About JavaScript
{id: about-javascript}

* In browser + DOM (Document Object Model)
* On server (Node.js)
* Embedded in other applications



## JavaScript editors, IDEs
{id: editors-ide}

IDE - Integrated Development Environment


* Aptana Studio
* WebStorm
* Atom + Ternjs (atom-ternjs) (for JavaScript intelligence) + script (to be able to run code from editor)



* Notepad++



## alert
{id: alert}
{i: alert}
{i: script}
{i: ;}

{aside}

Probably the simplest way to see some action from JavaScript is to embed an **alert()** call
in an html file.
{/aside}
![](examples/js/alert.html)

* Not really used any more
* always put ; at the end of statements



## Document.write
{id: document-write}
{i: document.write}
![](examples/js/document_write.html)

* script - javascript
* document.write
* document is the object representing the HTML document. The DOM



## confirm
{id: confirm}
{i: confirm}
![](examples/js/confirm.html)


## prompt
{id: prompt}
{i: prompt}
![](examples/js/prompt.html)


## console
{id: console}
{i: console.log}

{aside}

The better way to see messages from the JavaScript running in the browser is to use the **console.log()**
function and open the console.
{/aside}
![](examples/js/console_script.html)

To open the JavaScript console


* Chrome Mac: Command-Option-J
* Chrome Windows: Ctrl-Shift-J
* Firefox Mac:  Command-Option-K
* Firefox Windows: Ctrl-Shift-K
* Internet Explorer: F12
* Safari: Command-Option-C


Run it with Node.JS


Run it in the editor



## Separate script to its own file
{id: console-separate}
![](examples/js/console.html)
![](examples/js/console.js)

```
$ node examples/js/console.js
```


## Comments in JavaScript
{id: comments}
{i: /*}
{i: //}
![](examples/js/comments.js)

* To explain to the next developer why do we do something.
* Explain algorithm.
* Temporarily disable code for debugging.



## Bad Comments in JavaScript
{id: bad-comments}


  It is better to avoid the multiline comments /*  */
  Especially as most editors support the commenting out of a whole
  section of lines with just one keystroke.


![](examples/js/bad_comments.js)

```
  SyntaxError: unterminated string literal
```

```
.../examples/js/bad_comments.js:8
   console.log("/* hello */")
                           ^^
SyntaxError: Unexpected token ILLEGAL
    at exports.runInThisContext (vm.js:73:16)
    at Module._compile (module.js:443:25)
    at Object.Module._extensions..js (module.js:478:10)
    at Module.load (module.js:355:32)
    at Function.Module._load (module.js:310:12)
    at Function.Module.runMain (module.js:501:10)
    at startup (node.js:129:16)
    at node.js:814:3
```



## Literal values in JavaScript (numbers, strings, booleans, etc.)
{id: literal-values-in-javascript}

* Numbers (42,  2.3, NaN,  Infinity, -Infinity)
* Strings ("", '')
* Booleans (true, false)
* null
* undefined
* Objects (incl. Arrays, Functions)

![](examples/js/literal_values.js)

* Numbers in JavaScript is 64-bit floating point (double)
* Regular arithmetic issues 0.1+0.2 is not exactly 0.3



## Examples for generating Infinite and NaN (not a number)
{id: nan-and-infinite}
{i: NaN}
{i: Infinite}
![](examples/js/nan.js)


## var - variables in JavaScript
{id: var}
{i: use strict}
{i: var}
![](examples/js/var.js)

* "use strict"; (later explained)
* Declare variables using 'var'
* Variable names start with letters, underscore (_), or the dollar sign.
* Variable names can contain letters, underscore (_), the dollar sign, and digits.
* camelCase is the recommended style in JavaScript, though I think long_names separated with underscores are nicer.



## Variables without var
{id: no-var}

* Works, variable are global here too.
* What if we make a typo in one of the variable names? No one might notice, but the code will misbehave.

![](examples/js/no_var.js)


## use strict
{id: use-strict}
{i: use strict}
![](examples/js/no_var_strict.js)
![](examples/js/no_var_strict.txt)


## use strict + var
{id: use-strict-var}
![](examples/js/var_strict.js)
![](examples/js/var_strict.txt)


## Exercise: Set up environment for web browser
{id: exercise-web-environment}

* Install either Chrome or Firefox if you don't have them yet.
* Using Notepad or any other text editor create and .html file that will show and 'alert' and try it in your browser.
* (Suggestion: Start by creating a directory in c:\ in Windows or in ~/ on Unix/Linux and put your files in that directory)



## Exercise: Set up environment for command line
{id: exercise-node-environment}

* Install [Node.js](https://nodejs.org/)
* Using Notepad or any other text editor (re-)create the console.js file and run it on the command line using node.
* (On Windows you need to open Start/Run: cmd)



## Exercise: Set up development environment
{id: exercise-editor-environment}


If you prefer to use another Editor/IDE, that's ok. Then insted of these steps,
make sure you have similar capabilities there.



* Install [Atom](https://atom.io/)
* Open the directory where you've already saved the .html and .js files earlier using  **File/Open Project Folder**
* Install the Ternjs (atom-ternjs) package for JavaScript intelligence and check if it works properly. (In your .js file type in a string followed by a .)
* Install the 'script' package to be able to run code from editor. Try to run the .js file.



## Exercise: Hello World
{id: exercise-hello}

* Using the new Editor/IDE - open the console.js and run it from the editor
* Create the console.html file too and open it with a browser
* Create a hello.html that loads hello.js that ask the user for her name and then displays the result in the browser and on the console as well.




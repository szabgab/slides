# Second steps
{id: second-steps}

## Modules
{id: modules-first-time}

{aside}
When we program in Python we basically have 3 main pieces. The base-language itself. A set of standard modules. A set of 3rd party modules.

All the modules provide additional functionality to the base-language and without them we would not be able to do much. The standard modules
come installed with Python, the 3rd party modules we need to install. Once installed however they behave in the same way. We need to `import`
them and then we can use them. We'll discuss these even more later, but we already would like to use some so let's see some basic ideas.

I know we already used the `math` module in the solution of the earlier exercises, but some people might have missed those.

In this example we `import` the `sys` module that contains various attributes and operations related to the Python system. (There is another module
called `os` that provides functionality related to the Operating System.)

A few examples:

The `executable` attribute pointing to where the currently running Python executable is located. On MS Windows this will be a path to a python.exe file.

`platform` is going to be `win32` on any Windows machine.

We are going to discuss the whole `sys.argv` thing a lot more, but for now look `sys.argv[0]` contains path to the current Python file.

`sys.version_info` contains the version information about the currently running Python.
Specifically `sys.version_info.major` contains the major version number which 3 for Python 3 and 2 for Python 2.
If really needed, you could use this to recognize when someone is trying to run your program on an unsupported version of Python.

These were all attributes that contain some fixed value.

There is also the `getsizeof` function that comes with the `sys` module. You know it is a function because you see a pair of parentheses
at the end. The attributes above did not have parentheses. Functions do something. This specific function calculates the number of bytes
being used by an object.

You can see an integer (both 1 and 42) use 28 bytes.

A floating point number uses 24 bytes.

An empty string uses 49 bytes.

Then each character takes another byte. (Actually this is only true in the case of Latin letters, but let's not get ahead of ourselves.)
{/aside}

* The documentation of the [sys](https://docs.python.org/library/sys.html) module.

![](examples/basics/modules.py)

## A main function
{id: python-optional-main-sub}
{i: main}
{i: def}

{aside}
You could write your code in the main body of your Python file, but using functions
and passing arguments to it will make your code easier to maintain and understand.
Therefore I recommend that you always write every script with a function called "main".

* Function definition starts with the **def** keyword, followed by the name of the new function ("main" in this case), followed by the list of **parameters in parentheses** (nothing in this case).
* The content or body of the function is then **indented** to the right.
* The function definition ends when the indentation stops.

If you execute this file you might be surprised that nothing happens. This is so because we only **defined** the function, we never used it. We'll do that next.
{/aside}

![](examples/basics/hello_world_main.py)

This won't run as the main function is declared, but it is never called (invoked).

## The main function - called
{id: python-optional-main-sub-called}
{i: main}
{i: def}

{aside}
In this example I added 3 lines to the previous file. The line `main()` calls the main function. We sometimes also say "runs the function" or "invokes the function".
In this context they mean the same.

The two print-statements are not necessary to call the function, I only added them so it will be easy to see the order of the operations that you can observe
by looking at the output.
{/aside}

![](examples/basics/hello_world.py)

```
before
Hello
World
after
```

{aside}
* Use a main function to avoid globals and better structure your code.
* Python uses **indentation** for blocks instead of curly braces, and it uses the colon **:** to start a block.
{/aside}


## Indentation
{id: indentation}
{i: indentation}

* Standard recommendations: 4 spaces on every level.

## Conditional main
{id: conditional-main}
{i: __main__}
{i: __name__}

![](examples/basics/conditional_main.py)

* We'll cover this later but in case you'd like, you can include this conditional execution of the main function.


## Input - Output I/O
{id: input-output}

Input

* Keyboard (Standard Input, Command line, GUI)
* Mouse (Touch pad)
* Touch screen
* Files, Filesystem
* Network  (e.g. in Web applications)

Output

* Screen
* File
* Network


## print in Python 2
{id: print-in-python2}

{aside}
print is one of the keywords that changed between Python 2 and Python 3. In Python 2 it does not need parentheses, in Python 3 it is a function and it needs to have parentheses.
{/aside}

![](examples/basics/print.py)

```
hello
world
Foo Bar
```
![](examples/basics/print_no_newline.py)

```
hello world
Foo Bar
```

No newline, but a space is added at the end of the output and between values.

![](examples/basics/write.py)

```
helloworld
```

write takes exactly one parameter


## print in Python 3
{id: print-in-python3}
{i: print}
{i: end}
{i: sep}

![](examples/basics/print3.py)

```
hello
world
Foo Bar
```
![](examples/basics/print3_no_newline.py)

![](examples/basics/print3_no_newline.out)


end will set the character added at the end of each print statement.

![](examples/basics/print3_no_newline_no_space.py)

![](examples/basics/print3_no_newline_no_space.out)


`sep` will set the character separating values.


## print in Python 2 as if it was Python 3
{id: print-in-python2-as-in-python3}
{i: __future__}
{i: print_function}

![](examples/basics/print3_in2.py)

```
helloworld
```


## Exception: SyntaxError: Missing parentheses in call
{id: syntax-error-missing-parentheses-in-call}

What if we run some code with **print "hello"** using Python 3?

![](examples/basics/print.err)


## Prompting for user input in Python 2
{id: python-prompting-for-user-input}
{i: raw_input}
{i: prompt}
{i: STDIN}

![](examples/basics/prompt2.py)

```
/usr/bin/python2 prompt2.py

We have a question!
Your name: Foo Bar
Hello Foo Bar , how are you?
Hello Foo Bar, how are you?
```

What happens if you run this with Python 3 ?


```
/usr/bin/python3 prompt2.py
```

![](examples/basics/prompt2.err)


## Prompting for user input in Python 3
{id: python3-prompting-for-user-input}
{i: input}
{i: prompt}
{i: STDIN}

{aside}
In Python 3 the **raw_input()** function was replaced by the **input()** function.
{/aside}

![](examples/basics/prompt3.py)

What happens if you run this using Python 2 ?

```
/usr/bin/python2 prompt3.py
```

* What happens if we type in "Foo Bar"

![](examples/basics/prompt3_1.err)

* What happens if we type in just "Foo" - no spaces:

![](examples/basics/prompt3_2.err)

* The next example shows a way to exploit the `input` function in Python 2 to delete the currently running script. You know, just for fun.

![](examples/basics/prompt3_3.err)


## Python2 input or raw_input?
{id: python-prompt-python-2-and-3}

In Python 2 always use `raw_input()` and never `input()`.


## Prompting both Python 2 and Python 3
{id: python-prompt-both-python-2-and-3}
{i: raw_input}
{i: input}

![](examples/basics/prompt.py)


## Add numbers entered by the user (oups)
{id: python-add-strings}
{i: +}

![](examples/basics/add.py)

```
First number: 2
Second number: 3
23
```

When reading from the command line using `input()`, the resulting value is a string.
Even if you only typed in digits. Therefore the addition operator `+` concatenates the strings.


## Add numbers entered by the user (fixed)
{id: python-add-numbers}

![](examples/basics/add_numbers_input.py)

```
First number: 2
Second number: 3
5
```

In order to convert the string to numbers use the `int()` or the `float()` functions.
Whichever is appropriate in your situation.


## How can I check if a string can be converted to a number?
{id: is-it-a-number}
{i: isdecimal}
{i: isnumeric}

* This solution only works for integers. Not for floating point numbers.

* We'll talk about this later. For now assume that the user enters something that can be converted to a number.
* Wrap the code in try-except block to catch any exception raised during the conversion.
* Use Regular Expressions (regexes) to verify that the input string looks like a number.
* [Unicode Characters in the 'Number, Decimal Digit' Category](https://www.fileformat.info/info/unicode/category/Nd/list.htm)

* [isdecimal](https://docs.python.org/library/stdtypes.html#str.isdecimal) Decimal numbers (digits) (not floating point)
* [isnumeric](https://docs.python.org/library/stdtypes.html#str.isnumeric) Numeric character in the Unicode set (but not floating point number)
* In your spare time you might want to check out the standard types of Python at [stdtypes](https://docs.python.org/library/stdtypes.html).

![](examples/basics/isnumber.py)

![](examples/basics/isnumber.out)

![](examples/basics/isnumber2.out)

![](examples/basics/isnumber_other.py)

## Converting string to int
{id: converting-to-int}
{i: int}

![](examples/basics/converting_to_int.py)
![](examples/basics/converting_string_to_int.py)


## Converting float to int
{id: converting-float-to-int}

![](examples/basics/converting_float_to_int.py)
![](examples/basics/converting_floating_string_to_int.py)
![](examples/basics/converting_to_int_via_float.py)

## How can I check if a string can be converted to a number?
{id: is-number}
{i: int}
{i: float}
{i: is_int}
{i: is_float}


There is no is_int, we just need to try to convert and catch the exception, if there is one.


![](examples/basics/is_number.py)


## Conditionals: if
{id: python-conditionals-if}
{i: if}

![](examples/basics/if.py)


## Conditionals: if - else
{id: python-conditionals-if-else}
{i: if}
{i: else}

![](examples/basics/if_else.py)

## Divide by 0
{id: python-divide-by-0}
{i: ZeroDivisionError}

* Another use-case for if and else:

![](examples/basics/divide_by_zero.py)

![](examples/basics/divide_by_zero.err)

## Conditionals: if - else (other example)
{id: python-conditionals-if-else-divide}
{i: if}
{i: else}

![](examples/basics/if_else_divide.py)


## Conditionals: else if
{id: python-conditionals-else-if}
{i: else if}

![](examples/basics/else-if.py)


## Conditionals: elif
{id: python-conditionals-elif}
{i: elif}
{i: else if}

![](examples/basics/elif.py)

## Ternary operator (Conditional Operator)
{id: ternary-operator}
{i: ?:}

![](examples/basics/ternary.py)
![](examples/basics/without_ternary.py)

In other languages this is the [?:](https://en.wikipedia.org/wiki/%3F:) construct.

## Case or Switch in Python
{id: case-switch}
{i: case}
{i: switch}

* There is no case or switch statement in Python.


## Exercise: Rectangle
{id: exercise-rectangle}

* Write a script called **basic2_rectangle_input.py** that will ask for the sides of a rectangle and print out the area.
* Provide error messages if either of the sides is negative.


```
python rect.py
Side: 3
Side: 4
The area is 12
```


## Exercise: Calculator
{id: exercise-calculator}

Create a script called **basic2_calculator_input.py** that accepts 2 numbers and an operator `(+, -, *, /)`, and prints the result of the operation.

```
python calc.py
Operand: 19
Operand: 23
Operator: +
Results: 42
```

## Exercise: Age limit
{id: exercise-age-limit}

* Create a script called **basic2_age_limit_input.py**

* Ask the user what is their age.
* If it is above 18, tell them they can legally drink alcohol.
* If is is above 21, tell them they can also legally drink in the USA.

* Extra:
* Create a separate file **basic2_age_limit_all_input.py**
* Ask the user for an age and a country name tell them if they can legally drink alcohol.
* See the [Legal drinking age](https://en.wikipedia.org/wiki/Legal_drinking_age) list.
* Don't worry if this seems to be too difficult now to solve it in a nice way.


## Exercise: What is this language?
{id: exercise-what-is-this-language}

* Create a script called **basic2_language.py**

* Ask the user the name of this programing language.
* If they type in Python, welcome them.
* If they type in something else, correct them.

## Exercise: Standard Input
{id: exercise-stdin}

* In the previous exercises we expected the user-input to come in on the "Standard Input" aka. STDIN.
* If you would like to practice this more, come up with other ideas, try to solve them and tell me about the task. (in person or via e-mail.)
* (e.g. you could start building an interactive role-playing game.)

* Name the file **basic2_stdin.py**


## Solution: Area of rectangle
{id: solution-rectangle}

![](examples/basics/rectangle.py)


* For historical reasons we also have the solution in Python 2

![](examples/basics/rectangle_python2.py)


## Solution: Calculator
{id: solution-calculator}

{aside}
Here I used the `format` method of the strings to insert the value of op in the `{}` placeholder. We'll learn about this later on.
{/aside}

![](examples/basics/calculator.py)

* For historical reasons we also have the solution in Python 2

![](examples/basics/calculator_python2.py)

## Solution: Calculator eval
{id: solution-calculator-eval}

![](examples/basics/calculator_eval.py)

```
$ python examples/basics/calculator_eval.py

Number: 2
Number: 3
Operator (+-*/): +
2+3
5
```

Try Again, this time:

```
$ python examples/basics/calculator_eval.py

Number: os.system("ls -l")
Number:
Operator (+-*/):
```

And then you could try it with `rm -rf /` or if you are on Windows try `os.system("dir")`
or this: `os.system("rm -f calculator_eval.py")` and on windows it would be `os.system("del calculator_eval.py")`.


* Now forget this and don't use `eval` for the next few years!

## Solution: Age limit
{id: solution-age-limit}

![](examples/basics/age_limit.py)


## Solution: What is this language?
{id: solution-what-is-this-language}

![](examples/basics/check_python.py)

## STDIN vs Command line arguments
{id: example-using-command-line-arguments}

{aside}
If we run this script without any command-line parameters it will print out usage information.

If we give it two parameters it will treat the first one as the name of an input file and the second as the name of an output file.
{/aside}

* First try this; Then repeate. We must type in the same path again and again. Boring and error-prone.

![](examples/basics/convert_stdin.py)

* We could use a Tk-based dialog:
* Still boring (though maybe less error-prone)

![](examples/basics/convert_with_tk_dialog.py)

* The command line has
* History!

![](examples/basics/convert_argv.py)

## Command line arguments
{id: command-line-arguments}
{i: sys}
{i: argv}

![](examples/basics/cli.py)

```
$ python examples/basic/cli.py one two
```
![](examples/basics/cli.py.out)

```
$ python examples/basic/cli.py
```
![](examples/basics/cli.py.err)


## Command line arguments - len
{id: command-line-arguments-len}
{i: len}

![](examples/basics/cli_len.py)


## Command line arguments - exit
{id: command-line-arguments-exit}
{i: exit}
{i: !=}

![](examples/basics/cli_exit.py)

```
echo %errorlevel%
echo $?
```


## Exercise: Rectangle (argv)
{id: exercise-rectangle-argv}

* Create a script called **basic2_rectangle_argv.py**
* Change the above script that it will accept the arguments on the command line like this: `python basic2_rectangle_argv.py 2 4`


## Exercise: Calculator (argv)
{id: exercise-calculator-argv}


* Create a script called **basic2_calculator_argv.py**  that accepts 2 numbers and an operator `(+, -, *, /)`, on the command line and prints the result of the operation.
* `python basic2_calculator_argv.py 2 + 3`
* `python basic2_calculator_argv.py 6 / 2`
* `python basic2_calculator_argv.py 6 * 2`


## Solution: Area of rectangle (argv)
{id: solution-rectangle-argv}

![](examples/basics/rectangle_argv.py)

## Solution: Calculator (argv)
{id: solution-calculator-argv}

![](examples/basics/calculator_argv.py)

{aside}
The multiplication probably won't work because the Unix/Linux shell replaces the * by the list of files in your current directory and thus the python script will see a list of files instead of the `*`.
This is not your fault as a programmer. It is a user error. The correct way to run the script is `python calc.py 2 '*' 3`.
{/aside}


## Solution: Calculator eval
{id: solution-calculator-eval-x}

![](examples/basics/calculator_argv_eval.py)

```
$ python examples/basics/calculator_argv_eval.py 2 + 3
5

$ python examples/basics/calculator_argv_eval.py 2 '*' 3
6
```

* Now forget this and don't use `eval` for the next few years!


## Compilation vs. Interpretation
{id: compilation-vs-interpretation}

**Compiled**

* Languages: C, C++
* Development cycle: Edit, Compile (link), Run.
* Strong syntax checking during compilation and linking.
* Result: Stand-alone executable code.
* Need to compile to each platform separately. (Windows, Linux, Mac, 32bit vs 64bit).

**Interpreted**

* Shell, BASIC
* Development cycle: Edit, Run.
* Syntax check only during run-time.
* Result: we distribute the source code.
* Needs the right version of the interpreted on every target machine.

**Both?**

* Java (running on JVM - Java Virtual Machine)
* C# (running on CLR - Common Language Runtime)


## Is Python compiled or interpreted?
{id: compilation}

There are syntax errors that will prevent your Python code from running

![](examples/basics/syntax_error.py)
![](examples/basics/syntax_error.py.out)

There are other syntax-like errors that will be only caught during execution

![](examples/basics/compile.py)
![](examples/basics/compile.py.out)


![](examples/basics/compile_with_global.py)
![](examples/basics/compile_with_global.out)

* Python code is first compiled to bytecode and then interpreted.
* CPython is both the compiler and the interpreter.
* Jython and IronPython are mostly just compiler to JVM and CLR respectively.


## Flake8 checking
{id: flake8-compile}

```
pip install flake8


flake8 --ignore= compile.py
```

![](examples/basics/compile_flake8.out)

If you used Anaconda you can install with:

```
conda install flake8
```


## Pylint checking
{id: pylint-checking}

```
pip install pylint
```

![](examples/basics/bad.py)

```
pylint bad.py
```

![](examples/basics/bad.out)


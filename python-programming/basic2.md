# Second steps
{id: second-steps}

## Modules
{id: modules-first-time}

![](examples/basics/modules.py)

## The main function
{id: python-optional-main-sub}
{i: main}
{i: def}

![](examples/basics/hello_world_main.py)

This won't run as the main function is declared, but it is never called (invoked).

## The main function - called
{id: python-optional-main-sub-called}
{i: main}
{i: def}


{aside}
You could write your code in the main body of your Python file, but using functions
and passing arguments to it will make your code easier to maintain and understand.
Therefore I recommend that you always write every script with a function called "main".

* Function definition starts with the **def** keyword, followed by the name of the new function ("main" in this case), followed by the list of **parameters in parentheses** (nothing in this case).
* The content or body of the function is then **indented** to the right.
* The function definintion ends when the indentation stops.
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

```
hello world
Foo Bar
```

end will set the character added at the end of each print statement.

![](examples/basics/print3_no_newline_no_space.py)

```
helloworld
FooBar
END
```

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

![](examples/basics/prompt3_1.err)
![](examples/basics/prompt3_2.err)


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

* [stdtypes](https://docs.python.org/library/stdtypes.html)

![](examples/basics/isnumber.py)
![](examples/basics/isnumber.out)

* We'll talk about this later. For now assume that the user enters something that can be converted to a number.
* Use Regular Expressions (regexes) to verify that the input string looks like a number.
* Wrap the code in try-except block to catch any exception raised during the conversion.

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


## Conditionals: if - else
{id: python-conditionals-if-else}
{i: else}
{i: if}

![](examples/basics/if.py)


## Conditionals: else if
{id: python-conditionals-else-if}
{i: else if}

![](examples/basics/else-if.py)


## Conditionals: elif
{id: python-conditionals-elif}
{i: elif}
{i: else if}

![](examples/basics/elif.py)

## Ternary operator
{id: ternary-operator}
{i: ?:}

![](examples/basics/ternary.py)

## Case or Switch in Python
{id: case-switch}
{i: case}
{i: switch}

* There is no case or switch statement in Python.


## Exercise: Rectangular
{id: exercise-rectangular}

* Write a script that will ask for the sides of a rectangular and print out the area.
* Provide error messages if either of the sides is negative.


```
python rect.py
Side: 3
Side: 4
The area is 12
```


## Exercise: Calculator
{id: exercise-calculator}

Create a script that accepts 2 numbers and an operator `(+, -, *, /)`, and prints the result of the operation.

```
python calc.py
Operand: 19
Operand: 23
Operator: +
Results: 42
```


## Exercise: Standard Input
{id: exercise-stdin}

* In the previous exercises we expected the userinput to come in on the "Standard Input" aka. STDIN.
* If you would like to practice this more, come up with other ideas, try to solve them and tell me about the task. (in person or via e-mail.)
* (e.g. you could start building an interactive role-playing game.)



## Solution: Area of rectangular
{id: solution-rectangular}

![](examples/basics/rectangular.py)


Same in Python 2

![](examples/basics/rectangular_python2.py)


## Solution: Calculator
{id: solution-calculator}
![](examples/basics/calculator.py)

Same in Python 2

![](examples/basics/calculator_python2.py)


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



## Exercise: Rectangular (argv)
{id: exercise-rectangular-argv}

* Change the above script that it will accept the arguments on the command line like this: **python rect.py 2 4**



## Exercise: Calculator (argv)
{id: exercise-calculator-argv}

* Create a script that accepts 2 numbers and an operator `(+, -, *, /)`, on the command line and prints the result of the operation.
* `python calc.py 2 + 3`
* `python calc.py 6 / 2`
* `python calc.py 6 * 2`


## Solution: Area of rectangular (argv)
{id: solution-rectangular-argv}

![](examples/basics/rectangular_argv.py)


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


## Solution: Calculator (argv)
{id: solution-calculator-argv}

![](examples/basics/calculator_argv.py)

The multiplication probably won't work because the Unix/Linux shell replaces the * by the list of files in your current directory and thus the python script will see a list of files instead of the `*`.
This is not your fault as a programmer. It is a user error. The correct way to run the script is `python calc.py 2 '*' 3`.


## Compilation vs. Interpretation
{id: compilation-vs-interpretation}

**Compiled**

* Languages: C, C++
* Development cylce: Edit, Compile (link), Run.
* Strong syntax checking during compilation and linking.
* Result: Stand-alone executable code.
* Need to compile to each platform separately. (Windows, Linux, Mac, 32bit vs 64bit).

**Interpreted**

* Shell, BASIC
* Development cycle: Edit, Run.
* Syntaxt check only during run-time.
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

* Python code is first compiled to bytecode and then interpreted.
* CPython is both the compiler and the interpreter.
* Jython and IronPython are mostly just compiler to JVM and CLR respectively.


## Flake8 checking
{id: flake8-compile}

```
conda install flake8
pip install flake8

flake8 --ignore= compile.py
```
![](examples/basics/compile_flake8.out)


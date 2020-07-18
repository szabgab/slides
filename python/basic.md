# First steps
{id: first-steps}

## What is Python?
{id: what-is-python}

* A snake.
* A British comedy group called [Monty Python](https://en.wikipedia.org/wiki/Monty_Python).
* A programming languge. The definition of the language: words, punctuation (operators) and grammar (syntax).
* The compiler/interpreter of the Python programming language. (aka. CPython).

{aside}
When people say they Python in relation to programming they either mean the Python programming language or they
mean the tool that can translate some text (code) written in the Python programming language to the language a computer
can actually understand. On MS Windows this is the **python.exe** you need to install. On Linux/Mac it is usally called **python**
or **python3**. The generic name of the tool that translates a programming language for the computer is eiter
called a compiler or an interpreter. We'll talk about this later on.
{/aside}

## What is needed to write a program?
{id: what-is-needed-to-write-a-program}

* An **editor** where we can write in a language.
* A **compiler or interpreter** that can translate our text to the language of the computer.

{aside}
In order to write and run a program you basically need two things. A text editor in which you can write the program
and a compiler or interpreter that can translate this program to the computer.
{/aside}

## The source (code) of Python
{id: the-source-of-python}

* [Python](https://www.python.org/)


## Python 2 vs. Python 3
{id: python-2-vs-3}

* Python 2.x - old, legacy code at companies, answers on the Internet. Retires on January 1, 2020.
* Python 3.x - the one that you should use. (not fully backward compatible) Available since December 3, 2008.

{aside}
Python has two major lines the version 2.x and the version 3.x. In a nutshell you **should** always use Python 3 if possible.

Unfortunately you can still encounter many companies and many projects in companies that are stuck on Python 2.
In such cases you probably will have to write in Python 2.

In addition when you search for solutions on the Internet in many cases you'll encounter solution that were written
for Python 2. Luckily in most of the cases it is almost trivial to convert thise small examples to work on Python 3.
You just need to be able to recognize that the code was originally written for Python 2 and you need to be able to make
the adjustments.

For this reason, while the majority of these pages cover Python 3, we are going to point out the places where it
might be useful to know how Python 2 works.

You are free to skip these parts and come back to them when the need arises.
{/aside}

## Installation
{id: installation}

* MS Windows
* Linux
* Apple/Mac OSX

{aside}
We are going to cover how to install Python all 3 major operating systems.
{/aside}

## Installation on Linux
{id: installation-linux}

* On Linux you usually have Python 2 installed in **/usr/bin/python**
* Python 3 in **/usr/bin/python3**.
* If they are not installed, you can install them with the appropriate **yum** or **apt-get** command of your distribution.
* An alternative is to install [Anaconda with Python 3.x](https://www.anaconda.com/download/)


```
$ which python3

$ sudo apt-get install python3
$ sudo yum install python3
```



## Installation on Apple Mac OSX
{id: installation-osx}

* On Mac OSX you can have Python 2 installed in **/usr/bin/python** and Python 3 installed as **/usr/bin/python3**.
* [Homebrew](https://brew.sh/)
* An alternative is to install [Anaconda with Python 3.x](https://www.anaconda.com/download/)


```
$ which python3

$ brew install python3
```


## Installation on MS Windows
{id: installation-windows}

* [Anaconda with Python 3.x](https://www.anaconda.com/download/)
* Anaconda shell
* Anaconda Jupyter notebook
* 
* An alternative is to [install from here](http://www.python.org/download/).



## Editors, IDEs
{id: python-editors}

{aside}

Basically you can use any text editor to write Python code. The minimum I recommend is to have proper syntax highlighting. IDEs will also provide intellisense, that is,
in most of the cases they will be able to understand what kind of objects do you have in your code and will be able to show you the available methods and their
parameters. Even better, they provide powerful debuggers.
{/aside}


{aside}
PyCharm seems to be the most popular IDE. It has a free version called community edition.
{/aside}

Linux


* [Emacs](http://www.gnu.org/software/emacs/)
* [vi, vim, gvim](http://www.vim.org/)
* [spf13-vim](http://vim.spf13.com/)
* [Kate](http://kate-editor.org/)
* [Gedit](http://projects.gnome.org/gedit/)
* [jEdit](http://www.jedit.org/)

Windows

* [Notepad++](http://notepad-plus-plus.org/)
* [Textpad](http://www.textpad.com/)
* [Ultra Edit](http://www.ultraedit.com/)

Mac

* [CotEditor](https://coteditor.com/)
* [TextWrangler](http://www.barebones.com/products/textwrangler/)
* [TextMate](http://macromates.com/)
* Type "text editor" in your Apple Store (filter to free)

All platforms

* [Sublime Text](http://www.sublimetext.com/) (commercial)
* [Ligth Table](http://www.lighttable.com/)

IDEs

* [PyCharm community edition](http://www.jetbrains.com/pycharm/)
* [Visual Code of Microsoft](https://code.visualstudio.com/)

* [Spyder](https://www.spyder-ide.org/), a scientific environment (included in Anaconda)
* [Jupyter](https://jupyter.org/) with [IPython](http://ipython.org/) behind the scene.

* [IDLE](https://en.wikipedia.org/wiki/IDLE) (comes with Python)
* [Komodo of ActiveState](http://www.activestate.com/)
* [Aptana](http://www.aptana.com/)
* [Pyscripter](http://code.google.com/p/pyscripter/)
* [PyDev (for Eclipse)](http://pydev.org/)
* [Wing IDE](http://www.wingware.com/)
* [Atom](https://atom.io/)



## Documentation
{id: documentation}

* [Google](https://www.google.com/)
* [Bing](https://www.bing.com/)
* [DuckDuckGo](https://duckduckgo.com/)
* [official documentation of Python](https://docs.python.org/)
* [Stack Overflow](https://stackoverflow.com/)
* [Code Maven](https://code-maven.com/python)
* ...



## Program types
{id: program-types}

* Desktop application (MS Word, MS Excel, calculator, Firefox, Chrome, ...
* Mobile applications - whatever runs on your phone.
* Embedded applications - software in your car or in your shoelace.
* Web applications - they run on the web server and send you HTML that your browser can show.
* **Command Line Applications**
* Scripts and programs are the same for our purposes
* ...




## Python on the command line
{id: python-on-the-command-line}
{i: -V|options}
{i: -c|options}

More or less the only thing I do on the command line with python is to check the version number:


```
python -V
python --version
```


You can run some Python code without creating a file, but I don't rememeber ever needing this. If you insists


```
python -c "print 42"
```

```
python3 -c "print(42)"
```

Type the following to get the details:


```
man python
```

[cmdline](https://docs.python.org/using/cmdline.html)




## First script - hello world
{id: first-script}
![](examples/basics/hello.py)

* Create a file called **hello.py** with the above content.
* Open your terminal or the Anaconda Prompt on MS Windows in the directory (folder)
* Change to the directory  where you saved the file.
* Run it by typing **python hello.py** or **python3 hello.py**
* The extension is .py - mostly for the editor (but also for modules).
* Parentheses after print() are required in Python 3, but use them even if you are stuck on Python 2.



## Examples
{id: download-the-examples}

* [The examples are on GitHub](https://github.com/szabgab/slides)
* You can download them and unzip them.



## Comments
{id: comments}
{i: #}

{aside}

# marks single line comments.
There are no real multi-line comments in Python, but we will see a way to have them anyway.
{/aside}
![](examples/basics/comments.py)



## Variables
{id: variables}
![](examples/basics/hello_variable.py)


## Exercise: Hello world
{id: exercise-hello-world}


Try your environment:



* Make sure you have access to the right version of Python.
* Install Python if needed.
* Check if you have a good editor with syntax highlighting.
* Write a simple script that prints **Hello world.**
* Add some comments to your code.
* Create a variable, assign some text to it and then print out the content of the variable.



## What is programming?
{id: what-is-programming}

* Use some language to tell the computer what to do.
* Like a cooking recepie it has step-by-step instructions.
* Taking a complex problem and dividing it into small steps a computer can do.



## What are the programming languages
{id: what-are-programming-languages}

* A computer CPU is created from transistors, 1 and 0 values. (aka. bits)
* Its language consists of numbers. (e.g 37 means move the content of ax register to bx register)
* English? too complex, too much ambiguity.
* Programming languages are in-beteen.



## A written human language
{id: human-language}

* Words
* Punctuation: - . , ! ?
* Grammar
* ...



## A programming language
{id: programming-language}

* Built-in words: print, len, type, def, ...
* [Literal values: numbers, strings](https://en.wikipedia.org/wiki/Literal_(computer_programming))
* [Operators: + - * = , ; ...](https://en.wikipedia.org/wiki/Operator_(computer_programming))
* [Grammar (syntax)](https://en.wikipedia.org/wiki/Syntax_(programming_languages))
* User-created words: variables, functions, classes, ...




## Words and punctuation matter!
{id: punctuation-matters}

* What did you chose? (Correctly: choose, but people will usually understand.)
* Lets do the homework. (Correctly: Let's, but most people will understand.)
* Let's eat, grandpa!
* Let's eat grandpa!
* [see more](https://thewritepractice.com/why-you-need-to-be-using-oxford-commas/)


* Programming languages have a lot less words, but they are very strict on the grammar (syntax).
* A mising comma can break your code.
* A missing space will change the meaning of your code.
* An incorreect word can ruin your day.



## Literals,  Value Types in Python
{id: value-types-in-python}
{i: int}
{i: str}
{i: float}
{i: bool}
![](examples/basics/show_types.py)
![](examples/basics/show_types.err)

* Strings must be enclosed in quotes.
* Numbers must be NOT enclosed in quotes.



## Floating point limitation
{id: floating-point-error}
![](examples/numbers/float_precision.py)

* [floating point](https://docs.python.org/3/tutorial/floatingpoint.html)




## Value Types in Numpy
{id: value-types}


Numpy but also other programming languages might have them.



* int8
* int32
* float32
* float64
* ...



## Rectangular (numerical operations)
{id: rectangular-basic}
![](examples/basics/rectangular_basic.py)



## Multiply string
{id: multiply-strings}
![](examples/basics/rectangular_strings.py)
![](examples/basics/rectangular_strings.err)


## Add numbers
{id: add-numbers}
![](examples/basics/add_numbers.py)


## Add strings
{id: add-strings}
![](examples/basics/add_strings.py)


## Exercise: Calculations
{id: exercise-calculations}

* Extend the rectangular_basic.py from above to print both the area and the circumference of the rectangle.
* Write a script that has a variable holding the radius of a circle and prints out the area of the circle and the circumference of the circle.
* Write a script that has two numbers a and b and prints out the results of a+b, a-b, a*b, a/b



## Solution: Calculations
{id: solution-calculations}
![](examples/basics/rectangular_solution.py)
![](examples/basics/circle_solution.py)
![](examples/basics/circle_math_solution.py)
![](examples/basics/calc_solution.py)





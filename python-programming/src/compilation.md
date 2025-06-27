# Is Python compiled or interpreted?


There are syntax errors that will prevent your Python code from running

{% embed include file="src/examples/basics/syntax_error.py" %}
{% embed include file="src/examples/basics/syntax_error.py.out" %}

There are other syntax-like errors that will be only caught during execution

{% embed include file="src/examples/basics/compile.py" %}
{% embed include file="src/examples/basics/compile.py.out" %}


{% embed include file="src/examples/basics/compile_with_global.py" %}
{% embed include file="src/examples/basics/compile_with_global.out" %}

* Python code is first compiled to bytecode and then interpreted.
* CPython is both the compiler and the interpreter.
* Jython and IronPython are mostly just compiler to JVM and CLR respectively.




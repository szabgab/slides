# Solution: Calculator (argv)

{% embed include file="src/examples/basics/calculator_argv.py" %}


The multiplication probably won't work because the Unix/Linux shell replaces the * by the list of files in your current directory and thus the python script will see a list of files instead of the `*`.
This is not your fault as a programmer. It is a user error. The correct way to run the script is `python calc.py 2 '*' 3`.



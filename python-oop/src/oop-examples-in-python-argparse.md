# OOP in Python (argparse)




There are more complex OOP usage cases that you have surely encountered already in Python. Either while programming or in my course. For example parsing the command line arguments
using argparse.

Here we call the ArgumentParser() method of the argparse object to create an instance of the `argparse.ArgumentParser` class. Then we call the `add_argument` method a few times and the `parse_args` method.
This returns an instance of the `argparse.Namespace` class.

So in fact you have already used OOP quite a lot while using various already existing classes and instances of those classes.

Now we are going to learn how can you create your own classes.


{% embed include file="src/examples/oop/examples_argparse.py" %}





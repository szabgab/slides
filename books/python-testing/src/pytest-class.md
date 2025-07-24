# PyTest: Fixture Class setup and teardown

* setup_class
* teardown_class
* setup_method
* teardown_method

In case you are using test classes then you can use another 2 pairs of functions, well actually methods, to setup and teardown the environment.
In this case it is much easier to pass values from the setup to the test functions and to the teardown function, but we need to write the whole thing in
OOP style.

Also note, the test functions are independent. They all see the atributes set in the `setup_class`, but the test functions cannot pass values to each other.

{% embed include file="src/examples/pytest/test_class.py" %}



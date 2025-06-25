# PyTest Fixture setup and teardown xUnit style


* setup_function
* teardown_function
* setup_module
* teardown_module

There are two mechanism in PyTest to setup and teardown fixtures. One of them is the xUnit-style system that is also available in other languages such as Java and C#.

In this example there are 3 tests, 3 functions that are called `test_SOMETHING`. There are also two pairs of functions to setup and teardown the fixtures on a per-function and per-module level.

Before starting to run the tests of this file PyTest will run the `setup_module` function, and after it is done running the tests PyTest will run the `teardonw_module` function. This will happen even if one or more of the tests failed.  These functions will be called once regradless of the number of tests we have in the module.

Before every test function PyTest will run the `setup_function` and after the test finisihed it will run the `teardown_function`. Regardless of the success or failure of the test.

So in our case where we have all 4 of the fixture functions implemented and we have 3 tests function the order can be seen on the next page.

In this example we also see one of the major issues of this style. The variable `db` that is set in the setup_module function must be marked as `global` in order to make it accessible in the test functions and in the `teardown_module` function.

{% embed include file="src/examples/pytest/test_fixture.py" %}

See next slide for the output.




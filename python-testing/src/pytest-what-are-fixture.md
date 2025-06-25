# PyTest: What are Fixtures?

* In generally we call [test fixture](https://en.wikipedia.org/wiki/Test_fixture) the environment in which a test is expected to run.
* Pytest uses the same word for a more generic concept. All the techniques that make it easy to set up the environment and to tear it down after the tests.

General examples:

* Setting up a database server - then removing it to clean the machine.
* Maybe filling the database server with some data - emptying the database.

Specific examples:

* If I'd like to test the login mechanism, I need that before the test starts running we'll have a verified account in the system.
* If I test the 3rd element in a pipeline I need the results of the 2nd pipeline to get started and after the test runs I need to remove all those files.



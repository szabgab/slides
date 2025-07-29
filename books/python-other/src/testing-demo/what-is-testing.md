# What is testing?

So what do we really mean when we mean testing?

For every piece of code wether its is a small module or a huge application you can have the following equasion.

There some environment the code works in. It might be just the interpreter/compiler in case of a single stand-alone function,
or it might include multiple networking elements, servers, databases, ioT deviecs etc. No matter what, the environment
is called by the testing people the "Fixture".

Then execute the code - the Application Under Test - and give it some input.

The result should be some "Expected Output".

So this is our equasion.


* Fixture + Input = Expected Output



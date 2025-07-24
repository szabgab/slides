# Hello Foo ARGV


* ARGV


Finally we could also expect the users to supply their name when they run the program.
For this we'll use the ARGV array that contains all the values that were passed to the program on the command line.

We'll take the first element of the array (that has index 0) and use that:


{% embed include file="src/examples/intro/hello_foo_argv.rb" %}

Run like this:

```
ruby examples/intro/hello_foo_argv.rb Bar
```

This is the output:

```
Hello Bar, how are you?
```




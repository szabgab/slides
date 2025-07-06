# Hello Foo using puts


* puts
* ,


It is not enough to print the name of the programmer, we would also want to greet the programmer.

We print the first part of the message, the variable, and the last part of the message in a single call to `puts`.
We need to separate these parts with a comma (`,`).


{% embed include file="src/examples/intro/hello_foo_puts.rb" %}


We got everything on the screen, but we are slightly disappointed as `puts` put each part of our message on a separate line. That's not really nice.


{% embed include file="src/examples/intro/hello_foo_puts.out" %}


In more technical terms, `puts` printed a `newline` after printing each one of its parameters.



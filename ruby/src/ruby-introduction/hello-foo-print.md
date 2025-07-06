# Hello Foo - print


* print


One way to improve the situation is to use the `print` function instead of the `puts` function to print to the screen.

That gave us a much nicer result as it did not print a newline after each item thereby moving the next one to the next line.
However, it also did not print a newline at the end of the whole print operation, which would have been also less convenient.
So in order to make it nicer we had to include `\n` at the end of our message to make it nicer.
`\n` represent a newline so when we include `\n` in whatever we print the next thing will be printed on the following line.


{% embed include file="src/examples/intro/hello_foo_print.rb" %}
{% embed include file="src/examples/intro/hello_foo_print.out" %}



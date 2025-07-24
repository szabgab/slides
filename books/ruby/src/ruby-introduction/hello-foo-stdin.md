# Hello Foo STDIN read


* STDIN
* gets



What if the person is not called Foo? What if we would like to ask the users of their name and greet them that way?
We can do this by reading from the keyboard which is, in technical terms called Standard Input or STDIN.

This is how we do it:


{% embed include file="src/examples/intro/hello_foo_stdin.rb" %}

Here is what happens when I run the program:

```
ruby examples/intro/hello_foo_stdin.rb
```

It prints:

```
Type in your name:
```

Then I type in `Bar` (another well known name in the programmer community) and press ENTER and this is the output I see:

```
Hello Bar
, how are you?
```


Why is it printed in two rows?

Because after we typed in Bar we pressed ENTER to tell the computer that we are done. However that ENTER generates a newline and that is included
in the text our program receives. So in the variable `person` we have a newline at the end and when we print it, the next thing will be shown
on a new line.



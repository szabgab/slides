# Introduction to Ruby
{id: introduction-to-ruby}

## Where to get Ruby
{id: where-to-get-ruby}

* [Ruby](https://www.ruby-lang.org/)



## Ruby on the command line
{id: ruby-on-the-command-line}

```
$ ruby -v
ruby 2.0.0p247 (2013-06-27 revision 41674) [universal.x86_64-darwin13]
```


{aside}

The -h flag will provide a list of all the command line options of Ruby.
{/aside}

```
$ ruby -h
...
```


{aside}

Mostly we are going to create files in Ruby, but it is good to know that you can also
create simple one-liners without creating a file.
{/aside}

```
$ ruby -e 'puts 19+23'
42
```


## irb - Interactive Ruby
{id: irb}

irb on Linux and Mac, fxri on Windows


{aside}

Before starting to write scripts, let's take a look at irb, the Interactive Ruby Shell.
A REPL (Read Evaluate Print Loop) that can help you explore the languages.
Just type **irb** on the command line and it will give you its own prompt.
There you can type in ruby statements.
{/aside}

```
$ irb
irb(main):001:0> 42
=> 42
irb(main):002:0> 'hello'
=> "hello"
irb(main):003:0> 19+23
=> 42
irb(main):004:0> puts 42
42
=> nil
irb(main):005:0> a = 19
=> 19
irb(main):006:0> b = 23
=> 23
irb(main):007:0> a+b
=> 42
irb(main):008:0> exit
$ 
```

{aside}

Simply typing in numerical or string expressions will print the result. Calling the **puts** ruby function will also print to the screen,
but then the REPL will print the "result" of puts, which is **nil**. We can assign values to variables, and then use them in other expressions.
Finally **exit** will let us leave the Interactive Ruby session.
{/aside}


## Hello world
{id: hello-world}
{i: "}
{i: '}
{i: puts}

{aside}

The required "Hello World!" example. Create the file called **hello.rb** with the following content. Then go to the command line, to the same directory
where you have the file **hello.rb** saved and type **ruby hello.rb**. It will print "Hello World!" to your screen.

What you can see here is that if you would like to have some text in your program you need to put them between quotes (") and you can use the `puts` function
to print something to the screen. Any text betwen quotes is called a "string".
{/aside}

![](examples/intro/hello.rb)

**ruby hello.rb**

{aside}
Just to clearify, unlike in some other programming languages, in Ruby you can use either double-quotes or single-quotes to mark the beginning and the end of a string,
but of course it has to be the same on both sides.
{/aside}

![](examples/intro/hello_single.rb)

## Ruby development environment
{id: ruby-development-environment}

{aside}
Any plain text editor will do, but there are also IDEs.
{/aside}

Linux


* vim
* emacs
* gedit


Windows


* NotePad++

## Create variable and print content using puts
{id: create-variable-and-print-content}
{i: =}

{aside}
The next step after greeting the world is greeting the programmer.
However, before we get there we would like to create a variable.
We created a variable called `person` and put the name of the programmer in it.
We also say we assigned a value to a variable.
For whatever reason most of the programmer are called `Foo` so we'll go with that name here too.

We then use `puts` to print out the content of the variable.

This will print `Foo` to the screen.
{/aside}

![](examples/intro/foo.rb)

## Hello Foo using puts
{id: hello-foo-puts}
{i: puts}
{i: ,}

{aside}
It is not enought to print the name of the programmer, we would also want to greet the programmer.

We print the first part of the message, the variable, and the last part of the message in a single call to `puts`.
We need to separate these parts with a comma (`,`).
{/aside}

![](examples/intro/hello_foo_puts.rb)

{aside}
We got everything on the screen, but we are slightly disappointed as `puts` put each part of our message on a seaparate line. That's not really nice.
{/aside}

![](examples/intro/hello_foo_puts.out)

{aside}
In more technical terms, `puts` printed a `newline` after printing each one of its parameters.
{/aside}

## Hello Foo - print
{id: hello-foo-print}
{i: print}

{aside}
One way to improve the situation is to use the `print` function instead of the `puts` function to print to the screen.

That gave us a much nicer result as it did not print a newline after each item thereby moving the next one to the next line.
However, it also did not print a newline at the end of the whole print operation, which would have been also less convenient.
So in order to make it nicer we had to include `\n` at the end of our message to make it nicer.
`\n` represent a newline so when we include `\n` in whaever we print the next thing will be printed on the following line.
{/aside}

![](examples/intro/hello_foo_print.rb)
![](examples/intro/hello_foo_print.out)

## Ruby interpolate
{id: ruby-interpolate-in-string}

{aside}
To further improve the situation we are going to use the interpolation capabilities of Ruby.
We can insert a hashmark followed by a variable between a pair of curly braces in a string.
Ruby will replace that whole construct with the value of thet variable.

Here however the behavior of double-quote and single-quote is different. The interpolation
only works in double-quoted strings. Single-quoted strings will just include the hash-mark,
the opening curly, the variable name and the closing curly.
{/aside}

![](examples/intro/interpolate.rb)
![](examples/intro/interpolate.out)

## Hello Foo - puts
{id: hello-foo-with-interpolation}

{aside}
Putting the interpolation to use here is how we greet our programmer using `puts` and a variable interpolated in a double-quoted string.
{/aside}

![](examples/intro/hello_foo.rb)
![](examples/intro/hello_foo.out)

## Hello Foo STDIN read
{id: hello-foo-stdin}
{i: STDIN}
{i: gets}


{aside}
What if the person is not called Foo? What if we would like to ask the users of their name and greet them that way?
We can do this by reading from the keyboard which is, in technical terms called Standard Input or STDIN.

This is how we do it:
{/aside}

![](examples/intro/hello_foo_stdin.rb)

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

{aside}
Why is it printed in two rows?

Because after we typed in Bar we pressed ENTER to tell the computer that we are done. However that ENTER generats a newline and that is included
in the text our program receives. So in the variable `person` we have a newline at the end and when we print it, the next thing will be shown
on a new line.
{/aside}

## Hello Foo STDIN and strip
{id: hello-foo-stdin-strip}
{i: STDIN}
{i: gets}
{i: strip}

{aside}
The solution is to remove the newline from the end of the string. We can do this using the `strip` method:
{/aside}

![](examples/intro/hello_foo_stdin_strip.rb)

Now if we run the program and identify as `Bar`, the output will look the way we wanted:


```
Hello Bar, how are you?
```


## Hello Foo - puts
{id: hello-foo-capitalize}
{i: capitalize}

![](examples/intro/hello_foo_capitalize.rb)
![](examples/intro/hello_foo_capitalize.out)


## Ruby command line arguments ARGV
{id: ruby-command-line-arguments-argv}
{i: ARGV}

![](examples/intro/cli.rb)

$ ruby examples/intro/cli.rb a b d

![](examples/intro/cli.out)

## Hello Foo ARGV
{id: hello-foo-argv}
{i: ARGV}

{aside}
Finally we could also expect the users to supply their name when they run the program.
For this we'll use the ARGV array that contains all the values that were passed to the program on the command line.

We'll take the first element of the array (that has index 0) and use that:
{/aside}

![](examples/intro/hello_foo_argv.rb)

Run like this:

```
ruby examples/intro/hello_foo_argv.rb Bar
```

This is the output:

```
Hello Bar, how are you?
```

## Ruby conditionals - if statement
{id: ruby-conditionals-if-statement}
{i: if}

![](examples/intro/if.rb)


## Ruby conditionals - if else statement
{id: ruby-conditionals-if-else-statement}
{i: else}

![](examples/intro/if-else.rb)

## Ruby path to current script
{id: ruby-path-to-current-script}
{i: $0}

![](examples/intro/current_script.rb)

## Variable Types in Ruby
{id: ruby-variable-types}
{i: class}
{i: type}
{i: Integer}
{i: Float}
{i: String}
{i: NilClass}
{i: TrueClass}
{i: FalseClass}
{i: Array}
{i: Hash}

![](examples/intro/variable_types.rb)

## Resources
{id: ruby-resources}

* [Ruby language home page](http://www.ruby-lang.org/)
* [Ruby Weekly newsletter](http://rubyweekly.com/)
* [Ruby Tapas - short screencasts](http://www.rubytapas.com/)
* [Ruby Inside](http://www.rubyinside.com/)



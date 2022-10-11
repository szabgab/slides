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
{i: puts}

{aside}

The required "Hello World" example. Create the file called **hello.rb** with the following content. Then go to the command line, to the same directory
where you have the hello.rb saved and type **ruby hello.rb**.
{/aside}
![](examples/intro/hello.rb)

**ruby hello.rb**



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



## Hello Foo - puts
{id: hello-foo-puts}
{i: puts}

![](examples/intro/hello_foo_puts.rb)
![](examples/intro/hello_foo_puts.out)


## Hello Foo - print
{id: hello-foo-print}
{i: print}

![](examples/intro/hello_foo_print.rb)
![](examples/intro/hello_foo_print.out)


## Hello Foo - puts
{id: hello-foo}

![](examples/intro/hello_foo.rb)
![](examples/intro/hello_foo.out)


## Hello Foo - puts
{id: hello-foo-capitalize}
{i: puts}

![](examples/intro/hello_foo_capitalize.rb)
![](examples/intro/hello_foo_capitalize.out)


## Ruby command line arguments ARGV
{id: ruby-command-line-arguments-argv}
{i: capitalize}

![](examples/intro/hello_foo_capitalize.rb)

$ ruby examples/intro/cli.rb a b d

![](examples/intro/hello_foo_capitalize.out)

## Ruby conditionals - if statement
{id: ruby-conditionals-if-statement}
{i: if}

![](examples/intro/if.rb)


## Ruby conditionals - if else statement
{id: ruby-conditionals-if-else-statement}
{i: else}

![](examples/intro/if-else.rb)

## Resources
{id: ruby-resources}

* [Ruby language home page](http://www.ruby-lang.org/)
* [Ruby Weekly newsletter](http://rubyweekly.com/)
* [Ruby Tapas - short screencasts](http://www.rubytapas.com/)
* [Ruby Inside](http://www.rubyinside.com/)



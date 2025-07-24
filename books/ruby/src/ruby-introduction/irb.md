# irb - Interactive Ruby


irb on Linux and Mac, fxri on Windows




Before starting to write scripts, let's take a look at irb, the Interactive Ruby Shell.
A REPL (Read Evaluate Print Loop) that can help you explore the languages.
Just type **irb** on the command line and it will give you its own prompt.
There you can type in ruby statements.


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



Simply typing in numerical or string expressions will print the result. Calling the **puts** ruby function will also print to the screen,
but then the REPL will print the "result" of puts, which is **nil**. We can assign values to variables, and then use them in other expressions.
Finally **exit** will let us leave the Interactive Ruby session.



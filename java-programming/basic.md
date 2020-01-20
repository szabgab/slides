# First steps
{id: first-steps}

## Java Installation
{id: java-installation}
{i: JRE}
{i: JDK}
{i: java}
{i: javac}

* [Download Java](https://java.com/en/download/)
* JRE - Java Runtime Environment (Java Virtual Machine JVM)
* JDK - Java Development Kit (Java Compiler javac)


```
$ java -version
java version "1.8.0_60"
Java(TM) SE Runtime Environment (build 1.8.0_60-b27)
Java HotSpot(TM) 64-Bit Server VM (build 25.60-b23, mixed mode)
```


```
$ javac -version
javac 1.8.0_60
```


## Hello World in Java
{id: java-hello-world}
{i: System.out.println}
![](examples/HelloWorld.java)

```
$ javac HelloWorld.java       # Compiles the file and creates HelloWorld.class
$ java HelloWorld
Hello World
```


## Java Data Types
{id: java-data-types}

```
42          - int
1_234       - int
true, false - boolean
"string"    - string in double quotes
'x'         - char in single quotes

'x' == "x"  - execption as cannot compare char with string.

"abc".getClass() works and prints class java.lang.String, but does not work on any of the other data types
```


## Java Variable declaration
{id: java-variable-declaration}

With and without initialization.

![](examples/Variables.java)



## Java comments
{id: java-comments}
{i: //}
{i: /*}

* // single-line comment
* /* multi-line comment  */



## Java prompt - read from STDIN
{id: java-prompt}
![](examples/Prompt.java)


## Java command line arguments
{id: java-command-line-arguments}
![](examples/CmdLineArgs.java)


## Java for-loop
{id: java-for-loop}
{i: for}
![](examples/ForLoop.java)


## Java while-loop
{id: java-while-loop}
{i: while}
![](examples/WhileLoop.java)


## Add Command line values
{id: java-add-command-line-values}
![](examples/AddCmdLineArgs.java)


## Add Command line numbers
{id: java-add-command-line-numbers}
![](examples/AddCmdLineNumbers.java)


## Use class
{id: java-use-class-in-same-file}
![](examples/GreetingsA.java)


## Method signature
{id: java-method-signature}
![](examples/GreetingsB.java)



## Use Java class from another class
{id: java-class-from-other-class}

![](examples/mymath/Calculator.java)
![](examples/mymath/UseCalc.java)

```
cd examples/mymath
rm -f *.class; javac Calculator.java UseCalc.java ; java UseCalc
```


## Other
{id: other}
![](examples/Calc.java)
![](examples/Cat.java)
![](examples/Grep.java)
![](examples/ReadFile.java)
![](examples/ReadLine.java)
![](examples/Regex.java)
![](examples/RegexTestHarness.java)
![](examples/SplitString.java)





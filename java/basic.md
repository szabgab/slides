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

![](examples/java/HelloWorld.java)

```
$ javac HelloWorld.java       # Compiles the file and creates HelloWorld.class
$ java HelloWorld
Hello World
```


## Java Data Types
{id: java-data-types}

Primitive types such as int, float, boolean, etc. Or reference types, such as strings, arrays, or objects.

```
42          - int
1_234       - int
true, false - boolean
"string"    - string in double quotes
'x'         - char in single quotes

'x' == "x"  - execption as cannot compare char with string.

"abc".getClass() works and prints class java.lang.String, but does not work on any of the other data types
```

![](examples/java/CheckDataTypes.java)

## Java Variable declaration
{id: java-variable-declaration}

With and without initialization.

![](examples/java/Variables.java)



## Java comments
{id: java-comments}
{i: //}
{i: /*}

* // single-line comment
* /* multi-line comment  */



## Java prompt - read from STDIN
{id: java-prompt}

![](examples/java/Prompt.java)


## Java command line arguments
{id: java-command-line-arguments}

![](examples/java/CmdLineArgs.java)


## Java for-loop
{id: java-for-loop}
{i: for}

![](examples/java/ForLoop.java)


## Java while-loop
{id: java-while-loop}
{i: while}

![](examples/java/WhileLoop.java)


## Convert string to number
{id: convert-string-to-number}

![](examples/java/Convert.java)


## Add Command line values
{id: java-add-command-line-values}

![](examples/java/AddCmdLineArgs.java)


## Add Command line numbers
{id: java-add-command-line-numbers}

![](examples/java/AddCmdLineNumbers.java)


## Use class
{id: java-use-class-in-same-file}

![](examples/java/GreetingsA.java)


## Method signature
{id: java-method-signature}

![](examples/java/GreetingsB.java)



## Use Java class from another class
{id: java-class-from-other-class}

![](examples/mymath/Calculator.java)
![](examples/mymath/UseCalc.java)

```
cd examples/mymath
rm -f *.class; javac Calculator.java UseCalc.java ; java UseCalc
```


## Calc
{id: calc}

![](examples/java/Calc.java)

## Cat
{id: cat}

![](examples/java/Cat.java)

## Grep
{id: grep}

![](examples/java/Grep.java)

## Read file
{id: read-file}

![](examples/java/ReadFile.java)

## Read line
{id: read-line}

![](examples/java/ReadLine.java)
![](examples/java/ReadLines.java)

* [Character stream](https://docs.oracle.com/javase/tutorial/essential/io/charstreams.html)
* [read bytestream](https://docs.oracle.com/javase/tutorial/essential/io/bytestreams.html)
* reads characters byte-by-byte


## Regex
{id: regex}

![](examples/java/Regex.java)

## Regex Test harness
{id: regex-test-harness}

![](examples/java/RegexTestHarness.java)

## Split a string
{id: split-a-string}

{i: StringTokenizer}
![](examples/java/SplitString.java)

## Java: Run external program
{id: run-external-program}
{i: InputStream}
{i: Runtime}
{i: getRuntime}
{i: exec}


![](examples/java/Runls.java)


## Compile and Run in shell
{id: compule-and-run-in-shell}

![](examples/java/run.sh)


## Static or Class attribute
{id: static-or-class-attribute}

![](examples/bike/Bike.java)
![](examples/bike/RunBike.java)


## inheritance
{id: inheritance}

![](examples/person/Person.java)
![](examples/person/Worker.java)
![](examples/person/TryClass.java)


## combination
{id: combination}

![](examples/shapes/Point.java)
![](examples/shapes/Line.java)
![](examples/shapes/RunCode.java)


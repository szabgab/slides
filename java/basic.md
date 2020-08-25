# First steps
{id: first-steps}

## Java Installation
{id: java-installation}
{i: JRE}
{i: JDK}
{i: java}
{i: javac}

{aside}
There are several implementation of Java, one currently controlled by Oracle and it can be downloaded from Oracle.com
but as far as I know there are various problematic licensing restrictions.
A better choice is to download the Open JDK.
{/aside}

* [Java Download Open JDK](https://openjdk.java.net/)

{aside}
On MS Windows install it by unipping the .zip file and then configuring the PATH to include the bin/ directory.
{/aside}

{aside}
Before we even write a line of code we would like to make sure that both the java compiler and the java runtime is
accessible for us. So we open a command line window or a Power Shell window and we type in javac --version
and java --version respectively.
{/aside}

On MS Windows

```
> javac --version
javac 14.0.2
```

```
> java --version
openjdk 14.0.2 2020-07-14
OpenJDK Runtime Environment (build 14.0.2+12-46)
OpenJDK 64-Bit Server VM (build 14.0.2+12-46, mixed mode, sharing)
```

On Ubuntu Linux:

```
$ javac -version
javac 1.8.0_252

$ java -version
openjdk version "1.8.0_252"
OpenJDK Runtime Environment (build 1.8.0_252-8u252-b09-1ubuntu1-b09)
OpenJDK 64-Bit Server VM (build 25.252-b09, mixed mode)
```


## Java from Oracle
{id: java-from-oracle}

* [Download Java from Oracle](https://java.com/en/download/)
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
{i: System}
{i: println}

{aside}
Printing Hello World on the screen is a bit more complex in Java than in many of the so-called scripting languages, but still it
is probably the most simple thing you can do in the language. So let's see it.

Create a file with a name like HelloWorld.java . The extension .java is important , so is the name.
In the file we create a class with the same name as the name of the file.
{/aside}

![](examples/java/HelloWorld.java)

```
$ javac HelloWorld.java       # Compiles the file and creates HelloWorld.class
$ java HelloWorld
Hello World
```


## Java Data Types
{id: java-data-types}
{i: String}
{i: int}
{i: double}
{i: boolean}
{i: true}
{i: false}

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

```
javac CheckDataTypes.java
java CheckDataTypes
```

![](examples/java/CheckDataTypes.out)


## Java Variable declaration
{id: java-variable-declaration}
{i: int}
{i: boolean}
{i: char}

With and without initialization.

![](examples/java/Variables.java)

```
javac Variables.java
java Variables
```

![](examples/java/Variables.out)

## Java comments
{id: java-comments}
{i: //}
{i: /*}

* // single-line comment
* /* multi-line comment  */



## Java prompt - read from STDIN
{id: java-prompt}
{i: InputStreamReader}
{i: BufferedReader}
{i: readLine}

![](examples/java/Prompt.java)

```
javac Prompt.java
java Prompt
```

## Convert string to number
{id: convert-string-to-number}
{i: Integer}
{i: parseInt}

![](examples/java/Convert.java)

```
javac Convert.java
java Conver
```

## Add Command line values
{id: java-add-command-line-values}
{i: args}
{i: length}

![](examples/java/AddCmdLineArgs.java)

```
javac AddCmdLineArgs.java
java AddCmdLineArgs Foo Bar
```

## Add Command line integers
{id: java-add-command-line-numbers}
{i: args}
{i: Integer}
{i: parseInt}

![](examples/java/AddCmdLineNumbers.java)

```
javac AddCmdLineNumbers.java
java AddCmdLineNumbers 19 23
```

## Java for-loop
{id: java-for-loop}
{i: for}
{i: ++}

![](examples/java/ForLoop.java)

$ javac ForLoop.java
$ java ForLoop


## Java while-loop
{id: java-while-loop}
{i: while}

![](examples/java/WhileLoop.java)


## Java command line arguments
{id: java-command-line-arguments}

![](examples/java/CmdLineArgs.java)

```
javac CmdLineArgs.java
java CmdLineArgs --name "Foo Bar" --email foo@bar.com
```

## Concatenate strings in Java
{id: concatenate-strings}
{i: +}

* Use the + operator

![](examples/java/ConcatStrings.java)

```
$ javac ConcatStrings.java
$ java ConcatStrings
```

## Use class
{id: java-use-class-in-same-file}

![](examples/java/GreetingsA.java)

```
javac GreetingsA.java
java GreetingsA
```

![](examples/java/GreetingsA.out)

## Method signature
{id: java-method-signature}

![](examples/java/GreetingsB.java)

```
javac GreetingsB.java
java GreetingsB
```

![](examples/java/GreetingsB.out)


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


## Method Overloading
{id: method-overloading}

![](examples/java/MethodOverloading.java)

```
$ javac MethodOverloading.java
$ java MethodOverloading
```

![](examples/java/MethodOverloading.out)


## Public instance attributes
{id: public-instance-attributes}

![](examples/public-attributes/TryPoint.java)
![](examples/public-attributes/Point.java)

## Getter for private instance attributes
{id: getter-for-private-instance-attributes}

![](examples/getter/TryPoint.java)
![](examples/getter/Point.java)

## Setter for private instance attributes
{id: setter-for-private-instance-attributes}

![](examples/setter/TryPoint.java)
![](examples/setter/Point.java)



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

## Combination
{id: combination}

![](examples/shapes/Point.java)
![](examples/shapes/Line.java)
![](examples/shapes/RunCode.java)


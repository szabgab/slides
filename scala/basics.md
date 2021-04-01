# Scala
{id: scala}

## What is Scala?
{id: what-is-scala}

* Scala stands for [Scalable language](https://www.scala-lang.org/)
* Created by Martin Odersky
* Started in 2001, first released in 2004
* Runs on JVM, the Java Virtual Machine


## Install Scala
{id: install-scala}

* On Ubuntu

```
apt install scala
```

## Editors
{id: scala-editors}

* [Scala IDE](http://scala-ide.org/)
* [sbt - Scala Build Tool](https://www.scala-sbt.org/)
* other IDEs

## Everything is an object
{id: everything-is-object-in-scala}


## Check if Java is installed
{id: check-java-version}

```
java -version
```

```
openjdk version "11.0.10" 2021-01-19
OpenJDK Runtime Environment (build 11.0.10+9-Ubuntu-0ubuntu1.20.10)
OpenJDK 64-Bit Server VM (build 11.0.10+9-Ubuntu-0ubuntu1.20.10, mixed mode, sharing)
```

## Scala in Docker
{id: scala-in-docker}

```
docker build -t scala .
docker run --rm -it -v$(pwd):/opt scala
```

```
# java -version
openjdk version "11.0.10" 2021-01-19
OpenJDK Runtime Environment (build 11.0.10+9-Ubuntu-0ubuntu1.20.10)
OpenJDK 64-Bit Server VM (build 11.0.10+9-Ubuntu-0ubuntu1.20.10, mixed mode, sharing)
```

```
# scala -version
Scala code runner version 2.11.12 -- Copyright 2002-2017, LAMP/EPFL
```

## REPL
{id: scala-repl}

* REPL = Read Evaluate Print Loop

```
$ scala
scala> 23 + 19
res0: Int = 42

scala> :quit
```

```
:help
```

## Scala Syntax
{id: scala-syntax}

* Semicolons (;) are optional at the end of the statement

## Hello World in Scala
{id: hello-world-in-scala}


![](examples/HelloWorld.scala)

Run Hello World in the REPL


```
$ scala
scala> :load Hello.scala
scala> Hello.main(null)
scala> Hello.main(Array())
```

```
$ scalac  HelloWorld.scala
$ scala   HelloWorld
Hello World!
```

![](examples/HelloName.scala)

## Run (Shell script)
{id: run}

![](examples/run.sh)

## Hello Name (command line parameters)
{id: hello-name}

```
$ scalac HelloName.scala
$ scala HelloName Foo
Hello Foo!
```

## var vs val
{id: var-vs-val}

`val` creates an immutable object.
`var` create mutable object.

## val is immutable
{id: val-is-immutable}

![](examples/ValIsImmutable.scala)

```
ValIsImmutable.scala:5: error: reassignment to val
        counter = 1
                ^
one error found
```

## var is immutable
{id: var-is-immutable}

![](examples/VarIsMutable.scala)


```
0
1
```

## Concatenate strings
{id: concatenate-strings}

![](examples/ConcatenateStrings.scala)

## Add Numbers (convert string to int)
{id: add-numbers}
{i: toInt}

![](examples/AddNumbers.scala)


## Run with sbt
{id: run-with-sbt}

* Create directory structure:

```
hello-world/
├── build.sbt
├── project
│   └── build.properties
└── src
    └── main
        └── scala
            └── Main.scala
```

![](examples/hello-world/src/main/scala/Main.scala)

## Comments
{id: comments-in-scala}


```
// Single line
```

```
/*
   Multi line
*/
```

## Scala While loop
{id: while-loop}

![](examples/WhileLoop.scala)


## Scala For loop
{id: for-loop}

![](examples/ForLoop.scala)
![](examples/ForLoopRange.scala)

## Scala show dates
{id: scala-show-dates}

![](examples/ShowDates.scala)

## More
{id: more}

* Lengths of array

* Left facing arrow `<-`


![](examples/Names.scala)
![](examples/Try.scala)


# Scala
{id: scala}

## What is Scala?
{id: what-is-scala}

* Scala stands for [Scalable language](https://www.scala-lang.org/)
* Created by Martin Odersky
* Started in 2001, first released in 2004
* Runs on JVM, the Java Virtual Machine

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
docekr run --rm -it scala
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




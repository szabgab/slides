# Jython - Python running on the JVM
{id: jython}

## Jython Installation
{id: jython-installation}
{i: java}
{i: jython}

* [Jython](http://www.jython.org/)
* java -jar jython-installer-2.7.0.jar
* ~/jython2.7.0/


## Jython Installation
{id: run-jython}

```
java -jar ~/jython2.7.0/jython.jar

java -jar ~/jython2.7.0/jython.jar some.py
```


## Jython load Java class
{id: jython-load-java-class}

```
cd examples/mymath/
java -jar ~/jython2.7.0/jython.jar
Jython 2.7.0 (default:9987c746f838, Apr 29 2015, 02:25:11)
[Java HotSpot(TM) 64-Bit Server VM (Oracle Corporation)] on java1.8.0_60
Type "help", "copyright", "credits" or "license" for more information.
>>> import Calculator
>>> Calculator.add(2, 3)
5
>>> Calculator.add(10, 3)
10
>>>
```


## Jython load Java class in code
{id: jython-load-java-class-in-code}

![](examples/jython/mymath/Calculator.java)
![](examples/jython/mymath/calc.py)

```
cd examples/jython/mymath/
java -jar ~/jython2.7.0/jython.jar calc.py
```


## Jython test Java class
{id: jython-test-java-class}

![](examples/jython/mymath/test_calc.py)

```
java -jar ~/jython2.7.0/jython.jar calc.py
java -jar ~/jython2.7.0/jython.jar -m unittest discover
```

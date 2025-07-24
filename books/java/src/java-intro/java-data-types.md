# Java Data Types

* String
* int
* double
* boolean
* true
* false

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

{% embed include file="src/examples/java/CheckDataTypes.java" %}

```
javac CheckDataTypes.java
java CheckDataTypes
```

{% embed include file="src/examples/java/CheckDataTypes.out" %}



# Use Java class from another class


{% embed include file="src/examples/mymath/Calculator.java" %}
{% embed include file="src/examples/mymath/UseCalc.java" %}

```
cd examples/mymath
rm -f *.class; javac Calculator.java UseCalc.java ; java UseCalc
```




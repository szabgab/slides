# Jython test Java class

{% embed include file="src/examples/jython/mymath/test_calc.py" %}

```
java -jar ~/jython2.7.0/jython.jar calc.py
java -jar ~/jython2.7.0/jython.jar -m unittest discover
```


# Include executables

```
root/
  setup.py
  README.rst
  MANIFEST.in
  bin/
    runmymath.py
    runmymath.bat
  mymath/
    __init__.py
    calc.py
```
{% embed include file="src/examples/package/3/bin/runmymath.py" %}
{% embed include file="src/examples/package/3/bin/runmymath.bat)

setup.py will need to get


```
    scripts=['bin/runmymath.py', 'bin/runmymath.bat'],
```




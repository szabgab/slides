# Add tests

* unittest
* discover

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
        test/
          __init__.py
          test_all.py
          test_calc.py
```
{% embed include file="src/examples/package/3/mymath/test/__init__.py" %}

```
python mymath/test/test_calc.py
python mymath/test/test_all.py
```

```
python -m unittest discover
```





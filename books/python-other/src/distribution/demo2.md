# Distribution demo 2

* The name of the package (demo2a in setup.py) and the name of the module (the filename demo2b.py) don't neet to be the same.
* The name of the folder (demo2)

{% embed include file="src/examples/distribution/demo2/demo2b.py" %}
{% embed include file="src/examples/distribution/demo2/setup.py" %}


* Install:

```
pip install .
```

* Use the name of the module

```
python -m demo2b
```

* Uninstall using the package name

```
pip uninstall demo2a --yes
```


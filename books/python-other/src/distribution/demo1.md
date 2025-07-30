# Distribution demo 1

{% embed include file="src/examples/distribution/demo1/demo1.py" %}
{% embed include file="src/examples/distribution/demo1/setup.py" %}


* Install from the current folder

```
pip install .
```

* Use it on the command line: (try it in a different folder!)

```
python -m demo1

/home/gabor/venv3/lib/python3.10/site-packages/demo1.py
```

* Use it in the interactive shell

```
python
>>> import demo1
>>> demo1.whoami()
```

* Uninstall (without asking questions)

```
pip uninstall demo1 --yes
```

{% embed include file="src/examples/distribution/demo1/.gitignore" %}



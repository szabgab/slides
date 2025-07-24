# Relative path


* __file__
* dirname
* abspath
* sys.path

```
../project_root/
     bin/relative_path.py
     lib/my_module.py
```


We can use a directory structure that is more complex than the flat structure we had earlier. In this case the location of the modules relatively to the scripts
is fixed. In this case it is "../lib". We can compute the relative path in each of our scripts. That will ensure we pick up the right module every time we run the script.
Regardless of the location of the whole project tree.


{% embed include file="src/examples/modules/project_root/lib/my_module.py" %}
{% embed include file="src/examples/modules/project_root/bin/relative_path.py" %}




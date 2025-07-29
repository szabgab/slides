# cwd context manager

{% embed include file="src/examples/context/mycwd.py" %}
{% embed include file="src/examples/context/context_cd.py" %}

```
$ python context_cd.py /tmp
/home/gabor/work/slides/python/examples/context
/home/gabor/work/slides/python/examples/context

$ python context_cd.py /opt
/home/gabor/work/slides/python/examples/context
/home/gabor/work/slides/python/examples/context
```


